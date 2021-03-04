#
# Provider that does all the work
# @version 1.0
# @author Sergiu Buhatel <sergiu.buhatel@gmail.ca>
#

from sqlalchemy.sql import text
from acme_sports_api.extensions import app
import json
import requests

class EventsProvider:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __get_team_ranking(self):
        url = app.config['API'].get('team_ranking')
        team_ranking = requests.get(url)
        if team_ranking.status_code == 200:
            return json.loads(team_ranking.content).get('results').get('data')
        else:
            return "Unexpected error has occured"

    def __get_scoreboard(self):
        if self.start is None or self.end is None:
            return "Specify start and end as dates in this format: YYYY-MM-DD"
        url = app.config['API'].get('prefix_scoreboard') + "/" + self.start + "/" \
                     + self.end + app.config['API'].get('postfix_scoreboard')
        scoreboard = requests.get(url)
        if scoreboard.status_code == 200:
            return json.loads(scoreboard.content).get('results')
        else:
            return "Unexpected error has occured"

    def __create_event(self, data_value):
        event = {}
        fields = ['event_id', 'event_date', 'away_team_id', 'away_nick_name', 'away_city',
                              'home_team_id', 'home_nick_name', 'home_city']
        for _, field in enumerate(fields):
            if field == 'event_date':
                event[field] = data_value.get(field)[:10]
                event['event_time'] = data_value.get(field)[11:]
                continue
            if field == 'away_team_id':
                team_info = self.__get_team_info(data_value.get(field))
                event['away_rank'] = team_info['rank']
                event['away_rank_points'] = team_info['points']
            if field == 'home_team_id':
                team_info = self.__get_team_info(data_value.get(field))
                event['home_rank'] = team_info['rank']
                event['home_rank_points'] = team_info['points']
            event[field] = data_value.get(field)
        return event

    def __get_team_info(self, team_id):
        for _, value in enumerate(self.team_ranking):
            if value.get('team_id') == team_id:
                return value
        return None

    def get_events(self):
        events = []
        self.team_ranking = self.__get_team_ranking()
        scoreboard = self.__get_scoreboard()
        for _, date_as_key in enumerate(scoreboard):
            if len(scoreboard[date_as_key]) > 0:
                data = scoreboard[date_as_key].get('data')
                for _, value in enumerate(data):
                    data_value = data[value]
                    event = self.__create_event(data_value)
                    events.append(event)
        return str(events)