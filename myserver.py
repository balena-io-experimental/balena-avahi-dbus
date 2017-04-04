
from flask import Flask

from avahi.service import AvahiService

## Web server
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World in collaboration with Avahi and DBUS!'

if __name__ == "__main__":
    avahiservice = AvahiService("resin webserver", "_http._tcp", 80)
    app.run(host='0.0.0.0', port=80)
