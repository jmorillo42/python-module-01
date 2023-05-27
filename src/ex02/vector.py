from __future__ import annotations
import typing
import sys

sys.tracebacklimit = 0


class Vector:
    def __init__(self, values):
        self.values: typing.List[typing.List[float]] = []
        if isinstance(values, int):
            if values <= 0:
                raise AssertionError('Initialize Vector with an integer greater than zero')
            self.values = [[float(i)] for i in range(values)]
        elif isinstance(values, tuple):
            if len(values) != 2 or not isinstance(values[0], int) or not isinstance(values[1], int) \
                    or values[1] <= values[0]:
                raise AssertionError('Initialize Vector with a tuple of two integers where the first one is greater \
than the second one')
            self.values = [[float(i)] for i in range(values[0], values[1])]
        elif isinstance(values, list) and all(isinstance(i, list) for i in values):
            if (len(values) == 1 and all(isinstance(i, float) for i in values[0])) \
                    or (len(values) > 1 and all(len(l) == 1 and isinstance(l[0], float) for l in values)):
                self.values = values
            else:
                raise AssertionError('Initialize Vector with a list of a list of floats or a list of lists of single \
float')
        else:
            raise AssertionError('Initialize Vector with an integer, a tuple of two integers or a list of list of \
floats')
        self.shape: typing.Tuple[int, int] = (len(self.values), len(self.values[0]))

    def dot(self, other):
        """produces a dot product between two vectors of same shape"""
        if self.shape != other.shape:
            raise AssertionError('Vectors must have the same shape')
        if self.shape[0] == 1:
            return sum([i * j for i, j in zip(self.values[0], other.values[0])])
        else:
            return sum([i * j for i, j in zip(self.T().values[0], other.T().values[0])])

    def T(self) -> Vector:
        """returns the transpose vector (i.e. a column vector into a row vector, or a row vector into a column vector)"""
        if self.shape[0] == 1:
            return Vector([[n] for n in self.values[0]])
        else:
            return Vector([[n[0] for n in self.values]])

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return self.__str__()

    # add & radd : only vectors of same shape.
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise AssertionError('Operation add must have two vectors')
        elif self.shape != other.shape:
            raise AssertionError('Vectors must have the same shape')
        if self.shape[0] == 1:
            return Vector([[self.values[0][i] + other.values[0][i] for i in range(self.shape[1])]])
        else:
            return Vector([[self.values[i][0] + other.values[i][0]] for i in range(self.shape[0])])

    def __radd__(self, other):
        self.__add__(other)

    # sub & rsub: only vectors of same shape.
    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise AssertionError('Operation sub must have two vectors')
        elif self.shape != other.shape:
            raise AssertionError('Vectors must have the same shape')
        if self.shape[0] == 1:
            return Vector([[self.values[0][i] - other.values[0][i] for i in range(self.shape[1])]])
        else:
            return Vector([[self.values[i][0] - other.values[i][0]] for i in range(self.shape[0])])

    def __rsub__(self, other):
        self.__sub__(other)

    # truediv : only with scalars (to perform division of Vector by a scalar).
    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise AssertionError('Operation div must have a scalar')
        if self.shape[0] == 1:
            return Vector([[self.values[0][i] / other for i in range(self.shape[1])]])
        else:
            return Vector([[self.values[i][0] / other] for i in range(self.shape[0])])

    # rtruediv : raises an NotImplementedError with the message "Division of a scalar by a Vector is not defined here."
    def __rtruediv__(self, other):
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

    # mul & rmul: only scalars (to perform multiplication of Vector by a scalar).
    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise AssertionError('Operation mult must have a scalar')
        if self.shape[0] == 1:
            return Vector([[self.values[0][i] * other for i in range(self.shape[1])]])
        else:
            return Vector([[self.values[i][0] * other] for i in range(self.shape[0])])

    def __rmul__(self, other):
        return self.__mul__(other)
