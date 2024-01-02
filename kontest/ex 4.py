
def check_password(s):
    english_lowercase = "abcdefghijklmnopqrstuvwxyz"
    english_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_symbols = "!@$%*.,?"
    lower_case_cnt, upper_case_cnt, special_symbols_cnt, digits_cnt = 0, 0, 0, 0
    for element in s:
        if element in english_lowercase:
            lower_case_cnt += 1
        elif element in english_uppercase:
            upper_case_cnt += 1
        elif element in special_symbols:
            special_symbols_cnt += 1
        elif element in digits:
            digits_cnt += 1
        else:
            return "not valid"
    if 8 <= len(s) <= 20 and lower_case_cnt > 0 and upper_case_cnt > 0 and special_symbols_cnt > 0 and digits_cnt > 0:
        return "valid"
    return "not valid"

print(check_password("")) # должно вернуть "not valid"
print(check_password("password")) # должно вернуть "not valid"
print(check_password("P1@p")) # должно вернуть "not valid"
print(check_password("P1@pP1@p")) # должно вернуть "valid"
print(check_password("P1@pP1@pP1@pP1@pP1@pP1@p")) # должно вернуть "not valid"
print(check_password("Paaaaaa2!!!")) # должно вернуть "not valid"