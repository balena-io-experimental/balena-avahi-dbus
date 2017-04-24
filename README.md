# resin-avahi-dbus

Example project to announce mDNS/Avahi services over dbus on resin.io / resinOS 2.0
devices.

The project deploys a trivial Python webserver, and uses a helper script, and
[`dbus-python`](https://dbus.freedesktop.org/doc/dbus-python/doc/tutorial.html)
underneath to announce the service on the local network using the system Avahi.

**Important**: this will work only with resinOS 2.x devices, where the host OS will
provide a system Avahi daemon! For resinOS 1.x devices check
[resin-mdns-service](https://github.com/resin-io-playground/resin-mdns-service) for
an example how to announce a service with Avahi daemon installed within the container
and adding the relevant service files.

## Avahi + dbus notes

If you are using the module in the `avahi` directory within this repository,
you can just call the following to announce the webserver, for example.

```
from avahi.service import AvahiService
avahiservice = AvahiService("resin webserver", "_http._tcp", 80)
```

Note that it's important to also set the correct `DBUS_SYSTEM_BUS_ADDRESS` value
to talk to the system dbus, as shown in the `start.sh` start script:

```
export DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket
```
or in many cases you can instead set it as an environment variable in the `Dockerfile` with
```
ENV DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket
```

For more details on this please check the [Dbus communication with hostOS](https://docs.resin.io/runtime/runtime/#dbus-communication-with-hostos)
section of the documentation.

## License

Copyright 2017 Resinio Ltd

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
