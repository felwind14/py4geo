"""Example of how to use pylint"""


class MyPerson:
    """_summary_"""

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

NUM_POINTS = 120

ADD = 2


def example_function(x, y):
    """_summary_

    Args:
        x (_type_): _description_
        y (_type_): _description_

    Returns:
        _type_: _description_
    """
    return x + y
