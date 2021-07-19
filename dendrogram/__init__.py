# Licensed under MIT License - see LICENSE

from . import latticeND, structureTree
from .latticeND import *
from .structureTree import *

__all__ = latticeND.__all__ + structureTree.__all__
__version__ = "0.2"
__name__ = "dendrogram"
__author__ = ["Xi Meng", "Bill Chen"]
