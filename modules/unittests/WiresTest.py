import unittest
import itertools

from modules.Wires import WiresData, WiresRules3, WiresRules4, WiresRules5, WiresRules6

class WiresDataMock(WiresData):
    def __init__(self, wires, sn_odd):
        WiresData.__init__(self)
        self._wires = wires
        self._sn_odd = sn_odd

    def wires(self):
        return self._wires

    def sn_odd(self):
        return self._sn_odd

class WiresTest(unittest.TestCase):

    @classmethod
    def _build_t3_input(cls):
        combin_all = list(itertools.product(WiresData.VALID_COLORS, repeat=3))
        # Stage 1
        WiresTest._INPUT_T3_ST1 = [x for x in combin_all if x.count('R') == 0]
        # Stage 2
        combin_w_last = [x for x in combin_all if x[-1] == 'W']
        WiresTest._INPUT_T3_ST2 = list({*combin_w_last} - {*WiresTest._INPUT_T3_ST1})
        # Stage 3
        combin_plural_b = [x for x in combin_all if x.count('B') > 1]
        WiresTest._INPUT_T3_ST3 = list({*combin_plural_b} - {*WiresTest._INPUT_T3_ST1} - {*WiresTest._INPUT_T3_ST2})
        # Stage 4
        WiresTest._INPUT_T3_ST4 = list({*combin_all} - {*WiresTest._INPUT_T3_ST1} - {*WiresTest._INPUT_T3_ST2} - {*WiresTest._INPUT_T3_ST3})

    @classmethod
    def _build_t4_input(cls):
        combin_all = list(itertools.product(WiresData.VALID_COLORS, repeat=4))
        # Stage 1
        WiresTest._INPUT_T4_ST1_ODD = [x for x in combin_all if x.count('R') > 1]
        # Stage 2
        combin_y_last_no_r = [x for x in combin_all if x[-1] == 'Y' and x.count('R') == 0]
        WiresTest._INPUT_T4_ST2_EVEN = combin_y_last_no_r
        WiresTest._INPUT_T4_ST2_ODD = list({*combin_y_last_no_r} - {*WiresTest._INPUT_T4_ST1_ODD})
        # Stage 3
        combin_one_b = [x for x in combin_all if x.count('B') == 1]
        WiresTest._INPUT_T4_ST3_EVEN = list({*combin_one_b} - {*WiresTest._INPUT_T4_ST2_EVEN})
        WiresTest._INPUT_T4_ST3_ODD = list({*combin_one_b} - {*WiresTest._INPUT_T4_ST1_ODD} - {*WiresTest._INPUT_T4_ST2_ODD})
        # Stage 4
        combin_plural_y = [x for x in combin_all if x.count('Y') > 1]
        WiresTest._INPUT_T4_ST4_EVEN = list({*combin_plural_y} - {*WiresTest._INPUT_T4_ST2_EVEN} - {*WiresTest._INPUT_T4_ST3_EVEN})
        WiresTest._INPUT_T4_ST4_ODD = list({*combin_plural_y} - {*WiresTest._INPUT_T4_ST1_ODD} - {*WiresTest._INPUT_T4_ST2_ODD} - {*WiresTest._INPUT_T4_ST3_ODD})
        # Stage 5
        WiresTest._INPUT_T4_ST5_EVEN = list({*combin_all} - {*WiresTest._INPUT_T4_ST2_EVEN} - {*WiresTest._INPUT_T4_ST3_EVEN} - {*WiresTest._INPUT_T4_ST4_EVEN})
        WiresTest._INPUT_T4_ST5_ODD = list({*combin_all} - {*WiresTest._INPUT_T4_ST1_ODD} - {*WiresTest._INPUT_T4_ST2_ODD} - {*WiresTest._INPUT_T4_ST3_ODD} - {*WiresTest._INPUT_T4_ST4_ODD})

    @classmethod
    def _build_t5_input(cls):
        combin_all = list(itertools.product(WiresData.VALID_COLORS, repeat=5))
        # Stage 1
        WiresTest._INPUT_T5_ST1_ODD = [x for x in combin_all if x[-1] == 'K']
        # Stage 2
        combin_one_r_plural_y = [x for x in combin_all if x.count('R') == 1 and x.count('Y') > 1]
        WiresTest._INPUT_T5_ST2_EVEN = combin_one_r_plural_y
        WiresTest._INPUT_T5_ST2_ODD = list({*combin_one_r_plural_y} - {*WiresTest._INPUT_T5_ST1_ODD})
        # Stage 3
        combin_no_k = [x for x in combin_all if x.count('K') == 0]
        WiresTest._INPUT_T5_ST3_EVEN = list({*combin_no_k} - {*WiresTest._INPUT_T5_ST2_EVEN})
        WiresTest._INPUT_T5_ST3_ODD = list({*combin_no_k} - {*WiresTest._INPUT_T5_ST1_ODD} - {*WiresTest._INPUT_T5_ST2_ODD})
        # Stage 4
        WiresTest._INPUT_T5_ST4_EVEN = list({*combin_all} - {*WiresTest._INPUT_T5_ST2_EVEN} - {*WiresTest._INPUT_T5_ST3_EVEN})
        WiresTest._INPUT_T5_ST4_ODD = list({*combin_all} - {*WiresTest._INPUT_T5_ST1_ODD} - {*WiresTest._INPUT_T5_ST2_ODD} - {*WiresTest._INPUT_T5_ST3_ODD})

    @classmethod
    def _build_t6_input(cls):
        combin_all = list(itertools.product(WiresData.VALID_COLORS, repeat=6))
        # Stage 1
        WiresTest._INPUT_T6_ST1_ODD = [x for x in combin_all if x.count('Y') == 0]
        # Stage 2
        combin_one_y_plural_w = [x for x in combin_all if x.count('Y') == 1 and x.count('W') > 1]
        WiresTest._INPUT_T6_ST2_EVEN = combin_one_y_plural_w
        WiresTest._INPUT_T6_ST2_ODD = list({*combin_one_y_plural_w} - {*WiresTest._INPUT_T6_ST1_ODD})
        # Stage 3
        combin_no_r = [x for x in combin_all if x.count('R') == 0]
        WiresTest._INPUT_T6_ST3_EVEN = list({*combin_no_r} - {*WiresTest._INPUT_T6_ST2_EVEN})
        WiresTest._INPUT_T6_ST3_ODD = list({*combin_no_r} - {*WiresTest._INPUT_T6_ST1_ODD} - {*WiresTest._INPUT_T6_ST2_ODD})
        # Stage 4
        WiresTest._INPUT_T6_ST4_EVEN = list({*combin_all} - {*WiresTest._INPUT_T6_ST2_EVEN} - {*WiresTest._INPUT_T6_ST3_EVEN})
        WiresTest._INPUT_T6_ST4_ODD = list({*combin_all} - {*WiresTest._INPUT_T6_ST1_ODD} - {*WiresTest._INPUT_T6_ST2_ODD} - {*WiresTest._INPUT_T6_ST3_ODD})


    @classmethod
    def setUpClass(cls):
        unittest.TestCase.setUpClass()
        WiresTest._build_t3_input()
        WiresTest._build_t4_input()
        WiresTest._build_t5_input()
        WiresTest._build_t6_input()

    @staticmethod
    def _run_subtest(self, rules, exp, comb, sn_odd):
        with self.subTest(i=(comb,sn_odd)):
            comb_str = "".join(comb)
            self.assertEqual(rules.run(WiresDataMock(comb_str, sn_odd)), exp)

    def test3_stage1(self):
        exp = "Cut second wire"
        for comb in WiresTest._INPUT_T3_ST1:
            WiresTest._run_subtest(self, WiresRules3, exp, comb, sn_odd = True)
            WiresTest._run_subtest(self, WiresRules3, exp, comb, sn_odd = False)

    def test3_stage2(self):
        exp = "Cut the last wire"
        for comb in WiresTest._INPUT_T3_ST2:
            WiresTest._run_subtest(self, WiresRules3, exp, comb, sn_odd = True)
            WiresTest._run_subtest(self, WiresRules3, exp, comb, sn_odd = False)

    def test3_stage3(self):
        exp = "Cut the last blue wire"
        for comb in WiresTest._INPUT_T3_ST3:
            WiresTest._run_subtest(self, WiresRules3, exp, comb, sn_odd = True)
            WiresTest._run_subtest(self, WiresRules3, exp, comb, sn_odd = False)

    def test3_stage4(self):
        exp = "Cut the last wire"
        for comb in WiresTest._INPUT_T3_ST4:
            WiresTest._run_subtest(self, WiresRules3, exp, comb, sn_odd = True)
            WiresTest._run_subtest(self, WiresRules3, exp, comb, sn_odd = False)

    def test4_stage1(self):
        exp = "Cut last red wire"
        for comb in WiresTest._INPUT_T4_ST1_ODD:
            WiresTest._run_subtest(self, WiresRules4, exp, comb, sn_odd = True)

    def test4_stage2(self):
        exp = "Cut the first wire"
        for comb in WiresTest._INPUT_T4_ST2_ODD:
            WiresTest._run_subtest(self, WiresRules4, exp, comb, sn_odd = True)
        for comb in WiresTest._INPUT_T4_ST2_EVEN:
            WiresTest._run_subtest(self, WiresRules4, exp, comb, sn_odd = False)

    def test4_stage3(self):
        exp = "Cut the first wire"
        for comb in WiresTest._INPUT_T4_ST3_ODD:
            WiresTest._run_subtest(self, WiresRules4, exp, comb, sn_odd = True)
        for comb in WiresTest._INPUT_T4_ST3_EVEN:
            WiresTest._run_subtest(self, WiresRules4, exp, comb, sn_odd = False)

    def test4_stage4(self):
        exp = "Cut the last wire"
        for comb in WiresTest._INPUT_T4_ST4_ODD:
            WiresTest._run_subtest(self, WiresRules4, exp, comb, sn_odd = True)
        for comb in WiresTest._INPUT_T4_ST4_EVEN:
            WiresTest._run_subtest(self, WiresRules4, exp, comb, sn_odd = False)

    def test4_stage5(self):
        exp = "Cut the second wire"
        for comb in WiresTest._INPUT_T4_ST5_ODD:
            WiresTest._run_subtest(self, WiresRules4, exp, comb, sn_odd = True)
        for comb in WiresTest._INPUT_T4_ST5_EVEN:
            WiresTest._run_subtest(self, WiresRules4, exp, comb, sn_odd = False)

    def test5_stage1(self):
        exp = "Cut the fourth wire"
        for comb in WiresTest._INPUT_T5_ST1_ODD:
            WiresTest._run_subtest(self, WiresRules5, exp, comb, sn_odd = True)

    def test5_stage2(self):
        exp = "Cut the first wire"
        for comb in WiresTest._INPUT_T5_ST2_ODD:
            WiresTest._run_subtest(self, WiresRules5, exp, comb, sn_odd = True)
        for comb in WiresTest._INPUT_T5_ST2_EVEN:
            WiresTest._run_subtest(self, WiresRules5, exp, comb, sn_odd = False)

    def test5_stage3(self):
        exp = "Cut the second wire"
        for comb in WiresTest._INPUT_T5_ST3_ODD:
            WiresTest._run_subtest(self, WiresRules5, exp, comb, sn_odd = True)
        for comb in WiresTest._INPUT_T5_ST3_EVEN:
            WiresTest._run_subtest(self, WiresRules5, exp, comb, sn_odd = False)

    def test5_stage4(self):
        exp = "Cut the first wire"
        for comb in WiresTest._INPUT_T5_ST4_ODD:
            WiresTest._run_subtest(self, WiresRules5, exp, comb, sn_odd = True)
        for comb in WiresTest._INPUT_T5_ST4_EVEN:
            WiresTest._run_subtest(self, WiresRules5, exp, comb, sn_odd = False)

    def test6_stage1(self):
        exp = "Cut the third wire"
        for comb in WiresTest._INPUT_T6_ST1_ODD:
            WiresTest._run_subtest(self, WiresRules6, exp, comb, sn_odd = True)

    def test6_stage2(self):
        exp = "Cut the fourth wire"
        for comb in WiresTest._INPUT_T6_ST2_ODD:
            WiresTest._run_subtest(self, WiresRules6, exp, comb, sn_odd = True)
        for comb in WiresTest._INPUT_T6_ST2_EVEN:
            WiresTest._run_subtest(self, WiresRules6, exp, comb, sn_odd = False)

    def test6_stage3(self):
        exp = "Cut the last wire"
        for comb in WiresTest._INPUT_T6_ST3_ODD:
            WiresTest._run_subtest(self, WiresRules6, exp, comb, sn_odd = True)
        for comb in WiresTest._INPUT_T6_ST3_EVEN:
            WiresTest._run_subtest(self, WiresRules6, exp, comb, sn_odd = False)

    def test6_stage4(self):
        exp = "Cut the fourth wire"
        for comb in WiresTest._INPUT_T6_ST4_ODD:
            WiresTest._run_subtest(self, WiresRules6, exp, comb, sn_odd = True)
        for comb in WiresTest._INPUT_T6_ST4_EVEN:
            WiresTest._run_subtest(self, WiresRules6, exp, comb, sn_odd = False)


if __name__ == '__main__':
    unittest.main()
