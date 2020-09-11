def return_10():
    return 10 

def add(number_1, number_2) :
    add_result = number_1 + number_2
    return add_result 

def subtract(number_1, number_2):
    subtract_result = number_1 - number_2
    return subtract_result

def multiply(number_1, number_2):
    multiply_result = number_1 * number_2
    return multiply_result

def divide(number_1, number_2):
    divide_result = number_1 / number_2
    return divide_result

def length_of_string(test_string):
    return len(test_string)

def join_string(string_1, string_2):
    return string_1 + string_2 

def add_string_as_number(string_1, string_2):
    return int(string_1) + int (string_2)

def number_to_full_month_name(month):
    year = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return year[month]

def number_to_short_month_name(month):
    year = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    chosen_month = year[month]
    return chosen_month[0:3]

def volume_of_cube(length):
    volume = length ** 3
    return volume

def reverse_string(string_1):
    return string_1[::-1]

def farenheit_to_celsius(temp):
    return (temp - 32) * 5/9