#This exercise will simulation a bill in the restaurant

import math

bill = input("How much was the restaurant bill? ")
people = input("How many people to split the bill? ")
bill_float = float(bill)
people_int = int(people)
split = bill_float / people_int

print(f"The exact price for each person is: {split:.2f}, and the price rounded "
      f"up is: {math.ceil(split)}")
