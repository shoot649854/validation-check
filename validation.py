class Validation:
    def __init__(self) -> None:
        pass

    def add(a, b):
        return a + b
    
    def sub(a, b):
        return a - b
    
    def mult(a, b):
        return a * b
    
    def div(a, b):
        return a / b
    
    def is_prime(n: int) -> bool:
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