import dbus
from time import sleep

sys_bus = dbus.SystemBus()
print(sys_bus)

def check():
    sys_bus = dbus.SystemBus()
    try:
        raw_server = sys_bus.get_object('org.freedesktop.Avahi', '/')
        server = dbus.Interface(raw_server, 'org.freedesktop.Avahi.Server')
        print(server.GetVersionString())
    except dbus.DBusException:
        return False
    return False

def run():
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
                                "webServer", # sname
                                "_http._tcp", # stype
                                "local", # sdomain
                                "0536ffe-0536ffe.local", # shost - should fill out programmically
                                dbus.UInt16(8080), # port
                                dbus.Array(signature="aay"))
    server2.Commit()
    print(server2.GetState()) # should be 1, as now up

if __name__ == "__main__":
    check()
    run()
    while True:
        print("Running Server")
        sleep(60)
