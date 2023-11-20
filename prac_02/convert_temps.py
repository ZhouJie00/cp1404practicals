def convert_celsius(fahrenheit):
    return fahrenheit*(9/5)+32
def convert_fahrenheit(celsius):
    return (celsius-32)*(5/9)

def main():

    in_file = open("temps_input.txt", "r")
    lines = in_file.readlines()
    in_file.close()

    split_lines =[]
    formated_lines=[]
    for line in lines:
        split_lines.append(line.split("\n"))


    for line in split_lines:
        formated_lines.append(line[0])

    print(formated_lines)

    #
    # out_file = open('temps_output.txt', 'a')
    # for i in range(len(line)):
    #     out_file.write()

    # out_file.close()
main()