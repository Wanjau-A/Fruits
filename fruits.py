def main():
    fruits = input("Fruit: ").strip().lower()
    if fruits == "apple":
        print(f"Number of calories in apple is 130")
    elif fruits == "avacado":
        print(f"Number of calories in avacado is 50")
    elif fruits == "banana":
        print("Number of calories in banana is 110")
    else:
        print("The fruit you entered is not in the database")


if __name__ == "__main__":
    main()