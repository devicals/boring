# v0.11.5@refactored
# Note: The goal here is to specifically avoid using built-in base conversions.
import os, sys, platform, string

ARGS = [a.lower() for a in sys.argv]
DEBUG = "--debug" in ARGS

FULL_CHARSET = string.digits + string.ascii_lowercase + string.ascii_uppercase + "+-"

class base:
    _char = [(i, FULL_CHARSET[:i]) for i in range(2, 65)]
    
    _map = [
        (b, {char: index for index, char in enumerate(chars)})
        for b, chars in _char
    ]
    _revmap = [
        (b, {index: char for index, char in enumerate(chars)})
        for b, chars in _char
    ]
    
    def convert(value = 0, b_in = 2, b_out = 10):
        # Setup
        b_in, b_out = int(b_in), int(b_out)
        
        __bin1 = []
        __bin2 = []
        output_decimal = 0
        
        original_value = value
        if b_in != 64:
            value = str(value).lower()
        else:
            value = str(value)
            
        if DEBUG:
            print(f"~ INPUT: {original_value}, FROM_BASE: {b_in}, TO_BASE: {b_out}")
        
        __ccbin1 = next((item for item in base._char if item[0] == b_in), None)
        if __ccbin1 is None:
            raise ValueError(f"Input base {b_in} is not supported.")
        
        __ccbin2 = next((item for item in base._char if item[0] == b_out), None)
        if __ccbin2 is None:
            raise ValueError(f"Output base {b_out} is not supported.")
        
        _current_char = __ccbin1[1]
        _allowed_char = list(_current_char) + [" "]
        
        if any(char not in _allowed_char for char in value):
            raise ValueError(f"Input '{value}' has illegal characters! Allowed for base {b_in}: {_allowed_char}.")
        
        value = value.replace(" ", "")
        
        # Conversion
        char_to_int_map = next((item for item in base._map if item[0] == b_in), None)[1]
        value_reversed = list(value)[::-1]
        
        if DEBUG:
            print(f"~ REVERSED INPUT LIST FOR CALCULATION: {value_reversed}")

        for char in value_reversed:
            ita = char_to_int_map[str(char)]
            __bin1.append(int(ita))
        
        if DEBUG:
            print(f"~ CONVERTING '{value}' (BASE {b_in}) TO DECIMAL")
            
        for i, v in enumerate(__bin1):
            term = int(v) * (b_in**int(i))
            current_total = output_decimal
            output_decimal += term
            if DEBUG:
                print(f"~ CALCULATION: current_total={current_total}, term={v} * {b_in}**{i} = {term}, new_total={output_decimal}")
        
        if DEBUG:
            print(f"~ FINAL DECIMAL SUM: {output_decimal}")
            
        if b_out == 10:
            if DEBUG:
                return value, b_in, b_out, __ccbin1, __ccbin2, _current_char, _allowed_char, ita, __bin1, __bin2, str(output_decimal)
            return str(output_decimal)
        
        if DEBUG:
            print(f"~ CONVERTING DECIMAL '{output_decimal}' TO BASE {b_out}")

        if output_decimal == 0:
            if DEBUG:
                print("~ INPUT IS ZERO, RETURNING '0'")
            zero_char = next((item for item in base._revmap if item[0] == b_out), None)[1][0]
            return zero_char

        index_to_char_map = next((item for item in base._revmap if item[0] == b_out), None)[1]

        q = output_decimal
        while q != 0:
            q, r = divmod(q, b_out)
            
            char_to_append = index_to_char_map[r]
            
            original_bin2 = list(__bin2)
            __bin2.append(char_to_append)
            if DEBUG:
                print(f"~ APPEND {char_to_append} TO __bin2 (from remainder {r}): Original: {original_bin2}, New: {__bin2}")
        
        output = "".join(__bin2[::-1])
        
        if DEBUG:
            print(f"~ FINAL RESULT STRING: {output}")
            return value, b_in, b_out, __ccbin1, __ccbin2, _current_char, _allowed_char, ita, __bin1, __bin2, str(output_decimal), str(output)
        return str(output)