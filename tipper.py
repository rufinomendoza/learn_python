#This is a tipper program

print("This is a program to help calculate your restaurant tip.")
bill = float(input("What is your restaurant bill? "))

fifteen = round(bill * .15,2)
twenty = round(bill * .20,2)


print("These should be your tips:")
print("\tFor 15%:", fifteen)
print("\tFor 20%:", twenty)

input("\n\nPress the enter key to exit.")
