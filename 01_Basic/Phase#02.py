#Simple Quiz App

print("Q1: Capital of Pakistan?")
ans = input("A) Lahore  B) Islamabad : ")
if ans == "B":
    print("Correct!\n")
else:
    print("Wrong! Answer: B\n")


print("Q2: 2 + 2 = ?")
ans = input("A) 3  B) 4 :")
if ans == "B":
    print("Correct!\n")
else:
    print("Wrong! Answer: B\n")


print("Q3: What is 5 x 5?")
ans = input("A) 20  B) 25 :")
if ans == "B":
    print("Correct!\n")
else:
    print("Wrong! Answer: B\n")


print("Q4: what's the Color of sky?")
ans = input("A) Red  B) Blue :")
if ans == "B":
    print("Correct!\n")
else:
    print("Wrong! Answer: B\n")


print("Q5: How many days in a week?")
ans = input("A) 5  B) 7 :")
if ans == "B":
    print("Correct!\n")
else:
    print("Wrong! Answer: B\n")


print("Q6: How many months in a year?")
ans = input("A) 10  B) 12 :")
if ans == "B":
    print("Correct!\n")
else:
    print("Wrong! Answer: B\n")


#ATM Simulation

balance = 5000

pin = input("PIN: ")

if pin == "1234":
    select= input("1)Balance 2)Deposit 3)Withdraw : ")

    if select == "1":
        print("Balance:", balance)

    if select == "2":
        balance = balance + int(input("Amount: "))
        print("Balance:", balance)

    if select == "3":
        amount = int(input("Amount: "))
        if amount > balance:
            print("Not enough!")
        else:
            balance = balance - amount
            print("Balance:", balance)
else:
    print("Wrong PIN!")   
