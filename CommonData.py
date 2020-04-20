from InputHelper import InputHelper

class CommonData:
    LIT_INDICATOR_VALID = ['BOB', 'CAR', 'CLR', 'FRK', 'FRQ', 'IND', 'MSA', 'NSA', 'SIG', 'SND', 'TRN']
    __instance = None

    @staticmethod 
    def get_instance():
        if CommonData.__instance == None:
            CommonData()
        return CommonData.__instance

    def __init__(self):
        if CommonData.__instance != None:
            raise Exception("This class is a singleton!")

        self._battery_read = False
        self._battery_aa = 0
        self._battery_d = 0

        self._lit_indicator_read = False
        self._lit_indicator = ""

        self._serial_number_read = False
        self._serial_number = ""

        CommonData.__instance = self

    def _read_battery_input(self):
        label = "Number AA batteries"
        self._battery_aa = InputHelper.read_int(label, InputHelper.NON_NEG)
        label = "Number D batteries"
        self._battery_d = InputHelper.read_int(label, InputHelper.NON_NEG)
        self._battery_read = True

    def get_battery_count(self):
        if not self._battery_read:
            self._read_battery_input()
        return self._battery_aa + self._battery_d

    def _read_lit_indicator_input(self):
        label = "3-letter Lit Indicator"
        self._lit_indicator = InputHelper.read_string(label, CommonData.LIT_INDICATOR_VALID)
        self._lit_indicator_read = True

    def get_lit_indicator(self):
        if not self._lit_indicator_read:
            self._read_lit_indicator_input()
        return self._lit_indicator

    def _read_serial_number_input(self):
        label = "Serial Number"
        self._serial_number = InputHelper.read_string(label)
        self._serial_number_read = True

    def get_serial_number(self):
        if not self._serial_number_read:
            self._read_serial_number_input()
        return self._serial_number
