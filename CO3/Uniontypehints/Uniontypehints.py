def set_contact(contact: int | str) -> None:
    print("Primary Contact:", contact)


contact = input("Enter Mobile Number or Email: ")

if contact.isdigit():
    set_contact(int(contact))
else:
    set_contact(contact)
