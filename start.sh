#!/usr/bin/env bash

## connect to the host's system bus from the application container
export DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket

python myserver.py
