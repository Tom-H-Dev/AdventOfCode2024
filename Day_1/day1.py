#gen context
#pun left list of numbers in a int array and put right list in an int array\
#sort array by numerical order
#loop throuh all the values of the array get x value from list 1 and list 2
#subtract the values
#outcome add to total

def main():
    file =  open("Day_1/day1_context.txt", "r")
    #get line by line first add to left array
    #if the length of the first array is longer 
    # than the second put it in second
    left_array = []
    right_array = []
    total_value = 0
    
    temp = ''
    for line in file:
        last_char = ''
        line_array = [char for char in line]
        
        for char in line_array:
            if char.isnumeric():
                if last_char == ' ':
                    temp = ''
                    
                temp += char

            elif char == ' ' or char == '\n':
                if last_char.isnumeric():
                    if len(left_array) > len(right_array):
                        right_array.append(temp)
                    else: left_array.append(temp)
                temp = ''
            last_char = char
    right_array.append(temp)
    left_array = sorted(left_array)
    right_array = sorted(right_array)

    for i in range(len(left_array)):
        temp_val = int(left_array[i]) - int(right_array[i])
        if temp_val < 0:
            temp_val *= -1
        total_value += temp_val
    total_value = 0
    times_array = []

    times_array = count_and_add_matches(left_array, right_array)

    for number in left_array:
        total_value +=  int(number) * int(times_array.count(number))
    print(total_value)
            
def count_and_add_matches(left_array, right_array):
    left_set = set(left_array)
    matches = []
    for num in right_array:
        if num in left_set:
            matches.append(num)
    return matches




if __name__ == "__main__":
    main()