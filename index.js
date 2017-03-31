const dbus = require('dbus-native');
const avahi = require('avahi-dbus');
let bus =  dbus.systemBus();

let daemon = new avahi.Daemon(bus);
daemon.GetVersionString(function(err, result) {
    console.log("Avahi Version: "+ result);
});

// daemon.ServiceBrowserNew(avahi.IF_UNSPEC, avahi.PROTO_UNSPEC, '_rfb._tcp', 'local', 0, function(err, browser) {
//       browser.on('ItemNew', function(interface, protocol, name, type, domain, flags) {
//                 daemon.ResolveService(interface, protocol, name, type, domain, avahi.PROTO_UNSPEC, 0,
//                         function(err, interface, protocol, name, type, domain, host, aprotocol, address, port, txt, flags) {
//                                       console.log('New item:', interface, protocol, name, type, domain, host, aprotocol, address, port, txt, flags);
//                                               });
//                     });
//       browser.on('ItemRemove', function(interface, protocol, name, type, domain, flags) {
//                 console.log('Removed: ' + name);
//                         });
// });
