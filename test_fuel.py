from fuel import convert, gauge
def main():
    test_ConvertInputs()
    test_GaugeInputs()


def test_ConvertInputs():
    #test upper bound values--------------------------------------//
    try:
        assert convert("100/100") == 100
    except AssertionError:
        print("this output is incorrect. it should be = 100")

    try:
        assert convert("99/100") == 99
    except AssertionError:
        print("this output is incorrect. it should be = 99")


    #test lower boundary values------------------------------------//
    try:
        assert convert("1/100") == 1
    except AssertionError:
        print("this output is incorrect. it should be = 1")
    
    try:
        assert convert("0/100") == 0
    except AssertionError:
        print("this output is incorrect. it should be = 0")


    #test valid inputs-----------------------------------------------//
    try:
        assert convert("49/49") == 100
    except AssertionError:
        print("this output is incorrect. it should be = 100")
    
    try:
        assert convert("0/32") == 0
    except AssertionError:
        print("this output is incorrect. it should be = 0")

    try:
        assert convert("3/4") == 75
    except AssertionError:
        print("this output is incorrect. it should be = 75")

    try:
        assert convert("1/4") == 25
    except AssertionError:
        print("this output is incorrect. it should be = 25")

    try:
        assert convert("1/2") == 50
    except AssertionError:
        print("this output is incorrect. it should be = 50")
    
    try:
        assert convert("24/80") == 30
    except AssertionError:
        print("this output is incorrect. it should be = 30") 
    
    
    #test with rounding required----------------------------------------//
    try:
        assert convert("47/48") == 98
    except AssertionError:
        print("this output is incorrect. it should be = 98")
    
    try:
        assert convert("8/66") == 12
    except AssertionError:
        print("this output is incorrect. it should be = 12")
    

    #test with input errors---------------------------------------------//
    try:
        assert convert("49/48") == "there is a problem with your input. please check and try again"
    except AssertionError:
        print("this output is incorrect. it should be = there is a problem with your input. please check and try again")

    try:
        assert convert("49/0") == "there is a problem with your input. please check and try again"
    except AssertionError:
        print("this output is incorrect. it should be = there is a problem with your input. please check and try again")

    try:
        assert convert("-1/4") == "there is a problem with your input. please check and try again"
    except AssertionError:
        print("this output is incorrect. it should be = there is a problem with your input. please check and try again")

    try:
        assert convert("1/-4") == "there is a problem with your input. please check and try again"
    except AssertionError:
        print("this output is incorrect. it should be = there is a problem with your input. please check and try again")

    try:
        assert convert("h/4") == "there is a problem with your input. please check and try again"
    except AssertionError:
        print("this output is incorrect. it should be = there is a problem with your input. please check and try again")

    try:
        assert convert("1/h") == "there is a problem with your input. please check and try again"
    except AssertionError:
        print("this output is incorrect. it should be = there is a problem with your input. please check and try again")

def test_GaugeInputs():
    #any invalid entries would have been wweeded out by now so there is no need to test for invalid inputs just for the boundaries of what is outputted at different values
    #lower bound tests-----------------------------------------//
    try:
        assert gauge(0) == "E"
    except AssertionError:
        print("this output is incorrect. it should be = E")

    try:
        assert gauge(1) == "E"
    except AssertionError:
        print("this output is incorrect. it should be = E")

    try:
        assert gauge(2) == "2%"
    except AssertionError:
        print("this output is incorrect. it should be = 2%")
    
    #upper bound tests ----------------------------------------//
    try:
        assert gauge(100) == "F"
    except AssertionError:
        print("this output is incorrect. it should be = F")
    
    try:
        assert gauge(99) == "F"
    except AssertionError:
        print("this output is incorrect. it should be = F")
    
    try:
        assert gauge(98) == "98%"
    except AssertionError:
        print("this output is incorrect. it should be = 98%")
    
    #valid middle range values---------------------------------//
    try:
        assert gauge(50) == "50%"
    except AssertionError:
        print("this output is incorrect. it should be = 50%")

    try:
        assert gauge(84) == "84%"
    except AssertionError:
        print("this output is incorrect. it should be = 84%")

    try:
        assert gauge(37) == "37%"
    except AssertionError:
        print("this output is incorrect. it should be = 37%")


if __name__ == "__main__":
    main()

