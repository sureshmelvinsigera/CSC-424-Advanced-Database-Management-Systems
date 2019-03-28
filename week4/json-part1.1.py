student = {
    1: {
        'name': ' John',
        'age': 25,
        'position': 'software engineer'
    },
    2: {
        'name': ' Melvin',
        'age': 25,
        'position': 'intern'
    },
    3: {
        'name': ' Stacy',
        'age': 23,
        'position': 'software engineer'
    }
}

good_students = []

for key, values in student.items():
    if values['position'] == 'software engineer':
        print(values['name'])
