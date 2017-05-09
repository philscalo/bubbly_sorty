#!/usr/bin/env python

"""implement a simple sorting algorithm"""

# 1 - get input of 5 numbers into an array
# 2 - compare 1st number to 2nd number
# 3 - if greater, move slots; if less, leave
from sys import *


init_list = [10, 67, 34, 22, 108, 182, 2267, 2569, 2, 9, 65]


#TODO  change to take an input from stdin
#write a test to determine if array is out of order
#rerun test at completion of each step


def show_results():
    for item in init_list:
        print(item)


def check_order():
    for i in range(len(init_list) - 1):
        if init_list[i] > init_list[i + 1]:
            return 'Error - sequence unordered'
    return 'OK'


def bubble_it():
    global init_list
    global attempt_count
    attempt_count = 0
    for cnt in range(len(init_list)-1):
        for each_member in range(len(init_list)-1):
            if init_list[each_member]>init_list[each_member+1]:
                init_list[each_member], init_list[each_member + 1] = init_list[each_member + 1], init_list[each_member]
#            print(init_list)
#            print('Pass No. ' + str(each_member))
            x = check_order()

            attempt_count += 1
            if x == 'OK':
                print('ALL SET')
                print('final sequence order: ' + str(init_list))
                print('list resequenced in ' + str(attempt_count) + ' passes')
                return
            print(str(x))
        cnt += 1


if __name__ == '__main__':
    bubble_it()