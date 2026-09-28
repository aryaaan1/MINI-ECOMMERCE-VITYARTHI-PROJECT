from validation import validate_name, validate_phone, validate_address

def test_name():
    assert validate_name("Aryan") == True
    assert validate_name("12345") == False

def test_phone():
    assert validate_phone("9876543210") == True
    assert validate_phone("12345") == False

def test_address():
    assert validate_address("VIT Bhopal") == True
    assert validate_address("") == False