# Simple Game: Rock, Paper, Scissors! ✂️📄🗿

import random

print("🎮 Welcome to Rock, Paper, Scissors!")
print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
print("Type 'quit' to stop playing\n")

# Keep score
player_wins = 0
computer_wins = 0
ties = 0

while True:
    # Get player choice
    player_choice = input("Choose rock, paper, or scissors (or 'quit'): ").lower()
    
    if player_choice == 'quit':
        break
    
    if player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue
    
    # Computer makes random choice
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine winner
    if player_choice == computer_choice:
        print("It's a tie! 🤝")
        ties += 1
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        print("You win! 🎉")
        player_wins += 1
    else:
        print("Computer wins! 🤖")
        computer_wins += 1
    
    # Show current score
    print(f"\nScore: You {player_wins} - {computer_wins} Computer (Ties: {ties})")
    print("-" * 40)

# Final score
print(f"\n🏆 Final Score:")
print(f"You: {player_wins}")
print(f"Computer: {computer_wins}")
print(f"Ties: {ties}")

if player_wins > computer_wins:
    print("🎉 You're the overall winner! Great job!")
elif computer_wins > player_wins:
    print("🤖 Computer wins overall! Better luck next time!")
else:
    print("🤝 It's a tie overall! What a close game!")

print("\nThanks for playing! 👋")