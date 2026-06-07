"""
Test setup. Puts scripts/ on sys.path so `from lib import vault` resolves
the same way the engines import it (lib is a namespace package under scripts/).
"""
import sys
from pathlib import Path

SCRIPTS = Path(__file__).parent.parent / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
