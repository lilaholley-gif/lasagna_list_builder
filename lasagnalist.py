# ===== LASAGNA INGREDIENT LIST MANAGER =====

def load_list():
    try:
        with open("LasagnaList.txt", "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []


def save_list(ingredients):
    with open("LasagnaList.txt", "w") as file:
        for item in ingredients:
            file.write(item + "\n")


def print_list(ingredients):
    if not ingredients:
        print("\nThe ingredient list is empty.\n")
    else:
        print("\n--- LASAGNA INGREDIENTS ---")
        for i, item in enumerate(ingredients, start=1):
            print(f"{i}. {item}")
        print()


def add_item(ingredients):
    item = input("Enter ingredient to add: ")
    ingredients.append(item)
    print("Ingredient added!")


def remove_item(ingredients):
    print_list(ingredients)
    try:
        index = int(input("Enter item number to remove: "))
        ingredients.pop(index - 1)
        print("Ingredient removed!")
    except:
        print("Invalid input.")


def edit_item(ingredients):
    print_list(ingredients)
    try:
        index = int(input("Enter item number to edit: "))
        new_item = input("Enter new ingredient: ")
        ingredients[index - 1] = new_item
        print("Ingredient updated!")
    except:
        print("Invalid input.")


def move_item(ingredients):
    print_list(ingredients)
    try:
        old = int(input("Move which item number? "))
        new = int(input("Move to position: "))

        item = ingredients.pop(old - 1)
        ingredients.insert(new - 1, item)

        print("Ingredient moved!")
    except:
        print("Invalid input.")


def main():
    ingredients = load_list()

    while True:
        print("\n--- MENU ---")
        print("1. View List")
        print("2. Add Ingredient")
        print("3. Remove Ingredient")
        print("4. Edit Ingredient")
        print("5. Move Ingredient")
        print("6. Save and Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print_list(ingredients)
        elif choice == "2":
            add_item(ingredients)
        elif choice == "3":
            remove_item(ingredients)
        elif choice == "4":
            edit_item(ingredients)
        elif choice == "5":
            move_item(ingredients)
        elif choice == "6":
            save_list(ingredients)
            print("List saved. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()