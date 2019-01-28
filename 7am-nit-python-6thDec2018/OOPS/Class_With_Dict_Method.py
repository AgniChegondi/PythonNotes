class Person:
    def __init__(self, ok):
        self.id = ok


obama = Person(100)

help(obama.__dict__)

obama.__dict__['age'] = 49
print(obama.__dict__)
print(obama.age+len(obama.__dict__))
