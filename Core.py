import os
import Configuration
from Classes.ServerConnection import ServerConnection
from Static.StaticData import StaticData

if not os.path.exists(f"HexDumpV{Configuration.settings['DumpMajor']}"):
    os.mkdir(f"HexDumpV{Configuration.settings['DumpMajor']}")

StaticData.Preload()

ServerConnection(("217.182.216.77", 9339))
