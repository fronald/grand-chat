import sys
import os

# Append module directory to python system path (sys.path)
module_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(module_root)
