#
# @version 1.0
# @author Sergiu Buhatel <sergiu.buhatel@gmail.ca>
#

Installation and running steps on macOS:

Step 1 - Download and install Python 3.9.1 64-bit
    https://www.python.org/downloads

Step 2 - Create virtual environment
    python3 -m venv env

Step 3 - Activate virtual environment
    source env/bin/activate

Step 4 - Install dependencies into the current active virtual environment
    pip install -r requirements.txt

Step 5 - Launch the server
    python waitress_server.py

Step 6 - Run in a browser or Postman
    http://localhost:7000/acme_sports_api/events?start=2020-01-12&end=2020-01-19
