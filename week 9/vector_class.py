class NotDefinedVectorOperationError(Exception):
    """
    Exception raised if mathematical operation not defined.

    Attributes:
        operation -- the operation not defined
        message -- the message displayed
    """

    def __init__(self, operation, message='{} operation in not defined in this circumstance'):
        self.salary = operation
        self.message = message.format(operation)
        super().__init__(self.message)


class Vector(object):
    """
    Vector class

    Operations:
        Vector addition (and subtractions) for vectors with the same dimension:
            Vector(1, 2, 3) + Vector(4, 5, 6) => Vector(5, 7, 9)
            Vector(1, 2) + Vector(1, 2, 3) => Exception: NotDefinedVectorOperationError

        Vector dot product for vectors with the same dimension:
            Vector(1, 2, 3) * Vector(4, 5, 6) => 32.0
            Vector(1, 2) * Vector(1, 2, 3) => Exception: NotDefinedVectorOperationError

        Vector cross product for vectors with dimension equal to 3:
            Vector(1, 2, 3) @ Vector(4, 5, 6) => Vector(-3, 6, -3)
            Vector(1, 2) @ Vector(3, 4) => Exception: NotDefinedVectorOperationError

        Multiplication of a Vector by a real value:
            Vector(1, 2, 3) * 3 => Vector(3, 6, 9)

        Absolute value of vector:
            abs(Vector(1, 2, 3)) => 3.7416573867739413
    """

    def __init__(self, *args):
        self.dimension = len(args)
        self.coordinates = list(args)

    def __str__(self):
        return '║' + ', '.join([str(elen) for elen in self.coordinates]) + '║'

    def __repr__(self):
        return 'Vector({})'.format(', '.join([str(elen) for elen in self.coordinates]))

    def __add__(self, other):
        # vector addition
        if other.dimension == self.dimension:
            output = [c_1 + c_2 for c_1, c_2 in zip(self.coordinates, other.coordinates)]
            return Vector(*output)
        else:
            raise NotDefinedVectorOperationError('Vector addition')

    def __sub__(self, other):
        # vector addition
        if other.dimension == self.dimension:
            output = [c_1 - c_2 for c_1, c_2 in zip(self.coordinates, other.coordinates)]
            return Vector(*output)
        else:
            raise NotDefinedVectorOperationError('Vector addition')

    def __mul__(self, other):
        # vector dot product
        if isinstance(other, Vector):
            if other.dimension == self.dimension:
                output = 0.
                for i in range(self.dimension):
                    output += self.coordinates[i] * other.coordinates[i]
                return output
            else:
                raise NotDefinedVectorOperationError('Vector dot product')
        elif isinstance(other, float) or isinstance(other, int):
            return Vector(*[self.coordinates[i] * other for i in range(self.dimension)])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __matmul__(self, other):
        # vector cross product
        if self.dimension == 3 and other.dimension == 3:
            c_1 = self.coordinates
            c_2 = other.coordinates
            det_1 = c_1[1] * c_2[2] - c_1[2] * c_2[1]
            det_2 = c_1[2] * c_2[0] - c_1[0] * c_2[2]
            det_3 = c_1[0] * c_2[1] - c_1[1] * c_2[0]
            return Vector(det_1, det_2, det_3)
        else:
            raise NotDefinedVectorOperationError('Vector cross product', message='{} not defined for dimension number '
                                                                                 'other than 3')

    def __abs__(self):
        # length of vector
        output = 0
        for i in range(self.dimension):
            output += self.coordinates[i] ** 2
        return output ** 0.5

    def __len__(self):
        # dimension of the vector
        return self.dimension

    def collinear(self, other):
        if abs(self @ other) == 0:
            return True
        else:
            return False


a = Vector(1, 2, 3)
b = Vector(4, 5, 6)
print(Vector())
