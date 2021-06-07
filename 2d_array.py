#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: June 2021
# This program uses a 2D array

import math
import random


def avg_of_numbers(my_numbers):
    # this function finds the averqge of elements in a 2D array

    sum_of_all_numbers = 0
    for first_dimension in my_numbers:
        for some_number in first_dimension:
            sum_of_all_numbers = sum_of_all_numbers + some_number

    average = sum_of_all_numbers / (len(my_numbers) * len
                                    (my_numbers[0]))

    return average


def main():
    # this function uses a 2D array
    my_numbers = []

    # input
    rows = int(input("How many row would you like: "))
    columns = int(input("How many columns would you like: "))

    for loop_counter_rows in range(0, rows):
        temp_column = []
        for loop_counter_columns in range(0, columns):
            a_random_number = random.randint(1, 50)
            temp_column.append(a_random_number)
            print("{0} ".format(a_random_number), end="")
        my_numbers.append(temp_column)
        print("")

    print("The average of all the numbers is: {0} "
          .format(avg_of_numbers(my_numbers)))


if __name__ == "__main__":
    main()
