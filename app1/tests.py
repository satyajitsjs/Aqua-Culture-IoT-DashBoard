# class Bank:
#     def __init__(self):
#         print("Choose any from the below choices\n")
#         print("Display the amount, press 1")
#         print("Deposite the amount, press 2")
#         print("Withdraw the amount,press 3\n")
#         self.choice = input("Enter your choice :")
    
#     def choices(self):
#         if self.choice == "1":
#             bank.show_balance()
#         elif self.choice == "2":
#             amount = int(input("Your deposited amount :"))
#             bank.deposite(amount)
#         else:
#             amount = int(input("Your withdraw amount :"))
#             bank.withdraw(amount)

#     def show_balance(self):
#         fr = open("Total amount.txt")
#         frr = fr.read()
#         print("My available balance :",frr)

#     def deposite(self,amount):
#         with open("Total amount.txt", "r+") as fr:
#             frr = fr.read()
#             if not frr:
#                 balance = amount + 0
#                 fr.write(str(balance))
#             else:
#                 balance = amount + int(frr)
#                 print(balance)
#                 fr.seek(0)
#                 fr.truncate()
#                 fr.write(str(balance))
#                 print("Your deposited amount : ",amount)
#                 print("Your total amount : ",balance)
    
#     def withdraw(self,amount):
#         with open("Total amount.txt","r+") as f:
#             frr = f.read()
#             balance = int(frr)-amount 
#             f.seek(0)
#             f.truncate()
#             f.write(str(balance))
#             # print("Your withdrawal amount : ",amount)
#             print("Your remaining amount : ",frr)

# bank = Bank()
# bank.choices()

# Import necessary modules
param = ['do','orp']
for i in param:
    if i == 'ph':
        print("hhhh")
