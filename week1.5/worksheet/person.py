# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self, name : str, birth : date):
        """
        constructs a person object given a name and date of birth
        """

        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(birth, date):
            raise TypeError("birth must be a date")

        if len(name) == 0:
            raise ValueError("name must not be empty")

        self.name = name
        self.birth = birth
        
    def initials(self) -> str:
        """
        returns a string containing the initials of the person
        """

        return ''.join([name[0].capitalize() for name in self.name.split(' ')])

    def is_birthday(self) -> bool:
        """
        returns true if today is persons birthday
        """

        return date.today().month == self.birth.month and date.today().day == self.birth.day

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

#p = Person("Johnny Testcase", date.today())
#print(p.is_birthday())
#
#p = Person("Johnny Testcase", date.fromisoformat("2026-11-05"))
#print(p.is_birthday())
#
#p = Person("Johnny Testcase", date.fromisoformat("2025-11-04"))
#print(p.is_birthday())