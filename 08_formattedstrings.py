#To build a string we 2 values we can concatenate them with the +

first = "Tiago"
last = "Teixeira"
full = first + " " + last
print(full)

#But we can do it in a more professional and simple way
#The result will be the same but written better

first = "Tiago"
last = "Teixeira"
full = f"{first} {last}"
print(full)

#basically we can format strings whatever we want, we just need to
# put it between the braces {}
