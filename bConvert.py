# v0.11.4@final
# Note: The goal here is to specifically avoid using built-in base conversions.
import os, sys, platform

ARGS = [a.lower() for a in sys.argv]
DEBUG = "--debug" in ARGS

class base:
    class binary:
        _char = " 01"

        @staticmethod
        def convert(input, to_base = "10"):
            input = str(input).lower()

            if any(char not in b2._char for char in input):
                raise ValueError(f"Input is not in binary. Allowed: [{', '.join(['<space>' if c == ' ' else c for c in b2._char])}].")

            if DEBUG:
                print(f"~ INPUT: {input}, TARGET BASE: {to_base}")

            match str(to_base):
                case "8":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b2.convert(input, 10)}, 8)")
                    return b10.convert(b2.convert(input, 10), 8)

                case "10":
                    if DEBUG:
                        print(f"~ CONVERTING '{input}' TO DECIMAL (BASE 10)")
                    original_input_str = input.replace(" ", "")
                    _bin_1 = list(map(int, original_input_str))
                    _bin_1 = _bin_1[::-1]
                    if DEBUG:
                        print(f"~ REVERSED BINARY LIST FOR CALCULATION: {_bin_1}")

                    _bin_2 = []
                    for i, v in enumerate(_bin_1):
                        item_to_append = int(v * 2**i)
                        _bin_2.append(item_to_append)
                        if DEBUG:
                            print(f"~ APPEND {item_to_append} TO _bin_2 (from index {i}, value {v}): Original: {_bin_2[:-1]}, New: {_bin_2}")

                    final_sum = sum(_bin_2)
                    if DEBUG:
                        print(f"~ FINAL DECIMAL SUM: {final_sum}")
                    return str(final_sum)

                case "16":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b2.convert(input, 10)}, 16)")
                    return b10.convert(b2.convert(input, 10), 16)

                case "32":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b2.convert(input, 10)}, 32)")
                    return b10.convert(b2.convert(input, 10), 32)

                case "64":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b2.convert(input, 10)}, 64)")
                    return b10.convert(b2.convert(input, 10), 64)

    class octal:
        _char = " 01234567"

        @staticmethod
        def convert(input, to_base = "10"):
            input = str(input).lower()

            if any(char not in b8._char for char in input):
                raise ValueError(f"Input is not in octal. Allowed: [{', '.join(['<space>' if c == ' ' else c for c in b8._char])}].")

            if DEBUG:
                print(f"~ INPUT: {input}, TARGET BASE: {to_base}")

            match str(to_base):
                case "2":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b8.convert(input, 10)}, 2)")
                    return b10.convert(b8.convert(input, 10), 2)

                case "10":
                    if DEBUG:
                        print(f"~ CONVERTING '{input}' TO DECIMAL (BASE 10)")
                    original_input_str = input.replace(" ", "")
                    _bin_1 = list(map(int, original_input_str))
                    _bin_1 = _bin_1[::-1]
                    if DEBUG:
                        print(f"~ REVERSED OCTAL LIST FOR CALCULATION: {_bin_1}")

                    _bin_2 = []
                    for i, v in enumerate(_bin_1):
                        item_to_append = int(v * 8**i)
                        _bin_2.append(item_to_append)
                        if DEBUG:
                            print(f"~ APPEND {item_to_append} TO _bin_2 (from index {i}, value {v}): Original: {_bin_2[:-1]}, New: {_bin_2}")

                    final_sum = sum(_bin_2)
                    if DEBUG:
                        print(f"~ FINAL DECIMAL SUM: {final_sum}")
                    return str(final_sum)

                case "16":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b8.convert(input, 10)}, 16)")
                    return b10.convert(b8.convert(input, 10), 16)

                case "32":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b8.convert(input, 10)}, 32)")
                    return b10.convert(b8.convert(input, 10), 32)

                case "64":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b8.convert(input, 10)}, 64)")
                    return b10.convert(b8.convert(input, 10), 64)

    class decimal:
        _char = " 0123456789"

        @staticmethod
        def convert(input, to_base = "2"):
            input = str(input).lower()

            if any(char not in b10._char for char in input):
                raise ValueError(f"Input is not in decimal. Allowed: [{', '.join(['<space>' if c == ' ' else c for c in b10._char])}].")

            if DEBUG:
                print(f"~ CONVERTING DECIMAL '{input}' TO BASE {to_base}")

            q = int(input)
            if q == 0:
                if DEBUG:
                    print("~ INPUT IS ZERO, RETURNING '0'")
                return "0"

            _result_list = []
            target_base_int = int(to_base)

            while q != 0:
                q, r = divmod(q, target_base_int)

                char_to_append = r
                if target_base_int in [16, 32, 64]:
                    base_name = {16: 'hexadecimal', 32: 'duotrigesimal', 64: 'tetrasexagesima'}[target_base_int]
                    if r not in getattr(base, base_name)._revmap:
                        raise ValueError(f"Internal Error: Remainder {r} not found in base {target_base_int} map for {base_name}.")
                    char_to_append = getattr(base, base_name)._revmap[r]

                _result_list.append(char_to_append)
                if DEBUG:
                    print(f"~ APPEND {char_to_append} TO _result_list (from remainder {r}): Original: {_result_list[:-1]}, New: {_result_list}")

            final_str = "".join(map(str, _result_list[::-1]))
            if DEBUG:
                print(f"~ FINAL RESULT STRING: {final_str}")
            return final_str

    class hexadecimal:
        _char = " 0123456789abcdef"
        _map = {v: i for i, v in enumerate(_char.strip())}
        _revmap = {v: i for i, v in _map.items()}

        @staticmethod
        def convert(input, to_base = "10"):
            input = str(input).lower()

            if any(char not in b16._char for char in input):
                raise ValueError(f"Input is not in hexadecimal. Allowed: [{', '.join(['<space>' if c == ' ' else c for c in b16._char])}].")

            if DEBUG:
                print(f"~ INPUT: {input}, TARGET BASE: {to_base}")

            match str(to_base):
                case "2":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b16.convert(input, 10)}, 2)")
                    return b10.convert(b16.convert(input, 10), 2)

                case "8":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b16.convert(input, 10)}, 8)")
                    return b10.convert(b16.convert(input, 10), 8)

                case "10":
                    if DEBUG:
                        print(f"~ CONVERTING '{input}' TO DECIMAL (BASE 10)")
                    original_input_str = input.replace(" ", "")
                    _bin_1 = list(original_input_str[::-1])
                    if DEBUG:
                        print(f"~ REVERSED HEX LIST FOR CALCULATION: {_bin_1}")

                    _bin_2 = []
                    for i, v in enumerate(_bin_1):
                        item_to_append = int(b16._map[v.lower()] * 16**i)
                        _bin_2.append(item_to_append)
                        if DEBUG:
                            print(f"~ APPEND {item_to_append} TO _bin_2 (from index {i}, value {v}): Original: {_bin_2[:-1]}, New: {_bin_2}")

                    final_sum = sum(_bin_2)
                    if DEBUG:
                        print(f"~ FINAL DECIMAL SUM: {final_sum}")
                    return str(final_sum)

                case "32":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b16.convert(input, 10)}, 32)")
                    return b10.convert(b16.convert(input, 10), 32)

                case "64":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b16.convert(input, 10)}, 64)")
                    return b10.convert(b16.convert(input, 10), 64)

    class duotrigesimal:
        _char = " 0123456789abcdefghijklmnopqrstuv"
        _map = {v: i for i, v in enumerate(_char.strip())}
        _revmap = {v: i for i, v in _map.items()}

        @staticmethod
        def convert(input, to_base = "10"):
            input = str(input).lower()

            if any(char not in b32._char for char in input):
                raise ValueError(f"Input is not in duotrigesimal. Allowed: [{', '.join(['<space>' if c == ' ' else c for c in b32._char])}].")

            if DEBUG:
                print(f"~ INPUT: {input}, TARGET BASE: {to_base}")

            match str(to_base):
                case "2":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b32.convert(input, 10)}, 2)")
                    return b10.convert(b32.convert(input, 10), 2)

                case "8":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b32.convert(input, 10)}, 8)")
                    return b10.convert(b32.convert(input, 10), 8)

                case "10":
                    if DEBUG:
                        print(f"~ CONVERTING '{input}' TO DECIMAL (BASE 10)")
                    original_input_str = input.replace(" ", "")
                    _bin_1 = list(original_input_str[::-1])
                    if DEBUG:
                        print(f"~ REVERSED DUOTRIGESIMAL LIST FOR CALCULATION: {_bin_1}")

                    _bin_2 = []
                    for i, v in enumerate(_bin_1):
                        item_to_append = int(b32._map[v.lower()] * 32**i)
                        _bin_2.append(item_to_append)
                        if DEBUG:
                            print(f"~ APPEND {item_to_append} TO _bin_2 (from index {i}, value {v}): Original: {_bin_2[:-1]}, New: {_bin_2}")

                    final_sum = sum(_bin_2)
                    if DEBUG:
                        print(f"~ FINAL DECIMAL SUM: {final_sum}")
                    return str(final_sum)

                case "16":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b32.convert(input, 10)}, 16)")
                    return b10.convert(b32.convert(input, 10), 16)

                case "64":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b32.convert(input, 10)}, 64)")
                    return b10.convert(b32.convert(input, 10), 64)

    class tetrasexagesima:
        _char = " 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+-"
        _map = {v: i for i, v in enumerate(_char.strip())}
        _revmap = {v: i for i, v in _map.items()}

        @staticmethod
        def convert(input, to_base = "10"):
            input = str(input)

            if any(char not in b64._char for char in input):
                raise ValueError(f"Input is not in tetrasexagesima. Allowed: [{', '.join(['<space>' if c == ' ' else c for c in b64._char])}].")

            if DEBUG:
                print(f"~ INPUT: {input}, TARGET BASE: {to_base}")

            match str(to_base):
                case "2":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b64.convert(input, 10)}, 2)")
                    return b10.convert(b64.convert(input, 10), 2)

                case "8":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b64.convert(input, 10)}, 8)")
                    return b10.convert(b64.convert(input, 10), 8)

                case "10":
                    if DEBUG:
                        print(f"~ CONVERTING '{input}' TO DECIMAL (BASE 10)")
                    original_input_str = input.replace(" ", "")
                    _bin_1 = list(original_input_str[::-1])
                    if DEBUG:
                        print(f"~ REVERSED TETRASEXAGESIMAL LIST FOR CALCULATION: {_bin_1}")

                    _bin_2 = []
                    for i, v in enumerate(_bin_1):
                        item_to_append = int(b64._map[v] * 64**i)
                        _bin_2.append(item_to_append)
                        if DEBUG:
                            print(f"~ APPEND {item_to_append} TO _bin_2 (from index {i}, value {v}): Original: {_bin_2[:-1]}, New: {_bin_2}")

                    final_sum = sum(_bin_2)
                    if DEBUG:
                        print(f"~ FINAL DECIMAL SUM: {final_sum}")
                    return str(final_sum)

                case "16":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b64.convert(input, 10)}, 16)")
                    return b10.convert(b64.convert(input, 10), 16)

                case "32":
                    if DEBUG:
                        print(f"~ CALLING: b10.convert({b64.convert(input, 10)}, 32)")
                    return b10.convert(b64.convert(input, 10), 32)

    if DEBUG:
        @staticmethod
        def run_tests():
            test_values = {
                "2":  "10011010010",
                "8":  "2322",
                "10": "1234",
                "16": "4d2",
                "32": "16i",
                "64": "JI"
            }

            classes = {
                "2": b2,
                "8": b8,
                "10": b10,
                "16": b16,
                "32": b32,
                "64": b64
            }

            for from_base, class_obj in classes.items():
                input_val = test_values[from_base]

                for to_base in test_values.keys():
                    if from_base == to_base:
                        continue

                    expected = test_values[to_base]

                    try:
                        result = class_obj.convert(input_val, to_base)

                        if str(result) != str(expected):
                            print(f"~ TEST FAILED: {from_base} -> {to_base} | Input: {input_val}, Expected: {expected}, Got: {result}")
                            return False
                        else:
                            if DEBUG:
                                print(f"~ TEST PASSED: {from_base} -> {to_base} | Input: {input_val}, Expected: {expected}, Got: {result}")

                    except Exception as e:
                        print(f"~ TEST FAILED WITH EXCEPTION: {from_base} -> {to_base} | Input: {input_val}, Error: {e}")
                        return False

            print("~ All tests passed!")
            return True

# Shortcuts
b2 = base.binary
b8 = base.octal
b10 = base.decimal
b16 = base.hexadecimal
b32 = base.duotrigesimal
b64 = base.tetrasexagesima