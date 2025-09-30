# Advanced Project 2: Text Adventure Game 🗡️

import random

class TextAdventure:
    def __init__(self):
        self.player = {
            "name": "",
            "health": 100,
            "inventory": ["sword", "health potion"],
            "location": "village"
        }
        
        self.locations = {
            "village": {
                "description": "A peaceful village with friendly people.",
                "exits": ["forest", "cave"],
                "items": ["map", "bread"]
            },
            "forest": {
                "description": "A dark forest filled with mysterious sounds.",
                "exits": ["village", "castle"],
                "items": ["magic crystal"],
                "monster": {"name": "Wolf", "health": 30}
            },
            "cave": {
                "description": "A spooky cave with glittering gems on the walls.",
                "exits": ["village"],
                "items": ["treasure chest", "gem"],
                "monster": {"name": "Goblin", "health": 25}
            },
            "castle": {
                "description": "An ancient castle with tall towers.",
                "exits": ["forest"],
                "items": ["crown", "ancient book"],
                "monster": {"name": "Dragon", "health": 80}
            }
        }
    
    def start_game(self):
        print("🏰 Welcome to the Text Adventure Game! 🗡️")
        print("=" * 50)
        
        self.player["name"] = input("Enter your character's name: ")
        print(f"\nWelcome, {self.player['name']}!")
        print("You are a brave adventurer seeking treasure and glory!")
        
        self.show_help()
        self.game_loop()
    
    def show_help(self):
        print("\n📚 Available Commands:")
        print("  look - Examine your surroundings")
        print("  go <location> - Move to a different location")
        print("  take <item> - Pick up an item")
        print("  inventory - Check your inventory")
        print("  status - Check your health")
        print("  fight - Fight the monster in this location")
        print("  use <item> - Use an item from your inventory")
        print("  help - Show this help message")
        print("  quit - Exit the game")
    
    def game_loop(self):
        while True:
            print("\n" + "=" * 50)
            command = input("What do you want to do? ").lower().strip()
            
            if command == "look":
                self.look_around()
            elif command.startswith("go "):
                destination = command[3:]
                self.move(destination)
            elif command.startswith("take "):
                item = command[5:]
                self.take_item(item)
            elif command == "inventory":
                self.show_inventory()
            elif command == "status":
                self.show_status()
            elif command == "fight":
                self.fight_monster()
            elif command.startswith("use "):
                item = command[4:]
                self.use_item(item)
            elif command == "help":
                self.show_help()
            elif command == "quit":
                print(f"Thanks for playing, {self.player['name']}! 👋")
                break
            else:
                print("❌ I don't understand that command. Type 'help' for available commands.")
    
    def look_around(self):
        location = self.locations[self.player["location"]]
        print(f"\n🏞️ You are in the {self.player['location']}.")
        print(f"📖 {location['description']}")
        
        if location.get("items"):
            print(f"🎒 Items here: {', '.join(location['items'])}")
        
        if location.get("monster"):
            monster = location["monster"]
            print(f"⚔️ There's a {monster['name']} here! (Health: {monster['health']})")
        
        print(f"🚪 You can go to: {', '.join(location['exits'])}")
    
    def move(self, destination):
        current_location = self.locations[self.player["location"]]
        
        if destination in current_location["exits"]:
            self.player["location"] = destination
            print(f"🚶 You moved to the {destination}.")
            self.look_around()
        else:
            print(f"❌ You can't go to {destination} from here.")
    
    def take_item(self, item):
        location = self.locations[self.player["location"]]
        
        if location.get("items") and item in location["items"]:
            location["items"].remove(item)
            self.player["inventory"].append(item)
            print(f"✅ You picked up the {item}!")
        else:
            print(f"❌ There's no {item} here to take.")
    
    def show_inventory(self):
        if self.player["inventory"]:
            print(f"🎒 Your inventory: {', '.join(self.player['inventory'])}")
        else:
            print("🎒 Your inventory is empty.")
    
    def show_status(self):
        print(f"👤 Name: {self.player['name']}")
        print(f"❤️ Health: {self.player['health']}")
        print(f"📍 Location: {self.player['location']}")
    
    def fight_monster(self):
        location = self.locations[self.player["location"]]
        
        if not location.get("monster"):
            print("❌ There's no monster here to fight!")
            return
        
        monster = location["monster"]
        print(f"⚔️ You engage in battle with the {monster['name']}!")
        
        while monster["health"] > 0 and self.player["health"] > 0:
            # Player attacks
            player_damage = random.randint(10, 25)
            monster["health"] -= player_damage
            print(f"🗡️ You attack for {player_damage} damage!")
            
            if monster["health"] <= 0:
                print(f"🎉 You defeated the {monster['name']}!")
                del location["monster"]  # Remove monster from location
                
                # Random reward
                rewards = ["gold coin", "magic potion", "rare gem"]
                reward = random.choice(rewards)
                self.player["inventory"].append(reward)
                print(f"🎁 You found a {reward}!")
                break
            
            # Monster attacks
            monster_damage = random.randint(5, 15)
            self.player["health"] -= monster_damage
            print(f"👹 The {monster['name']} attacks you for {monster_damage} damage!")
            print(f"❤️ Your health: {self.player['health']}")
            
            if self.player["health"] <= 0:
                print("💀 You have been defeated! Game Over!")
                return
    
    def use_item(self, item):
        if item not in self.player["inventory"]:
            print(f"❌ You don't have a {item}!")
            return
        
        if item == "health potion":
            self.player["health"] = min(100, self.player["health"] + 30)
            self.player["inventory"].remove(item)
            print(f"🧪 You used a health potion! Health restored to {self.player['health']}")
        elif item == "magic potion":
            self.player["health"] = min(100, self.player["health"] + 50)
            self.player["inventory"].remove(item)
            print(f"✨ You used a magic potion! Health restored to {self.player['health']}")
        elif item == "bread":
            self.player["health"] = min(100, self.player["health"] + 10)
            self.player["inventory"].remove(item)
            print(f"🍞 You ate the bread! Health restored to {self.player['health']}")
        else:
            print(f"❌ You can't use the {item}!")

def main():
    game = TextAdventure()
    game.start_game()

if __name__ == "__main__":
    main()

# 🎯 Features of this project:
# - Uses nested dictionaries for game world
# - Uses lists for inventory and location exits
# - Uses functions for game actions
# - Uses loops for the main game flow
# - Uses if/else statements for game logic
# - Uses random module for combat
# - Combines ALL the concepts we've learned!

# 💡 Ideas to extend this project:
# 1. Add more locations and monsters
# 2. Create a leveling system
# 3. Add different weapon types
# 4. Save/load game functionality
# 5. Add puzzles to solve