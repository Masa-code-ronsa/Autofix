import re

def validateEmailByRegex(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False