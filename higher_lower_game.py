

from art import logo, vs
from game_data import data
import random


def format_data(account):
    """Format the account data so it looks better when printed."""
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Check if the user's guess is correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)

score = 0
game_should_continue = True

# Choose two different accounts to start the game
account_a = random.choice(data)
account_b = random.choice(data)

while account_a == account_b:
    account_b = random.choice(data)


while game_should_continue:

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask the user to guess who has more followers
    guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    # Get the follower counts of both accounts
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    # Check if the guess is correct
    is_correct = check_answer(guess, a_followers, b_followers)

    # Clear the screen and show the logo again
    print("\n" * 20)
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")

        # Keep the account with more followers
        if a_followers > b_followers:
            # A has more followers, so keep A and change B
            account_b = random.choice(data)

            while account_b == account_a:
                account_b = random.choice(data)

        else:
            # B has more followers, so make B the new A
            account_a = account_b
            account_b = random.choice(data)

            while account_b == account_a:
                account_b = random.choice(data)

    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False
