students = {
    1:
        {
            'name': 'John',
            'gpa': 3.0,
            'classes_taken': ('490',)
        },
    2:
        {
            'name': 'Mike',
            'gpa': 2.0,
            'classes_taken': ('CSC211', 'CSC220', 'CSC326',)
        },
    3:
        {
            'name': 'Stacy',
            'gpa': 4.0,
            'Major': 'CS',
            'classes_taken': ('CSC126', 'CSC211', 'CSC326',)
        },
    4:
        {
            'name': 'Bruce',
            'gpa': 3.2,
            'Major': 'CSI',
            'Minor': 'ISI',
            'classes_taken': ('CSC211', 'CSC326',)
        },
    5:
        {
            'name': 'Jane',
            'gpa': 3.7,
            'major': 'CSI',
            'minor': 'ISI',
            'classes_taken': ('CSC126', 'CSC211', 'CSC326', 'CSC330', 'CSC490')
        }
}

for key, values in students.items():
    # print(type(key), type(values))
    for k, v in values.items():
        # print(k, values[k])
        if k == 'classes_taken':
            for i in values[k]:
                if i == 'CSC126':
                    print(values['name'])
