# In this exercise we generate standardized usernames, emails, and security IDs using string slicing, indexing, and case formatting.
import email

print("=== USER ACCOUNT GENERATOR ===")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = input("Enter your birth year: ")

first_letter = first_name[0].lower()
first_name = first_name.lower()
last_name = last_name.lower()
last_digits = birth_year[2:]

print("")
print("-" * 40)

username = first_letter + last_name + last_digits
print(f"Username: {username}")

email = print(f"Email: {first_name} {last_name} @gmail.com" .replace(" ", ""))

first_name_3 = first_name[:3].upper()
last_name_3 = last_name[-3:].upper()

badge_id = (f" {first_name_3} {last_name_3} {birth_year}" .replace(" ", ""))
print(f"Badge ID: {badge_id}")
print("-" * 40)
