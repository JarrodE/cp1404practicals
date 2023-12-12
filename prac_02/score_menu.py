
MENU = """(G)et score (must be 0-100)
(P)rint result
(S)how stars
(Q)uit"""


def main():
    score = int(input("Score: "))
    parameters(score)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Score: "))
            parameters(score)
        elif choice == "P":
            score_ranks(score)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def parameters(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def score_ranks(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Pass")
    else:
        print("Fail")


def print_stars(score):
    print(f"{'*' * score}")


main()
