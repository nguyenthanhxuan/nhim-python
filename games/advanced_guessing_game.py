# Advanced Game: Number Guessing with Levels 🎯

import random

def create_guessing_game():
    """Advanced number guessing game with multiple difficulty levels"""
    
    print("🎮 Welcome to the Ultimate Number Guessing Game!")
    print("=" * 50)
    
    # Game statistics
    stats = {
        "games_played": 0,
        "total_guesses": 0,
        "best_score": float('inf'),
        "levels_completed": []
    }
    
    # Difficulty levels
    levels = {
        1: {"name": "Beginner", "range": (1, 10), "max_guesses": 5},
        2: {"name": "Easy", "range": (1, 25), "max_guesses": 7},
        3: {"name": "Medium", "range": (1, 50), "max_guesses": 8},
        4: {"name": "Hard", "range": (1, 100), "max_guesses": 10},
        5: {"name": "Expert", "range": (1, 200), "max_guesses": 12},
        6: {"name": "Master", "range": (1, 500), "max_guesses": 15}
    }
    
    def play_level(level_num):
        """Play a single level of the guessing game"""
        level = levels[level_num]
        min_num, max_num = level["range"]
        max_guesses = level["max_guesses"]
        
        secret_number = random.randint(min_num, max_num)
        guesses_used = 0
        
        print(f"\n🎯 Level {level_num}: {level['name']}")
        print(f"📊 Range: {min_num} to {max_num}")
        print(f"🎲 You have {max_guesses} guesses to find the number!")
        print("-" * 40)
        
        while guesses_used < max_guesses:
            try:
                guess = int(input(f"Guess #{guesses_used + 1}: "))
                guesses_used += 1
                
                if guess == secret_number:
                    print(f"🎉 Congratulations! You found {secret_number}!")
                    print(f"🏆 You won in {guesses_used} guesses!")
                    
                    # Calculate score (fewer guesses = better score)
                    score = max_guesses - guesses_used + 1
                    print(f"⭐ Score for this level: {score} points")
                    
                    return guesses_used, True
                    
                elif guess < secret_number:
                    remaining = max_guesses - guesses_used
                    if remaining > 0:
                        print(f"📈 Too low! {remaining} guesses remaining.")
                    
                elif guess > secret_number:
                    remaining = max_guesses - guesses_used
                    if remaining > 0:
                        print(f"📉 Too high! {remaining} guesses remaining.")
                        
            except ValueError:
                print("❌ Please enter a valid number!")
                continue
        
        print(f"💔 Game Over! The number was {secret_number}")
        return guesses_used, False
    
    def show_stats():
        """Display player statistics"""
        print("\n📊 Your Statistics:")
        print("=" * 30)
        print(f"Games played: {stats['games_played']}")
        if stats['games_played'] > 0:
            avg_guesses = stats['total_guesses'] / stats['games_played']
            print(f"Average guesses per game: {avg_guesses:.1f}")
            if stats['best_score'] != float('inf'):
                print(f"Best game (fewest guesses): {stats['best_score']}")
        
        if stats['levels_completed']:
            print(f"Levels completed: {len(stats['levels_completed'])}")
            print(f"Highest level reached: {max(stats['levels_completed'])}")
    
    def show_levels():
        """Display available difficulty levels"""
        print("\n🎯 Available Levels:")
        print("=" * 40)
        for level_num, level_info in levels.items():
            status = "✅" if level_num in stats['levels_completed'] else "🔒"
            print(f"{status} Level {level_num}: {level_info['name']}")
            print(f"    Range: {level_info['range'][0]}-{level_info['range'][1]}")
            print(f"    Max guesses: {level_info['max_guesses']}")
    
    # Main game loop
    while True:
        print("\n" + "=" * 50)
        print("🎮 Main Menu")
        print("1. Play a level")
        print("2. View levels")
        print("3. View statistics")
        print("4. Tutorial")
        print("5. Quit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == "1":
            show_levels()
            try:
                level_choice = int(input(f"\nChoose level (1-{len(levels)}): "))
                if level_choice in levels:
                    guesses, won = play_level(level_choice)
                    
                    # Update statistics
                    stats['games_played'] += 1
                    stats['total_guesses'] += guesses
                    
                    if won:
                        if level_choice not in stats['levels_completed']:
                            stats['levels_completed'].append(level_choice)
                        if guesses < stats['best_score']:
                            stats['best_score'] = guesses
                    
                else:
                    print("❌ Invalid level choice!")
            except ValueError:
                print("❌ Please enter a valid number!")
                
        elif choice == "2":
            show_levels()
            
        elif choice == "3":
            show_stats()
            
        elif choice == "4":
            print("\n📚 How to Play:")
            print("🎯 Try to guess the secret number in as few attempts as possible")
            print("📈 If your guess is too low, you'll be told to go higher")
            print("📉 If your guess is too high, you'll be told to go lower")
            print("🏆 Complete levels to unlock harder challenges")
            print("⭐ Fewer guesses = higher score!")
            
        elif choice == "5":
            print("\n👋 Thanks for playing! Here are your final stats:")
            show_stats()
            print("\nCome back anytime to improve your guessing skills!")
            break
            
        else:
            print("❌ Invalid choice! Please choose 1-5.")

if __name__ == "__main__":
    create_guessing_game()

# 🎯 Features of this game:
# - Multiple difficulty levels
# - Score tracking and statistics
# - Progress saving (levels completed)
# - User-friendly menu system
# - Input validation
# - Detailed feedback

# 💡 Try these challenges:
# 1. Complete all 6 levels!
# 2. Try to beat each level in the minimum number of guesses
# 3. Can you complete Level 6 (Master) in under 10 guesses?