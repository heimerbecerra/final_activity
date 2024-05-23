import os
import random

# Inventory
video_games = {
    'Fornite': {'price': 60, 'stock': 10},
    'Warzone': {'price': 50, 'stock': 8},
    'Gta 6': {'price': 55, 'stock': 5},
    'Free fire': {'price': 40, 'stock': 12},
}

transactions = []                                                            

# clear
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# inventory
def show_inventory():
    print("Video Game Inventory:")
    for game, details in video_games.items():
        print(f"{game}: ${details['price']} - Stock: {details['stock']} units")

# buy
def buy(game, quantity):
    if game in video_games:
        if video_games[game]['stock'] >= quantity:
            video_games[game]['stock'] -= quantity
            transactions.append(['Purchase', game, quantity, video_games[game]['price'] * quantity])
            print(f"You have purchased {quantity} units of {game}.")
        else:
            print(f"Not enough stock of {game}.")
    else:
        print(f"The video game {game} is not available in the inventory.")

def sell(game, quantity):
    if game in video_games:
        video_games[game]['stock'] += quantity
        transactions.append(['Sale', game, quantity, video_games[game]['price'] * quantity])
        print(f"You have sold {quantity} units of {game}.")
    else:
        print(f"The video game {game} is not available in the inventory.")

def add_game(game, price, stock):
    if game not in video_games:
        video_games[game] = {'price': price, 'stock': stock}
        print(f"The video game {game} has been added to the inventory.")
    else:
        print(f"The video game {game} already exists in the inventory.")

def play_game(game):
    if game in video_games:
        outcomes = ["won", "lost", "draw"]
        outcome = random.choice(outcomes)
        print(f"You played {game} and {outcome} the game!")
    else:
        print(f"The video game {game} is not available in the inventory.")

def total_sales():
    total = sum(transaction[3] for transaction in transactions if transaction[0] == 'Purchase')
    return total

def store_videogames():
    print("__________Welcome to the Video Game Store!__________")
    
    while True:
        print("\n1. Show Inventory")
        print("2. Buy Video Game")
        print("3. Sell Video Game")
        print("4. Add New Video Game")
        print("5. Play Video Game")
        print("6. Show Total Sales")
        print("7. Exit")

        option = input("Select an option: ")
        clear_screen() 

        if option == '1':
            show_inventory()
        elif option == '2':
            game = input("Enter the name of the video game to buy: ")
            quantity = int(input("Enter the quantity to buy: "))
            buy(game, quantity)
        elif option == '3':
            game = input("Enter the name of the video game to sell: ")
            quantity = int(input("Enter the quantity to sell: "))
            sell(game, quantity)
        elif option == '4':
            game = input("Enter the name of the new video game: ")
            price = float(input("Enter the price of the new video game: "))
            stock = int(input("Enter the initial stock of the new video game: "))
            add_game(game, price, stock)
        elif option == '5':
            game = input("Enter the name of the video game to play: ")
            play_game(game)
        elif option == '6':
            print(f"Total Sales: ${total_sales()}")
        elif option == '7':
            print("Thank you for using the video game store simulator.")
            break
        else:
            print("Invalid option. Please try again.")

    print("__________Goodbye (7u7)!__________")

# Run
store_videogames()
