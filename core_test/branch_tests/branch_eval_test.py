import unittest

from GSCore.branch.branch_evaluator import BranchEvaluator, StateCodes


class BranchEvaluatorGenericTest(unittest.TestCase):
    def test_equals_1(self):
        node_eval_1 = BranchEvaluator()
        node_eval_2 = BranchEvaluator()
        self.assertEqual(node_eval_1, node_eval_2)

    def test_equals_2(self):
        node_eval_1 = BranchEvaluator("0301", 1, "", "",
                                      0.5, 0.6, 0.001, -0.001, 0.1, 1, 0.5)
        node_eval_2 = BranchEvaluator("0301", 1, "", "",
                                      0.5, 0.6, 0.001, -0.001, 0.1, 1, 0.5)
        self.assertEqual(node_eval_1, node_eval_2)

    def test_not_equals_1(self):
        node_eval_1 = BranchEvaluator("*301", 1, "", "",
                                      0.5, 0.6, 0.001, -0.001, 0.1, 1, 0.5)
        node_eval_2 = BranchEvaluator("0301", 1, "", "",
                                      0.5, 0.6, 0.001, -0.001, 0.1, 1, 0.5)
        self.assertNotEqual(node_eval_1, node_eval_2)

    def test_not_equals_2(self):
        node_eval_1 = BranchEvaluator("0301", 1, "", "", 0.5, 0.6, 0.01, -0.001, 0.1, 1, 0.5)
        node_eval_2 = BranchEvaluator("0301", 1, "", "", 0.5, 0.6, 0.1, -0.001, 0.1, 1, 0.5)
        self.assertNotEqual(node_eval_1, node_eval_2)


class BranchEvaluatorPropsTest(unittest.TestCase):
    def test_default(self):
        branch_eval = BranchEvaluator()
        self.assertEqual(branch_eval.resistance, 0.01)
        self.assertEqual(branch_eval.state, "0301")
        self.assertEqual(branch_eval.active_tc, None)
        self.assertEqual(branch_eval.reactance, None)
        self.assertEqual(branch_eval.circuit_num, 1)
        self.assertEqual(branch_eval.begin_node_handle, "")
        self.assertEqual(branch_eval.end_node_handle, "")
        self.assertEqual(branch_eval.conductance, None)
        self.assertEqual(branch_eval.loss_distrib, None)
        self.assertEqual(branch_eval.reactive_tc, None)
        self.assertEqual(branch_eval.susceptance, None)

    def test_resistance(self):
        branch_eval = BranchEvaluator(resistance=-0.4)
        self.assertEqual(branch_eval.resistance, -0.4)
        branch_eval.resistance = 1
        self.assertEqual(branch_eval.resistance, 1)
        branch_eval.resistance = "1"
        self.assertEqual(branch_eval.resistance, None)

    def test_state(self):
        branch_eval = BranchEvaluator()
        branch_eval.state = StateCodes.TurnedOff
        self.assertEqual(branch_eval.state, "*301")
        try:
            branch_eval = BranchEvaluator(state="0.4")
        except ValueError:
            self.assertTrue(True)

    def test_active_tc(self):
        branch_eval = BranchEvaluator(active_tc=-0.4)
        self.assertEqual(branch_eval.active_tc, -0.4)
        branch_eval.active_tc = 1
        self.assertEqual(branch_eval.active_tc, 1)
        branch_eval.active_tc = "1"
        self.assertEqual(branch_eval.active_tc, None)

    def test_reactance(self):
        branch_eval = BranchEvaluator(reactance=-0.4)
        self.assertEqual(branch_eval.reactance, -0.4)
        branch_eval.reactance = 1
        self.assertEqual(branch_eval.reactance, 1)
        branch_eval.reactance = "1"
        self.assertEqual(branch_eval.reactance, None)

    def test_circuit_num(self):
        branch_eval = BranchEvaluator(circuit_num=2)
        self.assertEqual(branch_eval.circuit_num, 2)
        try:
            branch_eval.circuit_num = 0
        except ValueError:
            self.assertTrue(True)

        try:
            branch_eval.circuit_num = "1"
        except ValueError:
            self.assertTrue(True)

    def test_begin_node_handle(self):
        branch_eval = BranchEvaluator(begin_handle="0.4")
        self.assertEqual(branch_eval.begin_node_handle, "0.4")
        try:
            branch_eval.begin_node_handle = 1
        except TypeError:
            self.assertTrue(True)

    def test_end_node_handle(self):
        branch_eval = BranchEvaluator(end_handle="0.4")
        self.assertEqual(branch_eval.end_node_handle, "0.4")
        try:
            branch_eval.end_node_handle = 1
        except TypeError:
            self.assertTrue(True)

    def test_conductance(self):
        branch_eval = BranchEvaluator(conductance=-0.4)
        self.assertEqual(branch_eval.conductance, -0.4)
        branch_eval.conductance = 1
        self.assertEqual(branch_eval.conductance, 1)
        branch_eval.conductance = "1"
        self.assertEqual(branch_eval.conductance, None)

    def test_loss_distrib(self):
        branch_eval = BranchEvaluator(loss_distrib=-0.4)
        self.assertEqual(branch_eval.loss_distrib, -0.4)
        branch_eval.loss_distrib = 1
        self.assertEqual(branch_eval.loss_distrib, 1)
        branch_eval.loss_distrib = "1"
        self.assertEqual(branch_eval.loss_distrib, None)

    def test_reactive_tc(self):
        branch_eval = BranchEvaluator(reactive_tc=-0.4)
        self.assertEqual(branch_eval.reactive_tc, -0.4)
        branch_eval.reactive_tc = 1
        self.assertEqual(branch_eval.reactive_tc, 1)
        branch_eval.reactive_tc = "1"
        self.assertEqual(branch_eval.reactive_tc, None)

    def test_susceptance(self):
        branch_eval = BranchEvaluator(susceptance=-0.4)
        self.assertEqual(branch_eval.susceptance, -0.4)
        branch_eval.susceptance = 1
        self.assertEqual(branch_eval.susceptance, 1)
        branch_eval.susceptance = "1"
        self.assertEqual(branch_eval.susceptance, None)


if __name__ == '__main__':
    unittest.main()
