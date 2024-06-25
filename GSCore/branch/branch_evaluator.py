from dataclasses import dataclass

from GSCore.entity import CompositeEntity


@dataclass(frozen=True)
class StateCodes:
    TurnedOn = "0301"
    TurnedOff = "*301"
    StateCodes = (TurnedOn, TurnedOff)


class BranchEvaluator(CompositeEntity):
    def __init__(self, state: str = "0301",
                 circuit_num: int = 1,
                 begin_handle: str = "",
                 end_handle: str = "",
                 resistance: float = 0.01,
                 reactance: float = None,
                 conductance: float = None,
                 susceptance: float = None,
                 active_tc: float = None,
                 reactive_tc: float = None,
                 loss_distrib: float = None):
        self.state = state
        self.circuit_num = circuit_num
        self.begin_node_handle = begin_handle
        self.end_node_handle = end_handle
        self.resistance = resistance
        self.reactance = reactance
        self.conductance = conductance
        self.susceptance = susceptance
        self.active_tc = active_tc
        self.reactive_tc = reactive_tc
        self.loss_distrib = loss_distrib

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if value not in StateCodes.StateCodes:
            raise ValueError(f"Incorrect branch state")
        self._state = value

    @property
    def circuit_num(self):
        return self._circuit_num

    @circuit_num.setter
    def circuit_num(self, value):
        if type(value) is not int:
            raise ValueError(f"Circuit number must be an integer, got {type(value)}")
        if value <= 0:
            raise ValueError(f"Circuit number must be positive integer, got {value}")
        if type(value) is int:
            self._circuit_num = value
        else:
            self._circuit_num = None

    @property
    def begin_node_handle(self):
        return self._begin_node_handle

    @begin_node_handle.setter
    def begin_node_handle(self, value):
        if type(value) is not str:
            raise TypeError(f"Begin node Handle must be a string, not {type(value)}")
        self._begin_node_handle = value

    @property
    def end_node_handle(self):
        return self._end_node_handle

    @end_node_handle.setter
    def end_node_handle(self, value):
        if type(value) is not str:
            raise TypeError(f"End node Handle must be a string, not {type(value)}")
        self._end_node_handle = value

    @property
    def resistance(self):
        return self._resistance

    @resistance.setter
    def resistance(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._resistance = value
        else:
            self._resistance = None

    @property
    def reactance(self):
        return self._reactance

    @reactance.setter
    def reactance(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._reactance = value
        else:
            self._reactance = None

    @property
    def conductance(self):
        return self._conductance

    @conductance.setter
    def conductance(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._conductance = value
        else:
            self._conductance = None

    @property
    def susceptance(self):
        return self._susceptance

    @susceptance.setter
    def susceptance(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._susceptance = value
        else:
            self._susceptance = None

    @property
    def active_tc(self):
        return self._active_tc

    @active_tc.setter
    def active_tc(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._active_tc = value
        else:
            self._active_tc = None

    @property
    def reactive_tc(self):
        return self._reactive_tc

    @reactive_tc.setter
    def reactive_tc(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._reactive_tc = value
        else:
            self._reactive_tc = None

    @property
    def loss_distrib(self):
        return self._loss_distrib

    @loss_distrib.setter
    def loss_distrib(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._loss_distrib = value
        else:
            self._loss_distrib = None
