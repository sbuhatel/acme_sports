#
# Entry point for the microservice
# @version 1.0
# @author Sergiu Buhatel <sergiu.buhatel@gmail.ca>
#

from acme_sports_api.web.views import *
from acme_sports_api import acme_sports_factory
from acme_sports_api.extensions import app

app.app_context().push()
acme_sports_factory.register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=7000)