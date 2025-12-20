"""
Text Adventure Game

Navigate through rooms, collect items, and solve puzzles!
"""

import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Room:
    """Represents a room in the adventure."""
    def __init__(self, name, description, items=None, exits=None):
        self.name = name
        self.description = description
        self.items = items if items else []
        self.exits = exits if exits else {}
    
    def add_exit(self, direction, room_name):
        """Add an exit to another room."""
        self.exits[direction] = room_name

class Game:
    """Main game class."""
    def __init__(self):
        self.inventory = []
        self.current_room = "entrance"
        self.rooms = self.create_rooms()
    
    def create_rooms(self):
        """Create all rooms in the game."""
        rooms = {
            "entrance": Room(
                "Entrance Hall",
                "You stand in a grand entrance hall. Dusty paintings line the walls.",
                items=["torch"],
                exits={"north": "library", "east": "kitchen"}
            ),
            "library": Room(
                "Ancient Library",
                "Tall bookshelves filled with old tomes surround you. A desk sits in the corner.",
                items=["key"],
                exits={"south": "entrance", "east": "study"}
            ),
            "kitchen": Room(
                "Abandoned Kitchen",
                "Pots and pans hang from the ceiling. A strange smell lingers in the air.",
                items=["knife"],
                exits={"west": "entrance", "north": "study"}
            ),
            "study": Room(
                "Mysterious Study",
                "A room filled with strange artifacts and a locked chest in the corner.",
                items=[],
                exits={"west": "library", "south": "kitchen"}
            ),
            "treasure": Room(
                "Treasure Room",
                "GOLD! JEWELS! You've found the treasure room! 🎉",
                items=["gold", "jewels"],
                exits={}
            )
        }
        
        # Add secret exit from study to treasure (requires key)
        return rooms
    
    def look_around(self):
        """Display current room information."""
        room = self.rooms[self.current_room]
        print(f"\n📍 {room.name}")
        print(f"{room.description}\n")
        
        if room.items:
            print(f"Items visible: {', '.join(room.items)}")
        
        if room.exits:
            directions = ", ".join(room.exits.keys())
            print(f"Exits: {directions}")
        
        print()
    
    def go(self, direction):
        """Move to another room."""
        room = self.rooms[self.current_room]
        
        if direction not in room.exits:
            print("You can't go that way!")
            return
        
        next_room_name = room.exits[direction]
        
        # Special case: study to treasure requires key
        if self.current_room == "study" and next_room_name == "treasure":
            if "key" not in self.inventory:
                print("The door is locked! You need a key.")
                return
        
        self.current_room = next_room_name
        print(f"You move {direction}...")
    
    def take(self, item):
        """Take an item from the current room."""
        room = self.rooms[self.current_room]
        
        if item not in room.items:
            print("That item is not here!")
            return
        
        room.items.remove(item)
        self.inventory.append(item)
        print(f"You picked up the {item}.")
    
    def inventory_command(self):
        """Display inventory."""
        if self.inventory:
            print(f"\nInventory: {', '.join(self.inventory)}")
        else:
            print("\nYour inventory is empty.")
    
    def help_command(self):
        """Display help information."""
        print("""
Available commands:
  look/l          - Look around the current room
  go [direction]  - Move in a direction (north, south, east, west)
  take [item]     - Pick up an item
  inventory/i     - Check your inventory
  help/h          - Show this help message
  quit/q          - Quit the game
        """)

def main():
    """Main game loop."""
    game = Game()
    
    clear_screen()
    print("=" * 50)
    print("🗺️  TEXT ADVENTURE 🗺️")
    print("=" * 50)
    print("\nWelcome, adventurer!")
    print("Explore the rooms, collect items, and find the treasure!")
    print("Type 'help' for commands.\n")
    
    game.look_around()
    
    while True:
        command = input("> ").lower().strip().split()
        
        if not command:
            continue
        
        cmd = command[0]
        
        if cmd in ['quit', 'q', 'exit']:
            print("\nThanks for playing!")
            break
        elif cmd in ['look', 'l']:
            game.look_around()
        elif cmd == 'go':
            if len(command) > 1:
                game.go(command[1])
                game.look_around()
            else:
                print("Go where? (north, south, east, west)")
        elif cmd == 'take':
            if len(command) > 1:
                game.take(command[1])
            else:
                print("Take what?")
        elif cmd in ['inventory', 'i']:
            game.inventory_command()
        elif cmd in ['help', 'h']:
            game.help_command()
        else:
            print("Unknown command. Type 'help' for available commands.")
        
        # Check win condition
        if game.current_room == "treasure":
            print("\n" + "=" * 50)
            print("🎉🎉🎉 CONGRATULATIONS! 🎉🎉🎉")
            print("You found the treasure room!")
            print("You win!")
            print("=" * 50)
            break
    
    input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()

