import unittest
from datetime import datetime

from GSCore.node.node_entity import Node
from GSCore.node.node_evaluator import NodeEvaluator
from GSCore.node.node_info import NodeInfo

from GSCore.branch.branch_entity import Branch
from GSCore.branch.branch_evaluator import BranchEvaluator
from GSCore.branch.branch_info import BranchInfo


class BranchEntityTest(unittest.TestCase):
    def test_equals(self):
        begin_node = Node(NodeEvaluator(v_rate=110, handle="NODE1"))
        end_node = Node(NodeEvaluator(v_rate=220, handle="NODE2"))
        branch1 = Branch(begin_node, end_node)
        branch2 = Branch(begin_node, end_node)
        self.assertEqual(branch1, branch2)

    def test_defaults(self):
        begin_node = Node()
        end_node = Node()
        branch = Branch(begin_node, end_node)
        self.assertEqual(branch.comissioning_date, None)
        self.assertEqual(branch.evaluator, BranchEvaluator())
        self.assertEqual(branch.info, BranchInfo())

    def test_complete_node(self):
        comiss_date = datetime(year=2026, month=12, day=12)
        begin_node = Node(NodeEvaluator(v_rate=220, handle="NODE1"))
        end_node = Node(NodeEvaluator(v_rate=110, handle="NODE2"))
        evaluator = BranchEvaluator(resistance=.5,
                                    reactance=0.6,
                                    conductance=0.001,
                                    susceptance=- 0.001,
                                    loss_distrib=0.1)
        info = BranchInfo("Full_name",
                          "disp",
                          "AC-240",
                          650,
                          42,
                          650,
                          1000,
                          1,
                          olt_step=1,
                          steps_num=5)
        branch = Branch(begin_node, end_node, evaluator, info, comiss_date)
        self.assertEqual(branch.comissioning_date, comiss_date)
        self.assertEqual(branch.evaluator, BranchEvaluator(begin_handle="NODE1",
                                                           end_handle="NODE2",
                                                           resistance=0.5,
                                                           reactance=0.6,
                                                           conductance=0.001,
                                                           susceptance=- 0.001,
                                                           loss_distrib=0.1,
                                                           active_tc=0.5))
        self.assertEqual(branch.info, BranchInfo("Full_name",
                                                 "disp",
                                                 "AC-240",
                                                 650,
                                                 42,
                                                 650,
                                                 1000,
                                                 1,
                                                 olt_step=1,
                                                 steps_num=5,
                                                 rate_tc=0.5,
                                                 current_tc=0.5,
                                                 olt_series=".52,.51,.5,.49,.48"))


if __name__ == '__main__':
    unittest.main()
