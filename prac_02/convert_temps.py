def convert_celsius(fahrenheit):
    return fahrenheit*(9/5)+32
def convert_fahrenheit(celsius):
    return (celsius-32)*(5/9)

def main():

    in_file = open("temps_input.txt", "r")
    line = in_file.readlines()
    in_file.close()



    out_file = open('temps_output.txt', 'a')
    for x in range(len(line)):
        out_file.write()

    out_file.close()
main()