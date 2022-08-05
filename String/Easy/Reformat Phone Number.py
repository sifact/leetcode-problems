def reformatNumber(number):

    output = []
    number = number.replace(' ', '').replace('-', '')

    i = 0
    while i < len(number):
        if i + 4 == len(number):
            output.append(number[i:i + 2])
            i += 2
        elif i + 3 <= len(number):
            output.append(number[i:i + 3])
            i += 3
        else:
            output.append(number[i:i + 2])
            i += 2

    return "-".join(output)


string = input()
print(reformatNumber(string))
