import unittest

from GSCore.node.node_info import NodeInfo


class NodeInfoGenericTest(unittest.TestCase):
    def test_equals_1(self):
        node_info_1 = NodeInfo()
        node_info_2 = NodeInfo()
        self.assertEqual(node_info_1, node_info_2)

    def test_equals_2(self):
        node_info_1 = NodeInfo("FullName", "Node", "DispatchName", 0.9, "None")
        node_info_2 = NodeInfo("FullName", "Node", "DispatchName", 0.9, "None")
        self.assertEqual(node_info_1, node_info_2)

    def test_equals_3(self):
        node_info_1 = NodeInfo("FullName", "Node", "DispatchName", 0.9, "None")
        node_info_2 = NodeInfo("FullName", "Node", "DisptchName", 0.9, "None")
        self.assertNotEqual(node_info_1, node_info_2)


class NodeInfoPropsTest(unittest.TestCase):
    def test_default(self):
        node_info = NodeInfo()
        self.assertEqual(node_info.power_factor, None)
        self.assertEqual(node_info.full_name, "")
        self.assertEqual(node_info.disp_name, "")
        self.assertEqual(node_info.net_type, "")
        self.assertEqual(node_info.notation, "")

    def test_power_factor(self):
        node_info = NodeInfo(power_factor=0.9)
        self.assertEqual(node_info.power_factor, 0.9)
        node_info.power_factor = 1
        self.assertEqual(node_info.power_factor, None)

    def test_full_name(self):
        node_info = NodeInfo(full_name="0.9")
        self.assertEqual(node_info.full_name, "0.9")
        node_info.full_name = 1
        self.assertEqual(node_info.full_name, "")

    def test_disp_name(self):
        node_info = NodeInfo(disp_name="0.9")
        self.assertEqual(node_info.disp_name, "0.9")
        node_info.disp_name = 1
        self.assertEqual(node_info.disp_name, "")

    def test_net_type(self):
        node_info = NodeInfo(net_type="0.9")
        self.assertEqual(node_info.net_type, "0.9")
        node_info.net_type = 1
        self.assertEqual(node_info.net_type, "")

    def test_notation(self):
        node_info = NodeInfo(notation="0.9")
        self.assertEqual(node_info.notation, "0.9")
        node_info.notation = 1
        self.assertEqual(node_info.notation, "")


if __name__ == '__main__':
    unittest.main()
