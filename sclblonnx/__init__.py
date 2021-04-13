"""
The sclblonnx package provides onnx tools
"""
# Ran on import of the package. Check version:
import sys

if sys.version_info < (3, 0):
    print('Sclblonnx requires Python 3, while Python ' + str(sys.version[0] + ' was detected. Terminating... '))
    sys.exit(1)

from .main import display, graph_from_file, empty_graph, new_node, add_input, add_node, add_output, \
    clean, run, graph_to_file, check
from .version import __version__


