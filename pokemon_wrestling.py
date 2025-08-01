"""
Sydney Umezurike
This program simulates a Pokémon arm wrestling 
tournament between a player and a computer.
"""

import random

POKEMON_LIST = [
    "Bulbasaur", "Charmander", "Butterfree", 
    "Rattata", "Weedle", "Pikachu", 
    "Sandslash", "Jigglypuff", "Raichu", 
    "Diglett"
]

def get_player(number):
    """ 
    Returns the name of the Pokemon associated with the numbering scheme 
    described. Any value 'out of bounds' returns Diglett by default. 
    For example, get_player(2) returns Charmander. get_player(101) 
    returns Diglett.
    """
    if 1 <= number <= len(POKEMON_LIST):
        return POKEMON_LIST[number - 1]
    return "Diglett"

def roll_dice():
    """ 
    Returns a random integer in the range 2..12 (inclusive).
    """
    return random.randint(2, 12)

def is_power_up_active(number):
    """ 
    Returns True or False based on the 'power-up' rules described in 
    the assignment text. The parameter value passed in is the value 
    from a valid roll of the dice to determine the power-up status.
    """
    return number == 7 or number == 11

def check_battle(computer, player):
    """ 
    Given the input parameters of the power values for the computer's 
    character and the player's character, determine the winner of the 
    1-1 matchup. Highest power score wins. In the case of a tie, it 
    is considered a draw. This function returns a string that indicates 
    the result: 'COMPUTER' if computer wins, 'PLAYER' if player wins, 
    or 'DRAW!' if the 1-1 matchup is a tie.
    """
    if computer > player:
        return "COMPUTER"
    elif player > computer:
        return "PLAYER"
    return "DRAW!"

def main():
    """Run the Pokémon arm wrestling tournament."""
    print("Welcome to the Pokémon Arm Wrestling Tournament!")
    
    # Team selection
    team_choice = input("Which team would you like to be? "
                        "(Red/Blue): ").strip().lower()
    
    # Initialize counters for wins
    player_wins = 0
    computer_wins = 0

    continue_playing = True

    while continue_playing:
        # Player selects a Pokémon
        player_pokemon_number = random.randint(1, len(POKEMON_LIST))
        player_pokemon = get_player(player_pokemon_number)
        
        # Computer selects a Pokémon
        computer_pokemon_number = random.randint(1, len(POKEMON_LIST))
        computer_pokemon = get_player(computer_pokemon_number)

        print(f"\nRound Start: {team_choice.capitalize()} "
              f"{player_pokemon} vs. Computer {computer_pokemon}")
        print("Highest dice roll wins. If you don't roll, "
              "we'll end the match.")

        # Player rolls the dice
        roll = input("Would you like to roll the dice? "
                     "(yes/no): ").strip().lower()
        if roll == "yes":
            player_dice_roll = roll_dice()
            print(f"You rolled a {player_dice_roll}.")
            player_power = (player_dice_roll + 
                            (1 if is_power_up_active(player_dice_roll) 
                             else 0))

            # Computer rolls the dice
            computer_dice_roll = roll_dice()
            print(f"Computer rolled a {computer_dice_roll}.")
            computer_power = (computer_dice_roll + 
                              (1 if is_power_up_active(computer_dice_roll) 
                               else 0))

            # Determine the winner
            winner = check_battle(computer_power, player_power)
            if winner == "PLAYER":
                player_wins += 1
                print(f"You win this round! {player_pokemon} wins!")
            elif winner == "COMPUTER":
                computer_wins += 1
                print(f"Computer wins this round! {computer_pokemon} wins!")
            else:
                print("It's a draw! No wins added.")

        else:
            print("Ending the match. Thank you for playing!")
            continue_playing = False  # End match if the player doesn't roll

        # Ask if the player wants to continue
        if continue_playing:
            continue_response = input("Would you like to continue to the next "
                                      "round? (yes/no): ").strip().lower()
            continue_playing = continue_response == "yes"

    # Print the tournament result
    print("\nTournament Over!")
    print(f"You won {player_wins} rounds.")
    print(f"The computer won {computer_wins} rounds.")
    if player_wins > computer_wins:
        print("Congratulations! You are the champion of the tournament!")
    elif computer_wins > player_wins:
        print("The computer is the champion of the tournament!")
    else:
        print("The tournament ended in a tie!")

if __name__ == "__main__":
    main()
