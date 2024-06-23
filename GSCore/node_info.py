from .entity import CompositeEntity


class NodeInfo(CompositeEntity):

    def __init__(self, full_name: str = "",
                 net_type: str = "",
                 disp_name: str = "",
                 power_factor: float = None,
                 notation: str = ""):
        self._full_name = full_name
        self._net_type = net_type
        self._dispatch_name = disp_name
        self._power_factor = power_factor
        self._notation = notation

    @property
    def power_factor(self):
        return self._power_factor

    @power_factor.setter
    def power_factor(self, value):
        if value is not None and \
                type(value) is float:
            self._power_factor = value
        else:
            self._power_factor = None

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        if type(value) is str:
            self._full_name = value
        else:
            self._full_name = ""

    @property
    def net_type(self):
        return self._net_type

    @net_type.setter
    def net_type(self, value):
        if type(value) is str:
            self._net_type = value
        else:
            self._net_type = ""

    @property
    def disp_name(self):
        return self._dispatch_name

    @disp_name.setter
    def disp_name(self, value):
        if type(value) is str:
            self._dispatch_name = value
        else:
            self._dispatch_name = ""

    @property
    def notation(self):
        return self._notation

    @notation.setter
    def notation(self, value):
        if type(value) is str:
            self._notation = value
        else:
            self._notation = ""
