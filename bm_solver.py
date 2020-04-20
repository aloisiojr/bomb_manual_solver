#!/usr/local/bin/python3

from modules.Wires import Wires

try:
    while(True):
        Wires().run()
except KeyboardInterrupt:
    pass
