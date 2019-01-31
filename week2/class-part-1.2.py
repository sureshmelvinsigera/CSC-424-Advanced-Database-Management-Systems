class Actor:
    def __init__(self, actor_name, actor_age, movie_list):
        print('Creating the actor profile')
        self.name = actor_name
        self.age = actor_age
        self.movies = movie_list

    def print_actor_information(self):
        print(self.name)
        print(self.age)
        for movie in self.movies:
            print(movie)
        print('\n===')

# creating actor objects
anthony = Actor('Anthony Hopkins', 81, ['Solace', 'Fracture'])
mark = Actor('Mark Wahlberg', 47, ['Mile 22', 'Ted'])
ed = Actor('Ed Harris', 68, ['A Beautiful Mind', 'Apollo 13'])
harrison = Actor('Harrison Ford', 76, ['Cowboys & Aliens', 'Morning Glory'])

anthony.print_actor_information()
mark.print_actor_information()
ed.print_actor_information()
harrison.print_actor_information()
