class PasswordValidator():

    def validate_password_length(self, password: str, min_length: int, max_length: int) -> bool:
        """
        Validate password length
        """

        return min_length <= len(password) <= max_length

    def validate_sequential_character_limit(self, password: str, limit: int) -> bool:
        """
        Validate sequential character limit
        """
        if limit == 0:
            return True
        sequence_count = 0
        prev_char = chr(0)
        for char in password:
            
            if char.isalnum() and (ord(char) == ord(prev_char) + 1 or ord(char) == ord(prev_char)):
                if sequence_count == 0:
                    sequence_count = 2
                else:
                    sequence_count += 1

                if sequence_count > limit:
                    return False
            else:
                sequence_count = 0

            prev_char = char

        return True

    def validate_allowed_special_characters(self, password: str, allowed_special_characters: str) -> bool:
        """
        Validate allowed special characters
        It will check if the special characters contains in this password is allowed in the allowed_special_characters
        """
        
        for char in password:
            if  char.isalpha() or char.isdigit() or char in allowed_special_characters:
                continue
            return False
        return True
    

if __name__ == '__main__':

    password = "abcd#$1234"
    min = 8
    max = 16
    allowed_special_characters = "!@#$%^&*()"
    print(PasswordValidator().validate_password_length(password, min, max))
    print(PasswordValidator().validate_sequential_character_limit(password, 4))
    print(PasswordValidator().validate_allowed_special_characters(password, allowed_special_characters))