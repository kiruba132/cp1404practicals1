"""
CP1404- Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    print(determine_status(score))

    random_score = random.randint(0, 100)  # Generate a random score between 0 and 100
    print(f"Random score: {random_score:.2f}, Status: {determine_status(random_score)}")

def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"
main()

