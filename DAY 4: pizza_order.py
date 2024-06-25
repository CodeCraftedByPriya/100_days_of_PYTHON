print("Thank you for choosing Python Pizza Deliveries!\nHere are the options to choose from\n\t\tSIZE : Small - S, Medium - M and Large - L\n\t\tTOPPINGS : Yes - Y and No - N")
print("COST\n\t\tSmall pizza (S): $15,\n\t\tMedium pizza (M): $20,\n\t\tLarge pizza (L): $25,\n\t\tAdd pepperoni for small pizza (Y or N): +$2,\n\t\tAdd pepperoni for medium or large pizza (Y or N): +$3,\n\t\tAdd extra cheese for any size pizza (Y or N): +$1")
size = input("What size pizza do you want? S, M, or L").upper()
add_pepperoni = input("Do you want pepperoni? Y or N").upper()
extra_cheese = input("Do you want extra cheese? Y or N").upper()

#for a small pizza
if size=='S':
  a=15
  if add_pepperoni=='Y' and extra_cheese == 'N':
    a += 2
  elif add_pepperoni=='Y' and extra_cheese == 'Y':
    a += 3
  elif add_pepperoni=='N' and extra_cheese == 'Y':
    a += 1
  else:
    a=15

#for a medium pizza
elif size=='M':
  a=20
  if add_pepperoni=='Y' and extra_cheese == 'N':
    a += 3
  elif add_pepperoni=='Y' and extra_cheese == 'Y':
    a += 4
  elif add_pepperoni=='N' and extra_cheese == 'Y':
    a += 1
  else:
    a=20

#for a large pizza
elif size=='L':
  a=25
  if add_pepperoni=='Y' and extra_cheese == 'N':
    a += 3
  elif add_pepperoni=='Y' and extra_cheese == 'Y':
    a += 4
  elif add_pepperoni=='N' and extra_cheese == 'Y':
    a += 1
  else:
    a=25

print(f'Your final bill is: ${a}.')
