class dog:
    def __init__(self, name, age, country, life, eat, owner, likes, likestwo):
        '''Constructor'''
        self.name = name
        self.age = age
        self.country = country
        self.life = life
        self.eat = eat
        self.owner = owner
        self.likes = likes
        self.likestwo = likestwo

    def print_info(self):
        print(f'My name is {self.name}. I am {self.age} years old. I am from {self.country}, and yes, '
              f'I am a talking dog! My life is {self.life}! I am fed {self.eat} times a day. '
              f'My owner`s name is {self.owner} and I love her! I like {self.likes} and {self.likestwo}!')

DogLife = dog('Fluffy', 2, 'Ukraine', 'amazing', 3, 'Margo', 'walking the streets', 'playing with the ball')

(DogLife.print_info())
