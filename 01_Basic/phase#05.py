# #Library Management System

books = ["Python", "Math", "Science"]

select = input("1)Show  2)Borrow  3)Return : ")

if select == "1":
    print(books)

elif select == "2":
    book = input("Book: ")
    books.remove(book)
    print("Borrowed!")

elif select == "3":
    book = input("Book: ")
    books.append(book)
    print("Returned!")



# Simple banking system
balance = 1000

option = input("1)Withdraw 2)Deposit 3)Balance:")

if option == "1":
    balance -= int(input("Amount:"))
elif option == "2":
    balance += int(input("Amount: "))
    
print(f"Balance: {balance}")

    