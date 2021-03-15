# Generics - defining a class that every type inherits and must conform to


class Applicable:

    def __init__(self, func):
        try:
            func.apply(1)
        
        except:
            print("This is not an applicable type!")