def display_welcome():
    print("\n============================================")
    print("       WELCOME TO FAST FOOD RESTAURANT")
    print("============================================")


def ask_yes_no(message):
    while True:
        answer = input(message).strip().lower()

        if answer in ["yes", "y"]:
            return True

        elif answer in ["no", "n"]:
            return False

        else:
            print("Please enter yes or no.")