print("Welcome to Brand Name Generator")

city_name = input("\nEnter your city name: ").strip()
pet_name = input("Enter your pet name: ").strip()
item_name = input("Enter the item you sell: ").strip()

print("\nChoose your brand name combination:")
print("1. City name + Pet name")
print("2. City name + Item name")
print("3. Pet name + Item name")

brand_name = None

while brand_name is None:
    try:
        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            brand_name = city_name + " " + pet_name
        elif choice == 2:
            brand_name = city_name + " " + item_name
        elif choice == 3:
            brand_name = pet_name + " " + item_name
        else:
            print("Invalid choice. Enter a number from 1 to 3.")

    except ValueError:
        print("Invalid input. Please enter a number.")

print("\nYour brand name could be:", brand_name)
