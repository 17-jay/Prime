class bold :
    BOLD = '\033[1m'
    END = '\033[0m' #this one resets the boldness to normal

print(bold.BOLD + "Let's see how Fat you are" + bold.END)



Height = float(input("Enter Height in metres(2dp): "))
Weight = float(input("Enter Weight in Kilograms(2dp)"))

BMI = Weight/(Height*Height)
print("Your BMI is, " ,BMI)


if(BMI>0):
    if(BMI<=16):
        print("SEVERELY UNDERWEIGHT!!!")
    elif(BMI<=18.5):
        print("UNDERWEIGHT!!")
    elif(BMI<=25):
        print("HEALTHY HUMAN")
    elif(BMI<=30):
        print("Ayayai, OVERWEIGHT!!")
    else:
        print("SEVERELY OVERWEIGHT!!!")

else:
    print("Kindly enter the valid details ")