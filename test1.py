import random


# GET GUESS
def get_guess():
    return input("What is your guess:")


# Generate the code
def generate_code():
    digits = [str(num) for num in range(10)]

    random.shuffle(digits)

    return digits[:3]


# Generate clue
def generate_clue(code, user_guess):
    if user_guess == code:
        return "CODE CRACKED!"

    clues = []

    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")

    if clues == []:
        return ["Nope"]
    else:
        return clues


print("Welcome Code Breaker!")

secret_code = generate_code()

clue_report = []

while clue_report != "CODE CRACKED!":
    guess = get_guess()
    clue_report = generate_clue(guess, secret_code)
    print("here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
