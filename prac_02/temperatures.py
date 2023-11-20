
def convert_celsius(fahrenheit):
    return fahrenheit*(9/5)+32
def convert_fahrenheit(celsius):
    return (celsius-32)*(5/9)

def main():

    option = input("1.Convert to celsius\n2.Convert to fahrenheit\nselect an option: ")
    value = float(input("Enter the value: "))
    if option == "1":
        print("converted fahrenheit: "+str(convert_celsius(value)))
    elif option == "2":
        print("converted celsius: "+str(convert_fahrenheit(value)))


main()