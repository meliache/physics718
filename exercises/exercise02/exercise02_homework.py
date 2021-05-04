import unittest

from vector_2d import Vector2D


class Particle:
    def __init__(self, position, momentum, mass):
        """
        Ininitialise the particle with a position and momentum vectors and a mass
        """
        # self.... = ...
        raise NotImplementedError

    def get_velocity(self):
        """
        Return the velocity vector of the particle
        """
        raise NotImplementedError

    def get_energy(self):
        """
        Return kinetic enrgy of the particle
        """
        raise NotImplementedError

    # The ``@property`` modifies the function so that we can call it without the
    # parantheses, like a property, e.g. just ``particle.velocity``
    @property
    def velocity(self):
        # return ...
        raise NotImplementedError

    # TODO: create likewise an `energy` property method


class Complex:
    pass
    # implement all on your own


if __name__ == "__main__":
    unittest.main(module="test_exercise02_homework", verbosity=2)
