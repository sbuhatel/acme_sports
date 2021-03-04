#
# Views
# @version 1.0
# @author Sergiu Buhatel <sergiu.buhatel@gmail.ca>
#

from flask import request, jsonify, url_for, Blueprint
from flask import json, jsonify, Response, blueprints
from acme_sports_api.web.common_view import acme_sports_bp
from acme_sports_api.decorators.crossorigin import crossdomain
import requests
from acme_sports_api.providers import EventsProvider

@acme_sports_bp.route("/", methods=['GET'])
@crossdomain(origin='*')
def hello():
    return "Hello ACME Sports!"

@acme_sports_bp.route("/events", methods=['GET'])
@crossdomain(origin='*')
def get_events():
    start = request.args.get('start')
    end = request.args.get('end')
    provider = EventsProvider(start, end)
    events = provider.get_events()
    return events

