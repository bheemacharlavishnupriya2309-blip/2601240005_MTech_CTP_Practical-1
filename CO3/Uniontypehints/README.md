**Description**

PEP 604 introduced a simpler syntax for expressing union types using the | operator.

A customer contact can be either a mobile number represented by str or an email address represented by str. The union syntax is useful when a value can have more than one possible type.

For different data types, the syntax can be written as:

int | str

This means the value can be either an integer or a string.

**Syntax**

PEP 604 Union Syntax

variable: type1 | type2

Function Syntax

def function_name(value: type1 | type2) -> return_type:
    # function body

**Algorithm**

Define a customer contact variable.

Allow the contact to have one of the specified types using the | operator.

Create a function to process the contact information.

Check the provided contact value.

Identify whether it represents a mobile number or an email address.

Display the customer contact.

End the program.

**Example**

def set_contact(contact: int | str) -> None:
    print("Primary Contact:", contact)


set_contact(9876543210)
set_contact("customer@example.com")

**Key Point**

PEP 604 makes union type annotations shorter and easier to read.

Traditional syntax:

from typing import Union

contact: Union[int, str]

PEP 604 syntax:

contact: int | str
