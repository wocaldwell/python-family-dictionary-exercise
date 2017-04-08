my_family = {
    'sister': {
        'name': 'Krista',
        'age': 42
    },
    'mother': {
        'name': 'Cathie',
        'age': 70
    }
}

for member, value in my_family.items():
    print(member)
    for key, inner_value in value.items():
        print(inner_value)


family_relations = {value['name'] + ' is my ' + relation + ' and is ' + str(value['age']) + ' years old' for (relation, value) in my_family.items()}

print(family_relations)
