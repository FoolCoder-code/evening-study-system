import eel
import os, sys
from pathlib import Path

index_path = Path("/html", "index.html")

eel.init("html")
eel.start("index.html", size=(600, 400))
