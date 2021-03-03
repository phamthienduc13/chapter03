userPocketNumber = int(input("Enter a pocket number: "))

if userPocketNumber >= 0 and userPocketNumber <= 36:

    if userPocketNumber == 0:
        userPocketColor = "green"

    elif userPocketNumber >= 1 and userPocketNumber <= 10:
        if userPocketNumber % 2 == 0:
            userPocketColor = "black"
        else:
            userPocketColor = "red"

    elif userPocketNumber >= 11 and userPocketNumber <= 18:
        if userPocketNumber % 2 == 0:
            userPocketColor = "red"
        else:
            userPocketColor = "black"

    elif userPocketNumber >= 19 and userPocketNumber <= 28:
        if userPocketNumber % 2 == 0:
            userPocketColor = "black"
        else:
            userPocketColor = "red"

    elif userPocketNumber >= 29 and userPocketNumber <= 36:
        if userPocketNumber % 2 == 0:
            userPocketColor = "red"
        else:
            userPocketColor = "black"

    print("User pocket color = ", userPocketColor)
else:
    print("Error. Please enter number between 0-36.")