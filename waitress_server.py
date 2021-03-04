#
# Production Web Server
# @version 1.0
# @author Sergiu Buhatel <sergiu.buhatel@gmail.ca>
#

from waitress import serve
from app import app
serve(app, listen='127.0.0.1:7000', ipv4=True, ipv6=False, url_scheme='http')

