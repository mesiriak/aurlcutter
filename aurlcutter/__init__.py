import logging
import importlib
import pkgutil

from ._types import SomeCutterInstance

logger = logging.getLogger(__name__)

__version__ = "0.0.1"
__author__ = "Max Mesiriak"
__email__ = "iamzhv@gmail.com"
__license__ = "GPLv3"


class Cutter(object):
    """
    Factory class for creating cutters instances
    """

    _cutters_path = "aurlcutter.cutters"
    _cutter_class_name = "Cutter"

    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs

        module = importlib.import_module(self._cutters_path)

        self.cutters = [i.name for i in pkgutil.iter_modules(module.__path__)]

    def __getattr__(self, imp: str) -> SomeCutterInstance:
        if imp not in self.cutters:
            return self.__getattribute__(imp)

        cutter_module = importlib.import_module("{}.{}".format(self._cutters_path, imp))
        instance = getattr(cutter_module, self._cutter_class_name)(**self.kwargs)

        return instance
