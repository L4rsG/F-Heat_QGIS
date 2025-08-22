import sys
from pathlib import Path

# Prepend the package src directory so tests can import modules from FHeat_QGIS/src
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'FHeat_QGIS' / 'src'
sys.path.insert(0, str(SRC))
