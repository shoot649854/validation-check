from validation import * 


def main():
    val = Validation()
    assert val.add(3, 2) == 5

if("__name__" == "__main__"):
    main()