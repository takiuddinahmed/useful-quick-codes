from password_validator.password_validator import PasswordValidator

def test_validate_password_length():
    validator = PasswordValidator()
    assert validator.validate_password_length("password", 8, 12) == True
    assert validator.validate_password_length("pass", 8, 12) == False
    assert validator.validate_password_length("passwordpassword", 8, 12) == False
    assert validator.validate_password_length("", 8, 12) == False
    assert validator.validate_password_length("passwordpasswordpassword", 8, 12) == False
    assert validator.validate_password_length("passwordpasswordpasswordpassword", 8, 12) == False


def test_validate_sequential_character_limit():
    validator = PasswordValidator()

    assert validator.validate_sequential_character_limit("abcd1234", 4) == True
    assert validator.validate_sequential_character_limit("abcd1234", 3) == False
    assert validator.validate_sequential_character_limit("abc123", 2) == False
    assert validator.validate_sequential_character_limit("", 3) == True
    assert validator.validate_sequential_character_limit("abcd", 0) == True
    assert validator.validate_sequential_character_limit("abcd", 1) == False
    assert validator.validate_sequential_character_limit("abcd1234", 0) == True

def test_validate_allowed_special_characters():
    validator = PasswordValidator()
    assert validator.validate_allowed_special_characters("password", "!@#$%") == False
    assert validator.validate_allowed_special_characters("pass!@#$word", "!@#$%") == True
    assert validator.validate_allowed_special_characters("", "!@#$%") == True
    assert validator.validate_allowed_special_characters("password", "") == False
    assert validator.validate_allowed_special_characters("", "") == True


def test_validate_allowed_special_characters():
    validator = PasswordValidator()
    assert validator.validate_allowed_special_characters("abc!12#3$", "!@#$%") == True
    assert validator.validate_allowed_special_characters("abc&123", "!@#$%") == False
    assert validator.validate_allowed_special_characters("abc123", "") == True
    assert validator.validate_allowed_special_characters("", "!@#$%") == True
    assert validator.validate_allowed_special_characters("", "") == True
    