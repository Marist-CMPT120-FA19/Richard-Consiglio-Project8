def main():
    heating = 0
    cooling = 0
    count = 0
    while count < 5:
        temp = int(input("What is the temperature"))
        c=0
        h=0
        count += count
    
        if temp <= 60:
            c = 60-temp
            cooling = cooling - c 
            
        elif temp >= 80:
             h = temp-80
             heating = heating + h

        elif speed > limit:
            print ("this is in range and will not count for cooling or heating")

        print ("your total cooling temperature below 60 is", cooling)
        print ("your total heating temperature above 80 is", heating)
        print ("your total between the two temps is", cooling + heating)


main()
