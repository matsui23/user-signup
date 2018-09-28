def validate_email(email):
    
    symbol = "@"
    period = "."

    if email == "":
        return 
    if email.find(symbol) == -1:
        return "Invalid username, missing '@'"
    if email.find(period) == -1:
        return "Invalid username, missing '.'"
    else:
        return
        