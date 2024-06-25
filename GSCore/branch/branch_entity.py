from datetime import datetime

from GSCore.entity import NetEntity
from GSCore.node.node_entity import Node
from .branch_evaluator import BranchEvaluator
from .branch_info import BranchInfo


class Branch(NetEntity):
    def __init__(self, begin_node: Node = None,
                 end_node: Node = None,
                 evaluation_data: BranchEvaluator = BranchEvaluator(),
                 info_data: BranchInfo = BranchInfo(),
                 comiss_date: datetime = None):
        self.evaluator = evaluation_data
        self.info = info_data
        self.begin_node = begin_node
        self.end_node = end_node
        self.comissioning_date = comiss_date

    @property
    def begin_node(self):
        return self._begin_node

    @begin_node.setter
    def begin_node(self, value):
        self._check_node_instance(value)
        self._begin_node = value
        self.evaluator.begin_node_handle = value.evaluator.handle
        if "_end_node" in self.__dict__.keys():
            self._set_transform_data(value)

    @property
    def end_node(self):
        return self._end_node

    @end_node.setter
    def end_node(self, value):
        self._check_node_instance(value)
        self._end_node = value
        self.evaluator.end_node_handle = value.evaluator.handle
        if "_begin_node" in self.__dict__.keys():
            self._set_transform_data(value)

    @staticmethod
    def _check_node_instance(value):
        if not isinstance(value, Node):
            raise TypeError(f'Value must be <Node>, not {type(value)}')

    def _set_transform_data(self, value):
        if (self._end_node is not None or self._begin_node is not None) \
                and self._end_node.evaluator.v_rate is not None \
                and value.evaluator.v_rate is not None:
            tc = self._end_node.evaluator.v_rate / self.begin_node.evaluator.v_rate
            self.evaluator.active_tc = tc
            self.info.rate_tc = tc
            self.info.current_tc = tc

    @property
    def evaluator(self):
        return self._evaluation_data

    @evaluator.setter
    def evaluator(self, value):
        if not isinstance(value, BranchEvaluator):
            raise ValueError(f"{value} is not an instance of BranchEvaluator")
        if value is None:
            self._evaluation_data = BranchEvaluator()
        else:
            self._evaluation_data = value

    @property
    def info(self):
        return self._info_data

    @info.setter
    def info(self, value):
        if not isinstance(value, BranchInfo):
            raise ValueError(f"{value} is not an instance of BranchInfo")
        if value is None:
            self._info_data = BranchInfo()
        else:
            self._info_data = value

