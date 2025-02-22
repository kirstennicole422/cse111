from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("John", "Doe") == "Doe; John"
    assert make_full_name("Mary-Anna", "Smith") == "Smith; Mary-Anna"
    assert make_full_name("Alexandraisalonglongname", "Brown") == "Brown; Alexandraisalonglongname"
    assert make_full_name("Sallie Mae", "Johnson") == "Johnson; Sallie Mae"

def test_extract_family_name():
    assert extract_family_name("Doe; John") == "Doe"
    assert extract_family_name("Smith; Mary-Anna") == "Smith"
    assert extract_family_name("Brown; Alexandraisalonglongname") == "Brown"
    assert extract_family_name("Johnson; Sallie Mae") == "Johnson"

def test_extract_given_name():
    assert extract_given_name("Doe; John") == "John"
    assert extract_given_name("Smith; Mary-Anna") == "Mary-Anna"
    assert extract_given_name("Brown; Alexandraisalonglongname") == "Alexandraisalonglongname"
    assert extract_given_name("Johnson; Sallie Mae") == "Sallie Mae"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])