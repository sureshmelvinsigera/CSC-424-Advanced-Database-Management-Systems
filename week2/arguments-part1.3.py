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
}


def load_student(**kwargs):
    for key, values in kwargs.items():
        print('\n')
        for value in values:
            print(values[value])


load_student(data=students)
