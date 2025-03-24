import random
import time
from socket import socket

# Player attributes
player_health = 100
player_ammo = 50

# Enemy attributes
enemy_health = 50

# Game loop
while True:
    # Display player status
    print("Player Status:")
    print(f"Health: {player_health}")
    print(f"Ammo: {player_ammo}")
    print("\n")

    # Generate random enemy appearance
    if random.randint(1, 10) <= 3:
        print("An enemy appears!")
        print("\n")

        # Combat loop
        while True:
            # Player actions
            action = input("Do you want to (s)hoot or (r)un? ").lower()

            if action == 's':
                if player_ammo > 0:
                    # Player shoots
                    player_ammo -= 1
                    enemy_health -= random.randint(10, 20)
                    print("You shoot the enemy!")
                    print("\n")
                else:
                    print("Out of ammo!")
                    print("\n")
            elif action == 'r':
                print("You run away!")
                print("\n")
                break
            else:
                print("Invalid action!")
                print("\n")

            # Check enemy health
            if enemy_health <= 0:
                print("You defeated the enemy!")
                print("\n")
                break

            # Enemy attacks
            player_health -= random.randint(5, 15)
            print("The enemy attacks you!")
            print("\n")

            # Check player health
            if player_health <= 0:
                print("You were defeated by the enemy!")
                print("\n")
                break

    # Game over check
    if player_health <= 0:
        print("Game over!")
        break

    # Rest before next encounter
    time.sleep(1)
socket