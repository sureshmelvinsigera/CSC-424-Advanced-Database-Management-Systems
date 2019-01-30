def load_cats(owner, *all_cats):
    print(owner, 'owns ')
    for cat in all_cats:
        print(cat)


def load_good_cats(owner, *arg):
    print(owner, 'owns ')
    for value in arg:
        print(value)


cats = ['Oscar', 'Max', 'Tiger', 'Sam', 'Misty', 'Simba', 'Coco', 'Chloe', 'Lucy', 'Molly']
load_cats('James', cats)
load_good_cats('James', cats)
