import unittest
from datetime import datetime

from GSCore.node_entity import Node
from GSCore.node_evaluator import NodeEvaluator
from GSCore.node_info import NodeInfo


class NodeEntityTest(unittest.TestCase):
    def test_equals(self):
        node1 = Node()
        node2 = Node()
        self.assertEqual(node1, node2)

    def test_defaults(self):
        node = Node()
        self.assertEqual(node.comiss_date, None)
        self.assertEqual(node.evaluator, NodeEvaluator())
        self.assertEqual(node.info, NodeInfo())

    def test_complete_node(self):
        comiss_date = datetime(year=2026, month=12, day=12)
        evaluator = NodeEvaluator(1, 57000, 110, 5, 2, 0, 0, 115, -30, 10)
        info = NodeInfo("FullName", "Node", "DispatchName", 0.9, "None")
        node = Node(evaluator, info, comiss_date)
        self.assertEqual(node.comiss_date, comiss_date)
        self.assertEqual(node.evaluator, evaluator)
        self.assertEqual(node.info, info)


if __name__ == '__main__':
    unittest.main()
