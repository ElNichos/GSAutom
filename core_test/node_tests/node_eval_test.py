import unittest

from GSCore.node.node_evaluator import NodeEvaluator


class NodeEvaluatorGenericTest(unittest.TestCase):
    def test_equals_1(self):
        node_eval_1 = NodeEvaluator()
        node_eval_2 = NodeEvaluator()
        self.assertEqual(node_eval_1, node_eval_2)

    def test_equals_2(self):
        node_eval_1 = NodeEvaluator(1, 1, 110, 5, 2, 0, 0, 115, -30, 10)
        node_eval_2 = NodeEvaluator(1, 1, 110, 5, 2, 0, 0, 115, -30, 10)
        self.assertEqual(node_eval_1, node_eval_2)

    def test_equals_3(self):
        node_eval_1 = NodeEvaluator(1, 57000, 110, 5.02, 2.009, 0.001, -0.001, 115.2, -30.09, 10.09)
        node_eval_2 = NodeEvaluator(1, 57000, 110, 5.02, 2.009, 0.001, -0.001, 115.2, -30.09, 10.09)
        self.assertEqual(node_eval_1, node_eval_2)

    def test_not_equals(self):
        node_eval_1 = NodeEvaluator(1, 57000, 110, 5.02, 2.009, 0.001, -0.001, 115.2, -30.09, 10.09)
        node_eval_2 = NodeEvaluator(1, 57001, 110, 5.02, 2.009, 0.001, -0.001, 115.2, -30.09, 10.09)
        self.assertNotEqual(node_eval_1, node_eval_2)


class NodeEvaluatorPropsTest(unittest.TestCase):
    def test_min_max_q_gen_1(self):
        try:
            NodeEvaluator(1, 1, 110, 5, 2, 0, 0, 115, 30, -10)
        except ValueError:
            self.assertTrue(True)

    def test_min_max_q_gen_2(self):
        node_eval = NodeEvaluator()
        node_eval.max_q_gen = -100
        try:
            node_eval.min_q_gen = -110
        except ValueError:
            self.assertTrue(True)

    def test_default(self):
        node_eval = NodeEvaluator()
        self.assertEqual(node_eval.node_id, None)
        self.assertEqual(node_eval.q_gen, None)
        self.assertEqual(node_eval.p_gen, None)
        self.assertEqual(node_eval.q_load, None)
        self.assertEqual(node_eval.p_load, None)
        self.assertEqual(node_eval.q_gen_max, None)
        self.assertEqual(node_eval.q_gen_min, None)
        self.assertEqual(node_eval.slc, None)
        self.assertEqual(node_eval.v_module, None)
        self.assertEqual(node_eval.v_rate, None)

    def test_node_id(self):
        node_eval = NodeEvaluator(node_id=1)
        self.assertEqual(node_eval.node_id, 1)
        node_eval.node_id = 1.0
        self.assertEqual(node_eval.node_id, None)

    def test_q_gen(self):
        node_eval = NodeEvaluator(q_gen=1)
        self.assertEqual(node_eval.q_gen, 1)
        node_eval.q_gen = 1.0
        self.assertEqual(node_eval.q_gen, 1.0)

    def test_p_gen(self):
        node_eval = NodeEvaluator(p_gen=1)
        self.assertEqual(node_eval.p_gen, 1)
        node_eval.p_gen = 1.0
        self.assertEqual(node_eval.p_gen, 1.0)

    def test_q_load(self):
        node_eval = NodeEvaluator(q_load=1)
        self.assertEqual(node_eval.q_load, 1)
        node_eval.q_load = 1.0
        self.assertEqual(node_eval.q_load, 1.0)

    def test_p_load(self):
        node_eval = NodeEvaluator(p_load=1)
        self.assertEqual(node_eval.p_load, 1)
        node_eval.p_load = 1.0
        self.assertEqual(node_eval.p_load, 1.0)

    def test_v_rate(self):
        node_eval = NodeEvaluator(v_rate=110)
        self.assertEqual(node_eval.v_rate, 110)
        node_eval.v_rate = 110.0
        self.assertEqual(node_eval.v_rate, 110.0)

    def test_v_module(self):
        node_eval = NodeEvaluator(v_module=115)
        self.assertEqual(node_eval.v_module, 115)
        node_eval.v_module = 115.36
        self.assertEqual(node_eval.v_module, 115.36)

    def test_slc(self):
        node_eval = NodeEvaluator(slc=1)
        self.assertEqual(node_eval.slc, 1)
        node_eval.slc = 6
        self.assertEqual(node_eval.slc, None)


if __name__ == '__main__':
    unittest.main()
