def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be \"the number of odd elements in the
    string i of the input.\" where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ['the number of odd elements 4n the str4ng 4 of the 4nput.']
    >>> odd_count(['3',\"11111111\"])
    ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 8n the str8ng 8 of the 8nput.']
    """
    result = []
    for i, s in enumerate(lst):
        odd_count = 0
        for digit in s:
            if int(digit) % 2 != 0:
                odd_count += 1
        output_string = "the number of odd elements " + str(odd_count) + "n the str" + str(odd_count) + "ng " + str(odd_count) + " of the " + str(odd_count) + "nput."
        result.append(output_string)
    return result

def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:
    Input: arr = [-3, -4, 5], k = 3
    Output: [-4, -3, 5]

    Example 2:
    Input: arr = [4, -4, 4], k = 2
    Output: [4, 4]

    Example 3:
    Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
    Output: [2]

    Note:
     1. The length of the array will be in the range of [1, 1000].
     2. The elements in the array will be in the range of [-1000, 1000].
     3. 0 <= k <= len(arr)
    """
    if k == 0:
        return []  # Handle the case where k is 0

    # Sort the array in descending order
    arr.sort(reverse=True)

    # Return the first k elements
    return arr[:k]

from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes

def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + )
    Subtraction ( - )
    Multiplication ( * )
    Floor division ( // )
    Exponentiation ( ** ) 

    Example:
    operator=['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
    The length of operator list is equal to the length of operand list minus one.
    Operand is a list of of non-negative integers.
    Operator list has at least one operator, and operand list has at least two operands.
    """

    if len(operator) != len(operand) - 1:
        raise ValueError("Operator and operand lists have incorrect lengths.")
    
    expression = ""
    for i in range(len(operator)):
        expression += str(operand[i]) + operator[i]

    expression += str(operand[-1])  # Add the last operand

    try:
        result = eval(expression)
        return result
    except (SyntaxError, NameError, ZeroDivisionError) as e:
        raise ValueError(f"Invalid expression or operation: {e}")
    
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i
    return 1  # If no divisor is found, return 1 (which always divides n)

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return "0"
    
    digits = []
    while x > 0:
        remainder = x % base
        digits.insert(0, str(remainder))  # Prepend to maintain order
        x //= base
    return "".join(digits)

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    n = len(l)
    if n % 2 == 0:
        mid1 = l[n // 2 - 1]
        mid2 = l[n // 2]
        median = (mid1 + mid2) / 2
    else:
        median = l[n // 2]
    return median

def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x_str = str(x)
    n = len(x_str)
    shift = shift % n  # Handle shifts larger than the number of digits

    if shift == 0:
        return x_str  # No shift needed
    
    shifted_str = x_str[n - shift:] + x_str[:n - shift]
    return shifted_str

def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index. 

    Example 3:
        Input: []
        Output: []
    
    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest value, but  there are two zeros,
                     so we will choose the first zero, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """
    if not arr:
        return []

    smallest_even = float('inf')
    smallest_index = -1

    for i, val in enumerate(arr):
        if val % 2 == 0 and val < smallest_even:
            smallest_even = val
            smallest_index = i

    if smallest_index == -1:
        return []  # No even numbers found
    else:
        return [smallest_even, smallest_index]
    
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = "aeiouAEIOU"
    encoded_message = ""
    for char in message:
        if 'a' <= char <= 'z':
            if char in vowels:
                next_char = chr(((ord(char) - ord('a')) + 2) % 26 + ord('a'))
                encoded_message += next_char.upper()
            else:
                encoded_message += char.swapcase()
        elif 'A' <= char <= 'Z':
            if char in vowels:
                next_char = chr(((ord(char) - ord('A')) + 2) % 26 + ord('A'))
                encoded_message += next_char.lower()
            else:
                encoded_message += char.swapcase()
        else:
            encoded_message += char  # Handle non-alphabetic characters
    return encoded_message

def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """

    if not date:
        return False

    try:
        month, day, year = map(int, date.split("-"))
    except ValueError:
        return False

    if not (1 <= month <= 12):
        return False
    
    if not (1 <= day <= 31):
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2 and day > 29:
        return False  # Handle leap years later


    return True

def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".
    """
    start1, end1 = interval1
    start2, end2 = interval2

    # Find the intersection interval
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)

    if intersection_start > intersection_end:
        return "NO"  # No intersection

    length = intersection_end - intersection_start + 1

    if length <= 1:
        return "NO"  # Length 0 or 1 is not prime

    for i in range(2, int(length**0.5) + 1):
        if length % i == 0:
            return "NO"

    return "YES"

import heapq

def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    ... (rest of docstring)
    """

    rows, cols = len(grid), len(grid[0])
    queue = []
    visited = set()
    
    for r in range(rows):
        for c in range(cols):
            heapq.heappush(queue, ([grid[r][c]], r, c))  # ([path], row, col)


    while queue:
        path, row, col = heapq.heappop(queue)
        
        if len(path) == k:
            return path
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_path = path + [grid[nr][nc]]
                if tuple((nr, nc)) not in visited:
                    heapq.heappush(queue, (new_path, nr, nc))
                    visited.add(tuple((nr, nc)))

    return []  # Should not happen given the problem constraints

def is_nested(string):
    """
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    """
    count = 0
    nested = False
    for char in string:
        if char == '[':
            count += 1
            if count >= 2:
                nested = True
        elif char == ']':
            count -= 1
            if count < 0:
                return False  # Invalid subsequence
    return nested and count == 0  # Must be balanced and have nesting

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces(\"Example\") == \"Example\"
    fix_spaces(\"Example 1\") == \"Example_1\"
    fix_spaces(\" Example 2\") == \"_Example_2\"
    fix_spaces(\" Example   3\") == \"_Example-3\"
    """
    result = ""
    space_count = 0
    for char in text:
        if char == ' ':
            space_count += 1
            if space_count <= 2:
                result += "_"
            else:
                result += "-"
        else:
            result += char
            space_count = 0
    return result

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check(\"example.txt\") # => 'Yes'
    file_name_check(\"1example.dll\") # => 'No' (the name should start with a latin alphapet letter)
    """

    if "." not in file_name:
        return "No"

    parts = file_name.split(".")
    if len(parts) != 2:
        return "No"

    name_part = parts[0]
    ext_part = parts[1]

    digit_count = 0
    for char in name_part:
        if char.isdigit():
            digit_count += 1

    if digit_count > 3:
        return "No"

    if not name_part or not name_part[0].isalpha():
        return "No"

    if ext_part not in ['txt', 'exe', 'dll']:
        return "No"

    return "Yes"

def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    symbols = [ "m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i" ]
    
    roman_numeral = ""
    i = 0
    while number > 0:
        if values[i] <= number:
            roman_numeral += symbols[i]
            number -= values[i]
        else:
            i += 1
            
    return roman_numeral

def is_prime(num):
    """Helper function to check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    fib_list = []
    a, b = 1, 1
    count = 0

    while True:
        if is_prime(b):
            count += 1
            if count == n:
                return b
        a, b = b, a + b

def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    """
    letter_grades = []
    for grade in grades:
        if grade >= 4.0:
            letter_grades.append("A+")
        elif grade > 3.7:
            letter_grades.append("A")
        elif grade > 3.3:
            letter_grades.append("A-")
        elif grade > 3.0:
            letter_grades.append("B+")
        elif grade > 2.7:
            letter_grades.append("B")
        elif grade > 2.3:
            letter_grades.append("B-")
        elif grade > 2.0:
            letter_grades.append("C+")
        elif grade > 1.7:
            letter_grades.append("C")
        elif grade > 1.3:
            letter_grades.append("C-")
        elif grade > 1.0:
            letter_grades.append("D+")
        elif grade > 0.7:
            letter_grades.append("D")
        elif grade > 0.0:
            letter_grades.append("D-")
        else:
            letter_grades.append("E")
    return letter_grades

def closest_integer(value):
    """
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    """
    try:
        num = float(value)
        lower = int(num)
        upper = lower + 1 if num >= 0 else lower - 1
        
        if abs(num - lower) <= abs(num - upper):
            return lower
        else:
            return upper

    except ValueError:
        return "Invalid input"
    
def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """

    if not arr:
        return []

    numbers_to_names = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    filtered_arr = [num for num in arr if 1 <= num <= 9]
    filtered_arr.sort()
    filtered_arr.reverse()

    result = [numbers_to_names[num] for num in filtered_arr if num in numbers_to_names]

    return result

def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).

    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """

    vowels = "AEIOUaeiou"
    
    # Check for empty or single-character words
    if len(word) <= 1:
        return ""

    for i in range(len(word) - 2, -1, -1):  # Iterate from second-to-last character
        char = word[i]
        
        # Check if current character is a vowel
        if char in vowels:
          
            # Check if the character before and after are consonants.
            prev_char = word[i-1] if i > 0 else None
            next_char = word[i+1] if i < len(word) - 1 else None

            if prev_char and next_char and (prev_char not in vowels and next_char not in vowels) :
                return char
    return ""

def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    total_sum = 0
    for i in range(k):
        num = arr[i]
        if abs(num) >= 10 and abs(num) < 1000:
            total_sum += num
        elif 0 < abs(num) < 10 : #Adding explicit check for single digit numbers
            total_sum += num
    return total_sum

import math

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    total_sum = 0
    for num in lst:
        ceiling_num = math.ceil(num)
        total_sum += ceiling_num * ceiling_num
    return total_sum

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))  # Use absolute value to handle negative numbers
            if len(num_str) > 1:
                if int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
                    count += 1
    return count

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    common_elements = set()
    for element in l1:
        if element in l2:
            common_elements.add(element)
    return sorted(list(common_elements))

import math

def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    
    if a + b <= c or a + c <= b or b + c <= a:
        return -1

    # Heron's formula
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return round(area, 2)

def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    if a < 1:
        return False
    
    prime_factors = []
    i = 2
    while i * i <= a:
        if a % i == 0:
            prime_factors.append(i)
            while a % i == 0:
                a //= i
        i += 1
    if a > 1:
        prime_factors.append(a)

    return len(prime_factors) == 3 and all(is_prime(factor) for factor in prime_factors)

def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            shifted_char = chr(((ord(char) - ord('a') + 4) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            shifted_char = chr(((ord(char) - ord('A') + 4) % 26) + ord('A'))
        else:
            shifted_char = char  # Keep non-alphabetic characters unchanged
        result += shifted_char
    return result

def check_dict_case(dict):
    """Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if not dict:
        return False

    all_lower = True
    all_upper = True

    for key in dict:
        if not isinstance(key, str):
            return False  # Key is not a string
        if key.islower():
            all_upper = False
        elif key.isupper():
            all_lower = False
        else:
            return False  # Key is not all lower or all upper

    return all_lower or all_upper


def combined_operations(text):
    """
    Combines fix_spaces, encode, and encrypt operations on a string.

    Args:
        text: The input string.

    Returns:
        The final encrypted string.  Returns an empty string if input is not a string.
    """

    if not isinstance(text, str):
        return ""
    
    # fix_spaces implementation
    new_text = ""
    i = 0
    start, end = 0, 0
    while i < len(text):
        if text[i] == " ":
            end += 1
        else:
            if end - start > 2:
                new_text += "-" + text[i]
            elif end - start > 0:
                new_text += "_" * (end - start) + text[i]
            else:
                new_text += text[i]
            start, end = i + 1, i + 1
        i += 1
    if end - start > 2:
        new_text += "-"
    elif end - start > 0:
        new_text += "_"  

    # encode implementation
    vowels = "aeiouAEIOU"
    vowels_replace = {char: chr(ord(char) + 2) for char in vowels}
    encoded_text = "".join([vowels_replace.get(char, char.swapcase()) for char in new_text])
    
    # encrypt implementation
    d = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for char in encoded_text:
        if char.lower() in d:
            encrypted_text += d[(d.index(char.lower()) + 4) % 26]  # Rotated by 4 places
        else:
            encrypted_text += char
            
    return encrypted_text