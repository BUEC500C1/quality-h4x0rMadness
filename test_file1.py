def Int2Roman(num):
    if num == 0:
        return " "
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
            return table[base_num] + Int2Roman(num - base_num)
        else:
            if first_digit in [2, 3]:
                rep = ""
                for i in range(first_digit):
                    rep += table[pow(10, len_num - 1)]
                return rep + Int2Roman(num - base_num)
            elif first_digit in [6, 7, 8]:
                rep = table[5 * pow(10, len_num - 1)]
                for i in range(first_digit - 5):
                    rep += table[pow(10, len_num - 1)]
                return rep + Int2Roman(num - base_num)
            elif first_digit == 4:
                rep = table[pow(10, len_num - 1)] + table[5 * pow(10, len_num - 1)]
                return rep + Int2Roman(num - base_num)
            elif first_digit == 9:
                rep = table[pow(10, len_num - 1)] + table[pow(10, len_num)]
                return rep + Int2Roman(num - base_num)

def test_method():
    assert Int2Roman(1) == "I"
    assert Int2Roman(2) == "II"
    assert Int2Roman(3) == "III"
    assert Int2Roman(4) == "IV"
    assert Int2Roman(5) == "V"
    assert Int2Roman(6) == "VI"
    assert Int2Roman(7) == "VII"
    assert Int2Roman(8) == "VIII"
    assert Int2Roman(9) == "IX"
    assert Int2Roman(10) == "X"




