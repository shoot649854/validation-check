from validation import * 


def main():
    val = Validation()
    assert val.add(3, 2) == 4

def test_is_prime():
    val = Validation()
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

if("__name__" == "__main__"):
    main()