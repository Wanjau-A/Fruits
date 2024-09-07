fruits = {
    "Apple":130,"Avacado":50,"Banana":110,"Cantaloupe":50,"Grapes":60,"Honeydew":90,"Kiwifruit":50,"Lemon":15,"Lime":20,
    "Nectarine":60,"Orange":80,"Peach":60,"Plumbs":100,"Strawberries":50,"Sweet Cherries":100,"Tangerine":50,"Watermelon":80
    }
def main():
    fruit = input("Fruit: ").strip().capitalize()
    if fruit in fruits:
        print(f"The number of calories in {fruit} is {fruits[fruit]}")
    else:
        print(f"{fruit} not found in the database")

if __name__ == "__main__":
    main()