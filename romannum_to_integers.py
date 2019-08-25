#covert roman numerals to integers
import re
numbers = {
    "IV": 4,
    "VI": 6,
    "IX": 9,
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}


#  check if any letter occurs for more than 3 times
def occurs_morethan_3(input_string):
    for i in numbers:
        count = re.search(f"{i*4}", input_string)
        # if len(count) > 3:
        if count:
            print(f"{input_string} is invalid")
            quit()
    return False


def find_sum(input_string):
    sum = 0
    flag = 0
    # fetch each character from the input
    for i in range(0, len(input_string)):

        if flag:
            flag = 0
            continue
        # fetch the keys from the dictionary
        for j in numbers:
            # check for special cases values and add it to sum
            if i != len(input_string)-1 and input_string[i]+input_string[i+1] == j:
                sum += numbers[j]
                flag = 1
                break
            # find the value and add it to sum
            elif input_string[i] == j:
                sum += numbers[j]
                break

    print(sum)

# get input
input_string = input("Enter the roman number ")
# converting to uppercase
input_string = input_string.upper()
if not occurs_morethan_3(input_string):
    find_sum(input_string)


