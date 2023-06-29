from validation import * 
val = Validation()

class test_case:
    def test_add():
        # Integer addition
        assert val.add(3, 2) == 5
        assert val.add(-5, 10) == 6
        assert val.add(0, 0) == 0
        
        # Float addition
        assert val.add(3.5, 2.1) == 5.6
        assert val.add(-1.5, 2.5) == 1.0
        assert val.add(0.0, 0.0) == 0.0
        
        # String concatenation
        assert val.add("Hello", "World") == "HelloWorld"
        assert val.add("Open", "AI") == "OpenAI"
        
        # Mixed types
        assert val.add(5, 2.5) == 7.5
        assert val.add("The answer is ", 42) == "The answer is 42"

    def test_sub():
        # Integer subtraction
        assert val.sub(3, 2) == 1
        assert val.sub(10, 5) == 5
        assert val.sub(0, 0) == 0
        
        # Float subtraction
        assert val.sub(3.5, 2.1) == 1.4
        assert val.sub(5.5, 1.5) == 4.0
        assert val.sub(0.0, 0.0) == 0.0
        
        # Mixed types
        assert val.sub(5, 2.5) == 2.5
        assert val.sub(10, "3") == 7

    def test_mult():
        # Integer multiplication
        assert val.mult(3, 2) == 6
        assert val.mult(-5, 10) == -50
        assert val.mult(0, 5) == 0
        
        # Float multiplication
        assert val.mult(3.5, 2.0) == 7.0
        assert val.mult(-1.5, 2.5) == -3.75
        assert val.mult(0.5, 0.5) == 0.25
        
        # String repetition
        assert val.mult("Hello", 3) == "HelloHelloHello"
        assert val.mult("Open", 2) == "OpenOpen"
        
        # Mixed types
        assert val.mult(5, 2.5) == 12.5
        assert val.mult("Repeat ", 3) == "Repeat Repeat Repeat "

    def test_div():
        # Integer division
        assert val.div(10, 2) == 5
        assert val.div(7, 3) == 2
        assert val.div(15, 5) == 3
        
        # Float division
        assert val.div(10.0, 2.5) == 4.0
        assert val.div(7.5, 3.0) == 2.5
        assert val.div(15.0, 4.0) == 3.7
        
        # Division by zero
        try:
            val.div(10, 0)
            assert False  # Division by zero should raise an exception
        except ZeroDivisionError:
            assert True  # Division by zero raises ZeroDivisionError
        
        try:
            val.div(7.5, 0.0)
            assert False  # Division by zero should raise an exception
        except ZeroDivisionError:
            assert True  # Division by zero raises ZeroDivisionError

    def test_is_prime():
        assert not val.is_prime(1)
        assert val.is_prime(2)
        assert val.is_prime(3)
        assert not val.is_prime(4)
        assert val.is_prime(5)
        assert not val.is_prime(6)
        assert val.is_prime(7)
        assert not val.is_prime(8)
        assert not val.is_prime(9)
        assert not val.is_prime(10)
