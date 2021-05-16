import secrets
import string

# We ask the users how many characters they want in the password
lenght = "How many characters do you want in your password?: "
combinations =  ["A: Just letters", "B: Just numbers/digits", "C: Numbers and letters", "D: Letters and special characters", "E: Numbers and special characters", "F: Letters, numbers and special characters"]

def pw_lenght():
    number_char = int(input(lenght))

    print("What type of password would you prefer?")

    for choices in combinations:
        print(choices)

    a = string.ascii_letters
    b = string.digits
    c = a + b
    d = a + string.punctuation
    e = b + string.punctuation
    f = string.ascii_letters + string.digits + string.punctuation

    passwordtype = str.upper(input("Make a choice between A-F: "))

    if passwordtype == "A":
        passworda = "".join(secrets.choice(a) for x in str(range(number_char)))
        print("Your password is: ", passworda)
    elif passwordtype == "B":
        passwordb = "".join(secrets.choice(b) for x in range(number_char))
        print("Your password is: ", passwordb)
    elif passwordtype == "C":
        passwordc = "".join(secrets.choice(c) for x in range(number_char))
        print("Your password is: ", passwordc)
    elif passwordtype == "D":
        passwordd = "".join(secrets.choice(d) for x in range(number_char))
        print("Your password is: ", passwordd)
    elif passwordtype == "E":
        passworde = "".join(secrets.choice(e) for x in range(number_char))
        print("Your password is: ", passworde)
    elif passwordtype == "F":
        passwordf = "".join(secrets.choice(f) for x in range(number_char))
        print("Your password is: ", passwordf)
    else:
        print("Please, type a letter between A-F")
