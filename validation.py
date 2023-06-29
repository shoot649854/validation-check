class Validation:
    def __init__(self) -> None:
        pass

    def add(self, a, b):
        if not (isinstance(a, str) and isinstance(b, str)):
            assert TypeError("Both 'a' and 'b' should be strings")
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mult(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a / b
    
    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False

        if n == 2:
            return True

        if n % 2 == 0:
            return False

        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2

        return True