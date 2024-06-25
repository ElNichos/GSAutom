from GSCore.entity import CompositeEntity


class BranchInfo(CompositeEntity):
    def __init__(self, full_name: str = "",
                 disp_name: str = "",
                 wire_type: str = "",
                 v_rate: int | float = None,
                 length: int | float = None,
                 heating_limit_current: int | float = None,
                 fault_limit_current: int | float = None,
                 s_rate: int | float = None,
                 rate_tc: int | float = None,
                 current_tc: int | float = None,
                 olt_step: int | float = None,
                 steps_num: int | float = None,
                 olt_series: str = ""):
        self.full_name = full_name
        self.disp_name = disp_name
        self.wire_type = wire_type
        self.v_rate = v_rate
        self.length = length
        self.i_heat = heating_limit_current
        self.i_fault = fault_limit_current
        self.s_rate = s_rate
        self._rate_tc = rate_tc
        self.current_tc = current_tc
        self._olt_step = olt_step / 100 if olt_step is not None else None
        self._steps_num = steps_num
        self._olt_series = self._calculate_olt_series()

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
    def disp_name(self):
        return self._dispatch_name

    @disp_name.setter
    def disp_name(self, value):
        if type(value) is str:
            self._dispatch_name = value
        else:
            self._dispatch_name = ""

    @property
    def wire_type(self):
        return self._wire_type

    @wire_type.setter
    def wire_type(self, value):
        if type(value) is str:
            self._wire_type = value
        else:
            self._wire_type = ""

    @property
    def v_rate(self):
        return self._v_rate

    @v_rate.setter
    def v_rate(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._v_rate = value
        else:
            self._v_rate = None

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._length = value
        else:
            self._length = None

    @property
    def i_heat(self):
        return self._heating_limit_current

    @i_heat.setter
    def i_heat(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._heating_limit_current = value
        else:
            self._heating_limit_current = None

    @property
    def i_fault(self):
        return self._fault_limit_current

    @i_fault.setter
    def i_fault(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._fault_limit_current = value
        else:
            self._fault_limit_current = None

    @property
    def s_rate(self):
        return self._s_rate

    @s_rate.setter
    def s_rate(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._s_rate = value
        else:
            self._s_rate = None

    @property
    def rate_tc(self):
        return self._rate_tc

    @rate_tc.setter
    def rate_tc(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._rate_tc = value
            self._olt_series = self._calculate_olt_series()
        else:
            self._rate_tc = None

    @property
    def current_tc(self):
        return self._current_tc

    @current_tc.setter
    def current_tc(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._current_tc = value
        else:
            self._current_tc = None

    @property
    def olt_step(self):
        return self._olt_step

    @olt_step.setter
    def olt_step(self, value):
        if value is not None and type(value) is int or type(value) is float and value > 0:
            self._olt_step = value / 100
            self._olt_series = self._calculate_olt_series()
        else:
            self._olt_step = None

    @property
    def steps_num(self):
        return self._steps_num

    @steps_num.setter
    def steps_num(self, value):
        if value is not None and type(value) is int:
            if value % 2 != 0:
                self._steps_num = value
                self._olt_series = self._calculate_olt_series()
            else:
                raise ValueError("Steps number must be an even number")
        else:
            self._steps_num = None

    @property
    def olt_series(self):
        self._olt_series = self._calculate_olt_series()
        return self._olt_series

    def _calculate_olt_series(self) -> str:
        olt_series = ""
        if self._steps_num is not None and self._olt_step is not None and self._rate_tc is not None:
            half_steps = int((self._steps_num - 1)/2)
            for i in range(-half_steps, half_steps+1)[::-1]:
                tap_value = self.rate_tc + (i * self._olt_step)
                if i == -half_steps:
                    olt_series += f"{tap_value:}"[1:]
                else:
                    olt_series += f"{tap_value:},"[1:]
        return olt_series
