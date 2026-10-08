VALID_PREFIX = "SAVE"
CODE_LENGTH = 10 # Changed from 8 to 10 characters for 6 digit codes


def normalise(code):
    return code.strip().upper()


def is_valid(code):
    code = normalise(code)

    if code.startswith("SAVE00"): # Added another check 
        return False
    if len(code) != CODE_LENGTH:
        return False
    if not code.startswith(VALID_PREFIX):
        return False
    if not code[len(VALID_PREFIX):].isdigit(): # Changed so that the valid_prefix can be interchangeable with any value as long as it is the valid prefix
        return False

    return True


entered_codes = ["save2024", " SAVE1234 ", "SAVE12", "SALE1234", "SAVE12AB"]

for entry in entered_codes:
    if is_valid(entry):
        print(f"{entry} accepted, discount applied")
    else:
        print(f"{entry} rejected")

# Accepted
# Accepted
# Rejected
# 
# Rejected