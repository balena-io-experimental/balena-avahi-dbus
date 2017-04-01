import dbus
from time import sleep
from flask import Flask

sys_bus = dbus.SystemBus()
print(sys_bus)

## Dbus

def check():
    """Avahi Server Version Check
    """
    sys_bus = dbus.SystemBus()
    try:
        raw_server = sys_bus.get_object('org.freedesktop.Avahi', '/')
        server = dbus.Interface(raw_server, 'org.freedesktop.Avahi.Server')
        print(server.GetVersionString())
    except dbus.DBusException:
        return False
    return False

def run():
    """Announce server
    """
    raw_server = sys_bus.get_object('org.freedesktop.Avahi', '/')
    server = dbus.Interface(raw_server, 'org.freedesktop.Avahi.Server')
    path = server.EntryGroupNew()
    print(path)

    raw_server2 = sys_bus.get_object('org.freedesktop.Avahi', path)
    server2 = dbus.Interface(raw_server2, 'org.freedesktop.Avahi.EntryGroup')

    print(server2.GetState()) # should be 0, as not up
    print(server2.IsEmpty())
    result = server2.AddService(dbus.Int32(-1), # avahi.IF_UNSPEC
                                dbus.Int32(-1), # avahi.PROTO_UNSPEC
                                dbus.UInt32(0), # flags
                                "Test Server", # sname
                                "_http._tcp", # stype
                                "local", # sdomain
                                "hydra.local", # shost - should fill out programmically
                                dbus.UInt16(8000), # port
                                dbus.Array(signature="aay")) # TXT field, this is empty
    server2.Commit()
    print(server2.GetState()) # should be 1, as now up

## Web server
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World in collaboration with Avahi and DBUS!'

if __name__ == "__main__":
    check()
    run()
    app.run(host='0.0.0.0', port=8000)
