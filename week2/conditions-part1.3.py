def get_letter_grade(scores):
    if scores >= 90 and scores <= 100:
        return 'A'
    elif scores >= 80 and scores <= 89:
        return 'B'
    elif scores >= 70 and scores <= 79:
        return 'C'
    elif scores >= 60 and scores <= 69:
        return 'D'
    elif scores >= 50 and scores <= 59:
        return 'E'
    else:
        return 'F'


score = get_letter_grade(67)
print('Grade is ', score)
