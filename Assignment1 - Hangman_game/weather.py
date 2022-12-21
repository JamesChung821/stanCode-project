"""
File: weather.py
Name: James Chung
-----------------
This program is utilized to record the weather.
"""

# Constant
PW = -100


def main():
    """
    This program is utilized to record the weather.
    """
    # Title
    print("stanCode \"Weather Master 4.0\"! ")

    # Enter an number
    weather = int(input("Next temperature: (or "+ str(PW) +" to quit)? "))

    #Set variable
    maximum = weather
    minimum = weather
    a = 0
    b = 0
    c = 0
    d = 0
    t = 0

    #Finish if entering the passward
    if weather == PW:
        print("No temperatures were entered.")

    #Record the weather
    else:
        while weather != PW:
            if weather > maximum:
                maximum = weather
                a += 1
            elif weather < minimum:
                minimum = weather
                b += 1
            else:
                c += 1
            if weather < 16:
                d += 1
            t += weather
            weather = int(input("Next temperature: (or "+ str(PW) +" to quit)? "))

        #Print the results
        print("Highest temperature = " + str(maximum))
        print("Lowest temperature = " + str(minimum))
        print("Average = " + str(float(t / (a + b + c))))
        print(str(d) + " cold day(s)")


######    DO NOT EDIT THE CODE BELOW THIS LINE    ######
if __name__ == '__main__':
    main()