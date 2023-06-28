import re

def toAlphaNumericString(value, max_length):
    alphanumeric_value = re.sub(r'\W+', '', value)
    return alphanumeric_value[:max_length]functions
