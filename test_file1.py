def int2roman(num):
    # INPUT : ints between 1 - 3999, float, char, string not applicable
    if not isinstance(num, int):
        return ""
    if num < 1 or num > 3999:
        return ""
    table = {}
    nums = [1, 5, 10, 50, 100, 500, 1000]
    chars = ["I", "V", "X", "L", "C", "D", "M"]
    for i in range(len(nums)):
        table[nums[i]] = chars[i]

    if num in table:
        return table[num]
    else:
        first_digit = int(str(num)[0])
        len_num = len(str(num))
        base_num = first_digit * pow(10, len_num - 1)
        if base_num in table:
            return table[base_num] + int2roman(num - base_num)
        else:
            if first_digit in [2, 3]:
                rep = ""
                for i in range(first_digit):
                    rep += table[pow(10, len_num - 1)]
                return rep + int2roman(num - base_num)
            elif first_digit in [6, 7, 8]:
                rep = table[5 * pow(10, len_num - 1)]
                for i in range(first_digit - 5):
                    rep += table[pow(10, len_num - 1)]
                return rep + int2roman(num - base_num)
            elif first_digit == 4:
                rep = table[pow(10, len_num - 1)] + table[5 * pow(10, len_num - 1)]
                return rep + int2roman(num - base_num)
            elif first_digit == 9:
                rep = table[pow(10, len_num - 1)] + table[pow(10, len_num)]
                return rep + int2roman(num - base_num)

def test_method():
    assert int2roman(0) == ""
    assert int2roman(-99) == ""
    assert int2roman(4000) == ""
    assert int2roman(9.9999) == ""
    assert int2roman('c') == ""
    assert int2roman(1) == "I"
    assert int2roman(2) == "II"
    assert int2roman(3) == "III"
    assert int2roman(4) == "IV"
    assert int2roman(5) == "V"
    assert int2roman(6) == "VI"
    assert int2roman(7) == "VII"
    assert int2roman(8) == "VIII"
    assert int2roman(9) == "IX"
    assert int2roman(10) == "X"


