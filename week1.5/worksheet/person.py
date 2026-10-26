# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self, name : str, birth : date):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(name, date):
            raise TypeError("birth must be a date")

        if len(name) == 0:
            raise ValueError("name must not be empty")

        self.name = name
        self.birth = birth
        
    def initials(self) -> str:
        """
        returns a string containing the initials of the person
        """

        return [name[0].capitalize() for name in self.name.split(' ')]

    def is_birthday(self) -> bool:
        """
        returns true if today is persons birthday
        """

        return self.birth == date.today()



    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
