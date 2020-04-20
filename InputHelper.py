import string

class InputHelper:
    NON_NEG = 1

    @staticmethod
    def read_int(label, valid = None):
        val = int(input(label + ": "))
        while valid == InputHelper.NON_NEG and val < 0:
            print("[Error] Input must be >=0")
            val = int(input(label + ": "))
        return val

    @staticmethod
    def read_string(label, valid_strs = None):
        val = input(label + ": ").upper()
        while valid_strs and val not in valid_strs:
            print("[Error] Must be in " + " ".join(valid_strs))
            val = input(label + ": ").upper()
        return val

    @staticmethod
    def _to_char_list(s):
        return list(s.upper().translate({ord(c): None for c in string.whitespace}))

    @staticmethod
    def read_char_array(label, valid_chars = None):
        val = InputHelper._to_char_list(input(label + ": "))
        while valid_chars and len([i for i in val if i not in valid_chars]) > 0:
            print("[E] Must be in " + " ".join(valid_chars))
            val = InputHelper._to_char_list(input(label + ": "))
        return val
