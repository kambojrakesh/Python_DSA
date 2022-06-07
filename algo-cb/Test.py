
def binary_search(numbers_list, no):
    left_index = 0
    middle_index = 0
    right_index = 0
    
    while left_index <= right_index:
        
        middle_index = (left_index + right_index) // 2    
        if no == numbers_list[middle_index]:
            return middle_index
            
        if no < numbers_list[middle_index]:
            right_index = middle_index - 1
            
        if no > numbers_list[middle_index]:
            left_index = left_index + 1

    return -1
        



if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 20

    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search")