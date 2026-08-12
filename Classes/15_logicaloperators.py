# Logical operators are used to combine multiple conditional statements.

high_income = True
good_credit = True
student = False

# 1. AND operator (Both conditions must be True)
if high_income and good_credit:
    print("Eligible for loan")

# 2. OR operator (At least one condition must be True)
if high_income or good_credit:
    print("Eligible for secondary loan")

# 3. NOT operator (Inverts the boolean value)
if not student:
    print("Not a student - standard rate applies")

# Combining multiple logical operators
if (high_income or good_credit) and not student:
    print("Fully eligible")

#Logical operators in python are like a circuit 