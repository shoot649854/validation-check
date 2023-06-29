from validation import * 


def test_answer():
    val = Validation()
    assert val.add(3, 2) == 5