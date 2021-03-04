#
# Flask Factory
# @version 1.0
# @author Sergiu Buhatel <sergiu.buhatel@gmail.ca>
#

import json

def create_app(package_name):
    from flask import Flask
    app = Flask(package_name)

    with open('client_secrets.json') as client_secrets_file:
        client_secrets = json.load(client_secrets_file)
    app.config['API'] = client_secrets.get('api')

    return app

def register_blueprints(app):
    from acme_sports_api.web.views import acme_sports_bp
    app.register_blueprint(acme_sports_bp, url_prefix='/acme_sports_api')
    return app