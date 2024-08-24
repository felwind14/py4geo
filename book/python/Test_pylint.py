"""Example of how to use pylint"""
class MyPerson:
    """Hola
    """
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.asked_for_name = False

    def getname(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        self.asked_for_name = True
        return self.name

print(MyPerson("Mike", 20, "m").getname())
