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
        },
    5:
        {
            'name': 'Jane',
            'gpa': 3.7,
            'Major': 'CSI',
            'Minor': 'ISI',
            'classes_taken': ('CSC126', 'CSC211', 'CSC326', 'CSC330', 'CSC490')
        }
}

# print(students[1]['name'], students[1]['gpa'])
# print(students[2]['name'], students[2]['gpa'])

good_students = []

for key, values in students.items():
    # print('key : ', key)
    if values['gpa'] > 3.0:
        # print('firing if key : ', key)
        good_students.append(values['name'])

print('Students with gpa > 3.0')
for i in good_students:
    print(i)
