import unittest

from GSCore.branch.branch_info import BranchInfo


class BranchInfoGenericTest(unittest.TestCase):
    def test_equals_1(self):
        branch_info_1 = BranchInfo()
        branch_info_2 = BranchInfo()
        self.assertEqual(branch_info_1, branch_info_2)

    def test_equals_1(self):
        branch_info_1 = BranchInfo("Full_name", "disp", "AC-240",
                                   110, 42, 650, 650, 1000, 1, 0.5, 1.78, 19)
        branch_info_2 = BranchInfo("Full_name", "disp", "AC-240",
                                   110, 42, 650, 650, 1000, 1, 0.5, 1.78, 19)
        self.assertEqual(branch_info_1, branch_info_2)

    def test_equals_3(self):
        branch_info_1 = BranchInfo("Full_name", "disp", "AC-240",
                                   110, 42, 650, 650, 1000, 1, 0.5, 1.78, 19)
        branch_info_2 = BranchInfo("Full_name", "disp", "AC-240",
                                   110, 41.99, 650, 650, 1000, 1, 0.5, 1.78, 19)
        self.assertNotEqual(branch_info_1, branch_info_2)


class BranchInfoPropsTest(unittest.TestCase):
    def test_default(self):
        branch_info = BranchInfo()
        self.assertEqual(branch_info.full_name, "")
        self.assertEqual(branch_info.wire_type, "")
        self.assertEqual(branch_info.rate_tc, None)
        self.assertEqual(branch_info.v_rate, None)
        self.assertEqual(branch_info.disp_name, "")
        self.assertEqual(branch_info.current_tc, None)
        self.assertEqual(branch_info.i_fault, None)
        self.assertEqual(branch_info.i_heat, None)
        self.assertEqual(branch_info.length, None)
        self.assertEqual(branch_info.olt_step, None)
        self.assertEqual(branch_info.s_rate, None)
        self.assertEqual(branch_info.steps_num, None)

    def test_full_name(self):
        branch_info = BranchInfo(full_name="0.9")
        self.assertEqual(branch_info.full_name, "0.9")
        branch_info.full_name = 1
        self.assertEqual(branch_info.full_name, "")

    def test_disp_name(self):
        branch_info = BranchInfo(disp_name="0.9")
        self.assertEqual(branch_info.disp_name, "0.9")
        branch_info.disp_name = 1
        self.assertEqual(branch_info.disp_name, "")

    def test_wire_type(self):
        branch_info = BranchInfo(wire_type="0.9")
        self.assertEqual(branch_info.wire_type, "0.9")
        branch_info.wire_type = 1
        self.assertEqual(branch_info.wire_type, "")

    def test_olt_series(self):
        branch_info = BranchInfo(rate_tc=110/220, olt_step=1, steps_num=5)
        self.assertEqual(branch_info.olt_series, ".52,.51,.5,.49,.48")

    def test_rate_tc(self):
        branch_info = BranchInfo(rate_tc=1)
        self.assertEqual(branch_info.rate_tc, 1)
        branch_info.rate_tc = 0.5
        self.assertEqual(branch_info.rate_tc, 0.5)

    def test_v_rate(self):
        branch_info = BranchInfo(v_rate=110)
        self.assertEqual(branch_info.v_rate, 110)
        branch_info.v_rate = 10.5
        self.assertEqual(branch_info.v_rate, 10.5)

    def test_current_tc(self):
        branch_info = BranchInfo(current_tc=110)
        self.assertEqual(branch_info.current_tc, 110)
        branch_info.current_tc = 0.5
        self.assertEqual(branch_info.current_tc, 0.5)

    def test_i_fault(self):
        branch_info = BranchInfo(fault_limit_current=110)
        self.assertEqual(branch_info.i_fault, 110)
        branch_info.i_fault = 110.05
        self.assertEqual(branch_info.i_fault, 110.05)

    def test_i_heat(self):
        branch_info = BranchInfo(heating_limit_current=110)
        self.assertEqual(branch_info.i_heat, 110)
        branch_info.i_heat = 110.05
        self.assertEqual(branch_info.i_heat, 110.05)

    def test_length(self):
        branch_info = BranchInfo(length=110)
        self.assertEqual(branch_info.length, 110)
        branch_info.length = 110.05
        self.assertEqual(branch_info.length, 110.05)

    def test_olt_step(self):
        branch_info = BranchInfo(olt_step=1.78)
        self.assertEqual(branch_info.olt_step, 0.0178)
        branch_info.olt_step = 1.78
        self.assertEqual(branch_info.olt_step, 0.0178)

    def test_s_rate(self):
        branch_info = BranchInfo(s_rate=110)
        self.assertEqual(branch_info.s_rate, 110)
        branch_info.s_rate = 110.05
        self.assertEqual(branch_info.s_rate, 110.05)

    def test_steps_num(self):
        branch_info = BranchInfo(steps_num=19)
        self.assertEqual(branch_info.steps_num, 19)
        try:
            branch_info.steps_num = 5.5
        except ValueError:
            self.assertEqual(True)


if __name__ == '__main__':
    unittest.main()
