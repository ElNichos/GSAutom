from datetime import datetime

from GSCore.entity import NetEntity
from .node_evaluator import NodeEvaluator
from .node_info import NodeInfo


class Node(NetEntity):
    def __init__(self, evaluation_data: NodeEvaluator = NodeEvaluator(),
                 info_data: NodeInfo = NodeInfo(),
                 comiss_date: datetime = None):
        self.evaluator = evaluation_data
        self.info = info_data
        self.comissioning_date = comiss_date

    @property
    def evaluator(self):
        return self._evaluation_data

    @evaluator.setter
    def evaluator(self, value):
        if not isinstance(value, NodeEvaluator):
            raise ValueError(f"{value} is not an instance of NodeEvaluator")
        if value is None:
            self._evaluation_data = NodeEvaluator()
        else:
            self._evaluation_data = value
