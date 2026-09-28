shopping_list = []

while True:
    print("\nadd / remove / show / done")
    choice = input("What do you want to do? ").lower()

    if choice == "add":
        item = input("Enter item: ")
        shopping_list.append(item)
        print(item, "added to your list.")

    elif choice == "remove":
        item = input("Enter item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed from your list.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        print("Your shopping list:")
        for item in shopping_list:
            print(item)

    elif choice == "done":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose add, remove, show, or done.")