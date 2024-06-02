#!/usr/bin/python3
"""IS DOCUMENTED"""


class SwimMixin():
    """IS DOCUMENTED"""

    def swim(self):
        print("The creature swims!")


class FlyMixin():
    """IS DOCUMENTED"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """IS DOCUMENTED"""

    def roar(self):
        print("The dragon roars!")
