def validate_pass(password, verify_password):
    
    if password != verify_password:
        return "Those passwords don't match"

    if password == "":
        return "Password is empty"

    if len(password) > 20 or len(password) < 3:
        return "Password should be shorter than 20 chars but greater than 3 chars."

    return