customer = {
    "name": "John Smith",
    "age": 22,
    "is_verified": True
}
print(customer["name"])
print(customer.get("age"))
print(customer.get("birthdate"))
customer["name"] = "Jack Smith"
print(customer["name"])
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)
