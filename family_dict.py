# Define a dictionary that contains info about several members of your family.
my_family = {
    'mom': {
        'name': 'Kathy',
        'age': 67
    },
    'sister': {
        'name': 'Rachel',
        'age': 32
    },
    'girlfriend': {
        'name': 'Jenn',
        'age': 30
    },
    'niece': {
        'name': 'Layla',
        'age': 8
    },
    'nephew': {
        'name': 'Tanner',
        'age': 6
    }
}

# Using a dictionary comprehension, produce output that looks like the following: Rachel is my sister and is 32 years old

family_stuff = {f"{member_values['name']} is my {family_member} and is {str(member_values['age'])} years old" for (family_member, member_values) in my_family.items()}

print(family_stuff)