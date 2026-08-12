#In this exercise I will be formatting the name and creating an email

name = input("Enter your name: ")
clean_name = name.strip()
print(clean_name.title())
length = print(len(clean_name))

email_name = clean_name.lower().replace(" ", ".")
print(f"{email_name}" + "@gmail.com")
