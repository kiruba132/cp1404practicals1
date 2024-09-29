MENU = "G - Get a valid score\nP - Print result\nS - Show stars\nQ - Quit"


def main():

    print(MENU)
    choice = input(">>> ").upper()
    score = float(input("Enter score: "))
    while choice != "Q":
        if choice == "G":
            determine_score(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
        score = float(input("Enter score: "))
    print("Thank you")


def determine_score(score):
    if score >= 90:
        print("Excellent!")
    elif score >= 50:
        print("Passable!")
    else:
        print("Bad!")


def show_stars(score):
    print_stars = int(score) * "*"
    print (print_stars)


main()