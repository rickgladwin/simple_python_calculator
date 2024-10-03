import pytest

import calculator.utils as util


class TestStringToNumber:
    def test_converts_positive_intlike_to_int(self):
        test_input: str = '23'
        expected: int = 23

        result = util.string_to_number(test_input)

        assert result == expected


    def test_converts_negative_intlike_to_int(self):
        test_input: str = '-12'
        expected: int = -12

        result = util.string_to_number(test_input)

        assert result == expected


    def test_converts_positive_floatlike_to_float(self):
        test_input: str = '3.127'
        expected: float = 3.127

        result = util.string_to_number(test_input)

        assert result == expected


    def test_converts_negative_floatlike_to_float(self):
        test_input: str = '-4789234.28'
        expected: float = -4789234.28

        result = util.string_to_number(test_input)

        assert result == expected


    def test_raises_value_error_given_input_letters(self):
        test_input: str = '0x2233'
        with pytest.raises(ValueError):
            util.string_to_number(test_input)
