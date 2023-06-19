import random


def userInput():
    ui = input("Enter: ")
    if not ui.isdigit():
        print("Strings are not acceptable")
        return userInput()
    if len(ui) != 4:
        print("The number should be 4-digit")
        return userInput()
    return ui


def userInputGameEnd(finalAttempt):
    uifinal = input(
        f"It took {finalAttempt} attempts!\nDo you want to play again? (y)es/(n)o: ").lower()
    if uifinal == "no" or uifinal == "n":
        return print("Have a nice day")
    if uifinal == "yes" or uifinal == "y":
        return main()
    else:
        return userInputGameEnd()


def rules():
    print("""Let's play Green, Yellow, Red!!!
Write any 4-digit number.

-For every digit you guessed correctly in the correct place, you have "Green”.
-For every digit you guessed correctly in the wrong place - "Yellow".”
-For each incorrect number, you'll get "Red".""")


def randNum():
    num = random.randint(1000, 9999)
    return num


def compare(ui, answer, attempts):
    attempts += 1
    ui_list = [int(x) for x in ui]
    answer_list = [int(x) for x in str(answer)]
    reds = 4
    greens = 0
    yellows = 0
    for i in range(len(ui_list)):
        if ui_list[i] == answer_list[i]:
            greens += 1
            reds -= 1
        elif ui_list[i] != answer_list[i] and ui_list[i] in answer_list:
            yellows += 1
            reds -= 1
    if greens != 4:
        print(f"You have:\n{greens} greens\n{yellows} yellows\n{reds} reds")
        return gameCycle(answer, attempts)
    return attempts


def gameCycle(answer, attempts):
    ui = userInput()
    finalAttempt = compare(ui, answer, attempts)
    if int(ui) == answer:
        print("You are correct")
        userInputGameEnd(finalAttempt)


def main():
    attempts = 0
    answer = randNum()
    rules()
    gameCycle(answer, attempts)


if __name__ == "__main__":
    main()
