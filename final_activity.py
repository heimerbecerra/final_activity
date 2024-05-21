
import random

# inventory
video_games = {
    'Fornite': {'price': 60, 'stock': 10},
    'Warzone': {'price': 50, 'stock': 8},
    'Gta 6': {'price': 55, 'stock': 5},
    'Free fire': {'price': 40, 'stock': 12},
}

transactions = []

# Function
def show_inventory():
    print("Video Game Inventory:")
    for game, details in video_games.items():
        print(f"{game}: ${details['price']} - Stock: {details['stock']} units")

# Function to buy video games
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

# Function to sell video games
def sell(game, quantity):
    if game in video_games:
        video_games[game]['stock'] += quantity
        transactions.append(['Sale', game, quantity, video_games[game]['price'] * quantity])
        print(f"You have sold {quantity} units of {game}.")
    else:
        print(f"The video game {game} is not available in the inventory.")

# Function to calculate total sales
def total_sales():
    total = sum(transaction[3] for transaction in transactions if transaction[0] == 'Purchase')
    return total

# Main function of the simulator
def store_videogames():
    print("__________Welcome to the Video Game 7u7!__________")
    
    while True:
        print("\n1. Show Inventory")
        print("2. Buy Video Game")
        print("3. Sell Video Game")
        print("4. Show Total Sales")
        print("5. Exit")

        option = input("Select an option: ")

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
            print(f"Total Sales: ${total_sales()}")
        elif option == '5':
            print("Thank you for using the video game store simulator.")
            break
        else:
            print("Invalid option. Please try again.")

    print("__________Goodbye bby 7u7!__________")

# Run the simulator
store_videogames()



