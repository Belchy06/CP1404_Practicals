"""CP1404 Practical - Programming language intermediate exercise"""


class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=False, year=""):
        """
        Initialize the class with the default values

        reflection = boolean
        """

        self.name = name.title()
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def __repr__(self):
        return "{}, {} Typing, Reflection = {}, First appeared in {}".format(self.name, self.typing,
                                                                             self.reflection, self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"
