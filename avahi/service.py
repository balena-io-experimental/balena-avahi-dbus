import dbus
import os
from time import sleep

from server import AvahiServer

class AvahiService:

    def __init__(self, service_name, service_type, port, txt=[]):
        """Announce a service over Avahi through dbus

        service_name: string with service's name
        service_type: string with service's type, eg. '_http._tcp'
        port: integer with port number
        txt: TXT fields as array of string in a format of ["key1=value1", "key2=value2"], by default it's empty (ie. [])
        """
        self.bus = dbus.SystemBus()
        self.avahiserver = AvahiServer()
        self.path = self.avahiserver.EntryGroupNew()
        raw_server = self.bus.get_object('org.freedesktop.Avahi', self.path)
        self.server = dbus.Interface(raw_server, 'org.freedesktop.Avahi.EntryGroup')

        hostname, domainname = self.avahiserver.GetHostName(), self.avahiserver.GetDomainName()
        self.server.AddService(dbus.Int32(-1), # avahi.IF_UNSPEC
                               dbus.Int32(-1), # avahi.PROTO_UNSPEC
                               dbus.UInt32(0), # flags
                               service_name, # sname
                               service_type, # stype
                               domainname, # sdomain
                               "{}.{}".format(hostname, domainname), # shost
                               dbus.UInt16(port), # port
                               dbus.Array(txt, signature='aay')) # TXT field, this is empty at the moment
        self.server.Commit()

#
#
#
#
# def announce():
#     """Announce server
#     """
#     raw_server = sys_bus.get_object('org.freedesktop.Avahi', '/')
#     server = dbus.Interface(raw_server, 'org.freedesktop.Avahi.Server')
#     hostname = server.GetHostName()
#     path = server.EntryGroupNew()
#     print(path)
#
#     raw_server2 = sys_bus.get_object('org.freedesktop.Avahi', path)
#     server2 = dbus.Interface(raw_server2, 'org.freedesktop.Avahi.EntryGroup')
#
#     print(server2.GetState()) # should be 0, as not up
#     print(server2.IsEmpty())
#     ### This is how hostname should be gotten, but currently it gets the wrong value
#     # hostname = socket.gethostname()
#     ### Workaround
#     # hostname = os.getenv("RESIN_DEVICE_UUID")[:7]
#     print("shost: {}.local".format(hostname))
#     service_name = os.getenv("SERVICE_NAME", "resin.io service")
#     result = server2.AddService(dbus.Int32(-1), # avahi.IF_UNSPEC
#                                 dbus.Int32(-1), # avahi.PROTO_UNSPEC
#                                 dbus.UInt32(0), # flags
#                                 service_name, # sname
#                                 "_http._tcp", # stype
#                                 "local", # sdomain
#                                 "{}.local".format(hostname), # shost
#                                 dbus.UInt16(8000), # port
#                                 dbus.Array([])) # TXT field, this is empty at the moment
#     server2.Commit()
#     print(server2.GetState()) # should be 1, as now up
#
# if __name__ == "__main__":
#     pass
