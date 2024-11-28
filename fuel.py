def main():
    #ask the user for the fraction which is currently displayed on their fuel guage
    fraction = input("fuel guage reading: ")
    #conversion to a percentage
    percentage = convert(fraction)
    #if an error occured when converting to a percentage display error
    if percentage == "there is a problem with your input. please check and try again":
        print(percentage)
    #if no error occured converting to a percentage then run gauge to convert to displayable percentage value
    else:
        output = gauge(percentage)
        #print the result
        print(output)


def convert(fraction):
    percentage = ""
    try:
        # take fraction in string form and split into the numerator and denominator  
        numbers = fraction.split("/")
        #convert the numbers into integers and assign them to variables
        num1 = int(numbers[0])
        num2 = int(numbers[1])
        #recognise if the fraction entered is top heavy or a negative fraction and therefore invalid and catch this as an error
        if num1 > num2 or num1<0 or num2<0:
            raise ValueError
        #perform calculation to get the percentage equivalent of the fraction rounded to the nearest integer value
        percentage = round((num1/num2)*100)
    #display an error message if either numerator or denominator isnt a number or if the denominator is 0 or the fraction is top heavy
    except ValueError or ZeroDivisionError:
        percentage = "there is a problem with your input. please check and try again"
    return percentage



def gauge(percentage):
    #create a string of the percentage formatted correctly to display
    fuelAmount = str(percentage) + "%"
    #if the tank is classed as empty or full alter the display to show that
    if (percentage<=1):
        fuelAmount = "E"
    elif (percentage>=99):
        fuelAmount = "F"
    #return the final formatted display for the percentage fuel value
    return (fuelAmount)
        

#check if this is cuurrently the main program running or if it has been called and referanced by another file
if __name__ == "__main__":
    main()
