from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("123 Main Street, Anywhere, UT 67890") == "Anywhere"
    assert extract_city("1345 S Rain Ct, West Anyplace, New York 40278") == "West Anyplace"

def test_extract_state():
    assert extract_state("123 Main Street, Anywhere, UT 67890") == "UT"
    assert extract_state("1345 S Rain Ct, West Anyplace, New York 40278") == "New York"
    assert extract_state("10096 Center Street, Wherever, California 97842") == "California"

def test_extract_zipcode():
    assert extract_zipcode("123 Main Street, Anywhere, UT 67890") == "67890"
    assert extract_zipcode("1345 S Rain Ct, West Anyplace, New York 40278") == "40278"
    assert extract_zipcode("10096 Center Street, Wherever, California 97842") == "97842"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
