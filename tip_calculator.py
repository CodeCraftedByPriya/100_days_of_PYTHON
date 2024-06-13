#TIP Calculator
bill = float(input("What is your bill in $"))
tip = float(input("How much are you willing to pay as tip:"))
no = int(input("How many are going to share the total bill:"))
total_bill = float(bill+tip)
total_amt = float((bill+tip)/no)
print("\nThe total bill including the tip is", total_bill,"\nThe amt that each should pay is", total_amt)
