def user_input_integer(input_text = "Bitte Zahl eingeben: "):
    error = True
    try:
        user_input = input(input_text)
        user_input = int(user_input)
        error = False
    except ValueError:
        print(user_input, "ist keine Zahl")        
        # raise ValueError
    return user_input, error