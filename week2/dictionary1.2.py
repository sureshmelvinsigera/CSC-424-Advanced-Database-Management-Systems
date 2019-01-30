students = {
    1:
        {
            'name': 'John',
            'gpa': 3.0,
            'classes_taken': ('CSC126', 'CSC211', 'CSC326')
        },
    2:
        {
            'name': 'Mike',
            'gpa': 2.0,
            'classes_taken': ('CSC126', 'CSC211', 'CSC326')
        },
    3:
        {
            'name': 'Stacy',
            'gpa': 4.0,
            'Major': 'CS',
            'classes_taken': ('CSC126', 'CSC211', 'CSC326')
        },
    4:
        {
            'name': 'Bruce',
            'gpa': 3.2,
            'Major': 'CSI',
            'Minor': 'ISI',
            'classes_taken': ('CSC211', 'CSC326')
        }
}

for key, values in students.items():
    print('\n')
    for value in values:
        print(values[value])
