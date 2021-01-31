shopping_list = {}

name = "a"
quantity = 0
price = 0  # In Cents
total = 0
rest = 0

products = []
# Product list example: product = [[name, quantity, price in cents], ["b", 1, 2]]
emails = []
# Email list examples: email = [client@google.com, bob@ana.com]


def shop():
    print("\nThis is your shopping list! Do you want to add an item?")

    option = int(input("Press 1 to add an item and 2 to finish\n"))

    while option != 2:
        if option != 1 and option != 2:
            print("Invalid option, try again")
            option = int(input("\nPress 1 to add an item and 2 to finish\n"))
        else:
            name = str(input("\nItem name\n"))
            quantity = int(input("\nAmount\n"))
            price = int(input("\nPrice in cents\n"))
            products.append([name, quantity, price])
            option = int(input("\nPress 1 to add another item and 2 to finish\n"))


def add_email():
    print("\nDo you want to add an email to pay the bill?")
    finishing = int(input("Press 1 to add an email and 2 to finish\n"))
    account = ""
    while finishing != 2:
        if finishing != 1 and finishing != 2:
            print("Invalid option, try again")
            finishing = int(input("\nPress 1 to add an email and 2 to finish\n"))
        else:
            account = input("\nInsert the email\n")
            emails.append(account)
            finishing = int(input("\nPress 1 to add another email and 2 to finish\n"))


while len(products) == 0 or len(emails) == 0:
    if len(products) == 0:
        print("\nYour shopping list is empty, do you want to add an item or finish the operation?")
        choice = int(input("1 to add item, 2 to end operation\n"))
        while choice != 2:
            if choice != 1 and choice != 2:
                print("Invalid option, try again")
                choice = int(input("1 to add item, 2 to end operation\n"))
            elif choice == 1:
                shop()
                break
    elif len(emails) == 0:
        print("\nThere's no one to pay the bill, do you want to cancel?")
        choice = int(input("1 to add email, 2 to end operation\n"))
        while choice != 2:
            if choice != 1 and choice != 2:
                print("Invalid option, try again")
                choice = int(input("1 to add email, 2 to end operation\n"))
            elif choice == 1:
                add_email()
                break
    if choice == 2:
        break


if len(products) != 0 and len(emails) != 0:
    for value in products:
        total += value[1] * value[2]

    while total % len(emails) != 0:
        rest += 1
        total -= 1
    for each in emails:
        shopping_list[each] = int(total / len(emails))
        if rest != 0:
            shopping_list[each] += 1
            rest -= 1
    print(shopping_list)
