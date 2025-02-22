from physics_calculator import convert_digit_to_float, time_converter
from pytest import approx
import pytest

def test_convert_digit_to_float():
    assert convert_digit_to_float("0.0") == approx(0.0, abs = 0.001)
    assert convert_digit_to_float("3") == approx(3.0, abs = 0.001)
    assert convert_digit_to_float("3.2") == approx(3.20, abs = 0.001)
    assert convert_digit_to_float("g") == approx(9.8066500, abs = 0.001)
    assert convert_digit_to_float("G") == approx(9.8066500, abs = 0.001)
    assert convert_digit_to_float("?") == "?"
    assert convert_digit_to_float("l") == "l"
    assert convert_digit_to_float("M") == "M"

def test_time_converter():
    assert time_converter(3.0, "s") == approx(3.0, abs = 0.001)
    assert time_converter(4, "s") == approx(4, abs = 0.001)
    assert time_converter(7.0, "ms") == approx(0.007, abs = 0.001)
    assert time_converter(3.6, "s") == approx(3.6, abs = 0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])    
