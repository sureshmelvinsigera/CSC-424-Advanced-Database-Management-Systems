def load_grades(a, b, c, *args):
    print(a)
    print(b)
    print(c)
    print(args)


grades = [10, 20, 60, 90, 50]
load_grades(*grades)
