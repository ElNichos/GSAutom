from datetime import datetime

from .entity import NetEntity
from .node_evaluator import NodeEvaluator
from .node_info import NodeInfo


class Node(NetEntity):
    def __init__(self, evaluation_data: NodeEvaluator = None,
                 info_data: NodeInfo = None,
                 comiss_date: datetime = None):
        if evaluation_data is None:
            self._evaluation_data = NodeEvaluator()
        else:
            self._evaluation_data = evaluation_data

        if info_data is None:
            self._info_data = NodeInfo()
        else:
            self._info_data = info_data

        if comiss_date is None:
            self._comiss_date = None
        else:
            self._commissioning_date = comiss_date

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

    @property
    def info(self):
        return self._info_data

    @info.setter
    def info(self, value):
        if not isinstance(value, NodeInfo):
            raise ValueError(f"{value} is not an instance of NodeInfo")
        if value is None:
            self._info_data = NodeInfo()
        else:
            self._info_data = value

    @property
    def comiss_date(self):
        return self._commissioning_date

    @comiss_date.setter
    def comiss_date(self, value):
        if not isinstance(value, datetime):
            raise ValueError(f"{value} is not an instance of datetime")
        if value is None:
            self._commissioning_date = None
        else:
            self._commissioning_date = value
