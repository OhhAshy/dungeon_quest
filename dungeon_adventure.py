import random

def main():
    def setup_player():
      name = input("Enter your name:")
      player = {"name": name,"health": 10, "inventory":[]}
      return player

      




    
       
       
      """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        # TODO: Ask the user for their name using input()
        # TODO: Initialize a dictionary with keys: "name", "health", and "inventory"
        # TODO: Return the dictionary


    def create_treasures():

        treasures = {"gold coin": random.randint(1,100),"ruby": random.randint(1,100), "ancient scroll": random.randint(1,100), "emerald": random.randint(1,100), "silver ring": random.randint(1,100)}
        return treasures

        

    
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        # TODO: Create a dictionary of treasure names and integer values
        # TODO: Return the dictionary


    def display_options(player, room_number):

        room_number: int
    
    
        
        print(f"You are in room {room_number}.")
        print(f"How will you proceed {player['name']}?")
        print("1. Search for more loot")
        print("2. Move to the next room")
        print("3. Check your life points and loot")
        print("4. Surrender")

            


        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        # TODO: Print the room number and the 4 menu options listed above


    def search_room(player, treasures):

        search = random.choice(["treasure", "trap"])

        if search == "treasure":
        
            treasure_name = random.choice(list(treasures.keys()))
            treasure_value = treasures[treasure_name]

            player.setdefault("inventory", []).append(treasure_name)

            print(f"You found some loot: {treasure_name} worth {treasure_value} gold!")

        else:
         
         player["health"] -=2
         print("You have fallen into a trap... You lost 2 life points")
        
         


         """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        # TODO: Write an if/else to handle treasure vs trap outcomes
        # TODO: Update player dictionary accordingly
        # TODO: Print messages describing what happened


    def check_status(player):
        print(f"Health: {player['health']}")

        inventory = player.get("inventory", [])

        if inventory:
            print("Inventory:", ",".join(inventory))
        else:
            print("Inventory: You have no items yet.")
        
        
        
        
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        # TODO: Print player health
        # TODO: If the inventory list is not empty, print items joined by commas
        # TODO: Otherwise print “You have no items yet.”


    def end_game(player, treasures):

        print(f"Final Health: {player['health']}")

        inventory = player.get("inventory", [])

        if inventory:
            print("Treasures:", ",".join(inventory))
        else:
            print("Treasures: You gained nothing....")

        total_gold = sum(treasures.get(item, 0) for item in inventory)
        print(f"Total Gold: {total_gold} gold")

        print(f"Game Over! Thanks for playing {player['name']}!")

        
        
        
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        # TODO: Calculate total score by summing the value of collected treasures
        # TODO: Print final health, items, and total value
        # TODO: End with a message like "Game Over! Thanks for playing."


    def run_game_loop(player, treasures):

        for room_number in range(1,6):
            print(f"You have entered Room {room_number}.")
            while True:
                display_options(player, room_number)
                choice = input("Enter your decision: ").strip()

        

                if choice == "1":
                    search_room(player, treasures)

                    if player['health'] < 1:
                        print(f"{player['name']} has been slain...")
                        end_game(player, treasures)
                        return
                elif choice =="2":
                    print(f"Moving to room {room_number + 1}")
                    break
                elif choice == "3":
                    print(f"Player status:{player}")
                elif choice == "4":
                    print(f"{player['name']} has surrendered!")
                    end_game(player, treasures)
                    return
                else:
                    print("Invalid option. Please try again choose 1, 2, 3, or 4.")

        print(f"You have explored all the rooms congrats on beating the dungeon, {player['name']}!")
        end_game(player, treasures)


        
    



        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # TODO: Loop through 5 rooms (1–5)
        # TODO: Inside each room, prompt player choice using input()
        # TODO: Use if/elif to handle each choice (1–4)
        # TODO: Break or return appropriately when player quits or dies
        # TODO: Call end_game() after all rooms are explored


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()
