def validate(username):
    
    if username == "":
        return "Username is empty"

    if len(username) > 20 or len(username) < 3:
        return "Username should be shorter than 20 chars but greater than 3 chars."

    return
