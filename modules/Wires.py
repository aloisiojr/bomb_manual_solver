from InputHelper import InputHelper
from CommonData import CommonData

class WiresData:
    VALID_COLORS = ['B', 'G', 'K', 'R', 'W', 'Y']

    def __init__(self):
        self._wires_read = False
        self._wires = []

    def _read_wires_input(self):
        label = "Wire colors (Black is K)"
        self._wires = InputHelper.read_char_array(label, WiresData.VALID_COLORS)
        while len(self._wires) < 3 or len(self._wires) > 6:
            print("[Error] Must have >= 3 and <= 6 wires!")
            self._wires = InputHelper.read_char_list(label, WiresData.VALID_COLORS)
        self._wires_read = True

    def wires(self):
        if not self._wires_read:
            self._read_wires_input()
        return self._wires

    def sn_odd(self):
        cd = CommonData.get_instance()
        return int(cd.get_serial_number()[-1]) % 2 == 1


class WiresRules:
    RULES = []

    @classmethod
    def run(cls, data):
        for test in cls.RULES:
            result = test(data)
            if result:
                return result


class WiresRules3(WiresRules):
    RULES = [
        (lambda d: 'R' not in d.wires() and "Cut second wire"),
        (lambda d: d.wires()[-1] == 'W' and "Cut the last wire"),
        (lambda d: d.wires().count('B') > 1 and "Cut the last blue wire"),
        (lambda d: "Cut the last wire"),
    ]
   
class WiresRules4(WiresRules):
    RULES = [
        (lambda d: d.wires().count('R') > 1 and d.sn_odd() and "Cut last red wire"),
        (lambda d: d.wires()[-1] == 'Y' and d.wires().count('R') == 0 and "Cut the first wire"),
        (lambda d: d.wires().count('B') == 1 and "Cut the first wire"),
        (lambda d: d.wires().count('Y') > 1 and "Cut the last wire"),
        (lambda d: "Cut the second wire"),
    ]

class WiresRules5(WiresRules):
    RULES = [
        (lambda d: d.wires()[-1] == 'K' and d.sn_odd() and "Cut the fourth wire"),
        (lambda d: d.wires().count('R') == 1 and d.wires().count('Y') > 1 and "Cut the first wire"),
        (lambda d: d.wires().count('K') == 0 and "Cut the second wire"),
        (lambda d: "Cut the first wire"),
    ]

class WiresRules6(WiresRules):
    RULES = [
        (lambda d: d.wires().count('Y') == 0 and d.sn_odd() and "Cut the third wire"),
        (lambda d: d.wires().count('Y') == 1 and d.wires().count('W') > 1 and "Cut the fourth wire"),
        (lambda d: d.wires().count('R') == 0 and "Cut the last wire"),
        (lambda d: "Cut the fourth wire"),
    ]


class Wires:
    def __init__(self):
        self._data = WiresData()

    def run(self):
        count = len(self._data.wires())

        if count == 3:
            advice = WiresRules3.run(self._data)
        elif count == 4:
            advice = WiresRules4.run(self._data)
        elif count == 5:
            advice = WiresRules5.run(self._data)
        else:
            advice = WiresRules6.run(self._data)

        print("[ADVICE] " + advice)
