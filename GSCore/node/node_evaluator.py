from GSCore.entity import CompositeEntity


class NodeEvaluator(CompositeEntity):
    def __init__(self, slc: int = None,
                 node_id: int = None,
                 v_rate: float = None,
                 p_load: float = None,
                 q_load: float = None,
                 p_gen: float = None,
                 q_gen: float = None,
                 v_module: float = None,
                 q_gen_min: float = None,
                 q_gen_max: float = None,
                 handle: str = ""):
        self._slc = slc
        self._node_id = node_id
        self._v_rate = v_rate
        self._p_load = p_load
        self._q_load = q_load
        self._p_gen = p_gen
        self._q_gen = q_gen
        self._v_module = v_module
        if q_gen_min is not None and q_gen_max is not None:
            if q_gen_min < q_gen_max:
                self._q_gen_min = q_gen_min
                self._q_gen_max = q_gen_max
            else:
                raise ValueError("q_gen_min is lesser than q_gen_max")
        else:
            self._q_gen_min = None
            self._q_gen_max = None
        self._handle = handle

    @property
    def handle(self):
        return self._handle

    @property
    def slc(self):
        return self._slc

    @slc.setter
    def slc(self, value):
        if value is not None and \
                type(value) is int and \
                value in range(1, 6):
            self._slc = value
        else:
            self._slc = None

    @property
    def node_id(self):
        return self._node_id

    @node_id.setter
    def node_id(self, value):
        if value is not None and type(value) is int:
            self._node_id = value
        else:
            self._node_id = None

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
    def p_load(self):
        return self._p_load

    @p_load.setter
    def p_load(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._p_load = value
        else:
            self._p_load = None

    @property
    def q_load(self):
        return self._q_load

    @q_load.setter
    def q_load(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._q_load = value
        else:
            self._q_load = None

    @property
    def p_gen(self):
        return self._p_gen

    @p_gen.setter
    def p_gen(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._p_gen = value
        else:
            self._p_gen = None

    @property
    def q_gen(self):
        return self._q_gen

    @q_gen.setter
    def q_gen(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._q_gen = value
        else:
            self._q_gen = None

    @property
    def v_module(self):
        return self._v_module

    @v_module.setter
    def v_module(self, value):
        if value is not None and type(value) is float or type(value) is int:
            self._v_module = value
        else:
            self._v_module = None

    @property
    def q_gen_min(self):
        return self._q_gen_min

    @q_gen_min.setter
    def q_gen_min(self, value):
        if value is not None and \
                type(value) is float or type(value) is int and \
                value <= self._q_gen_max:
            self._q_gen_min = value
        elif value >= self._q_gen_max:
            raise ValueError("q_gen_max must be bigger than q_gen_min")
        else:
            self._q_gen_min = None

    @property
    def q_gen_max(self):
        return self._q_gen_max

    @q_gen_max.setter
    def q_gen_max(self, value):
        if value is not None and \
                type(value) is float or type(value) is int and \
                value >= self._q_gen_min:
            self._q_gen_max = value
        elif value <= self._q_gen_min:
            raise ValueError("q_gen_max must be bigger than q_gen_min")
        else:
            self._q_gen_max = None
