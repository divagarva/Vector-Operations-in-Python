import numpy as np

class VectorOperations:
    def __init__(self, vector1, vector2):
        self.vector1 = np.array(vector1)
        self.vector2 = np.array(vector2)

    def scalar_multiplication(self, scalar):
        """
        Multiply a vector by a scalar.
        """
        scalar_mult_v1 = scalar * self.vector1
        scalar_mult_v2 = scalar * self.vector2
        return scalar_mult_v1, scalar_mult_v2

    def vector_sum(self):
        """
        Add two vectors.
        """
        if len(self.vector1) != len(self.vector2):
            raise ValueError("Vectors must be of the same length.")
        return self.vector1 + self.vector2

    def dot_product(self):
        """
        Compute the dot product of two vectors.
        """
        if len(self.vector1) != len(self.vector2):
            raise ValueError("Vectors must be of the same length.")
        return np.dot(self.vector1, self.vector2)

def main():
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]

    # Create an instance of the VectorOperations class
    vector_ops = VectorOperations(vector1, vector2)

    # Scalar multiplication
    scalar = 3
    scalar_mult_v1, scalar_mult_v2 = vector_ops.scalar_multiplication(scalar)
    print(f"Scalar multiplication of vector1 with {scalar}: {scalar_mult_v1}")
    print(f"Scalar multiplication of vector2 with {scalar}: {scalar_mult_v2}")

    # Vector sum
    vector_sum = vector_ops.vector_sum()
    print(f"Sum of vectors: {vector_sum}")

    # Dot product
    dot_prod = vector_ops.dot_product()
    print(f"Dot product of vectors: {dot_prod}")

if __name__ == "__main__":
    main()
