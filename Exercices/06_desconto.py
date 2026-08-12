# In this exercise we calculate product discounts, handle percentage arithmetic, and format currency outputs.

price = input("How much is the product price? ")
discount = input("How much is the discount price? ")
price_float = float(price)
discount_float = float(discount)

discount_amount = price_float * (discount_float / 100)
final_price = price_float - discount_amount

print(f"The original price was {price_float:.2f}, the discount amount was {discount_amount:.2f}, and the final price is {final_price:.2f}.")
