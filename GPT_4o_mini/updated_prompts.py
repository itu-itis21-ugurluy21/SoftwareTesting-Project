""""@Authors
Student Names: Muhammed Yunus Doğru
Student IDs: 150210092
"""
# HumanEval/113
def odd_count(lst):
    """
    Given a list of numeric strings, return a new list whose *i-th* element is
    the sentence

        "the number of odd elements in the string i of the input."

    but with every lower-case letter **i** replaced by the *actual count* of
    odd digits in the corresponding input string.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3', '11111111'])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """
    pass


# HumanEval/120
def maximum(arr, k):
    """
    Return the *k* largest values in **arr** as an **ascending** list.
    Duplicates are preserved.  If *k* is 0, return [].

    >>> maximum([-3, -4, 5], 3)
    [-4, -3, 5]
    >>> maximum([4, -4, 4], 2)
    [4, 4]
    >>> maximum([-3, 2, 1, 2, -1, -2, 1], 1)
    [2]
    """
    pass


# HumanEval/14
from typing import List
def all_prefixes(string: str) -> List[str]:
    """
    Return a list containing every prefix of *string* from shortest to longest.

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    pass


# HumanEval/160
def do_algebra(operator, operand):
    """
    Evaluate the left-to-right algebraic expression constructed from
    *operand* and *operator* lists:

        result = operand[0] <op[0]> operand[1] <op[1]> operand[2] ...

    Supported operators: +, -, *, //, **.

    >>> operator = ['+', '*', '-']
    >>> operand  = [2, 3, 4, 5]
    >>> do_algebra(operator, operand)
    9
    """
    pass


# HumanEval/24
def largest_divisor(n: int) -> int:
    """
    Return the greatest proper divisor of *n* (1 ≤ result < n).

    >>> largest_divisor(15)
    5
    """
    pass


# HumanEval/44
def change_base(x: int, base: int):
    """
    Convert non-negative integer *x* to the given base (2 ≤ base ≤ 9) and
    return the result as a string.

    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    pass


# HumanEval/47
def median(l: list):
    """
    Return the median of numeric list *l*.  
    For even-length lists use the average of the two middle values.

    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    8.0
    """
    pass


# HumanEval/65
def circular_shift(x, shift):
    """
    Circularly shift the decimal digits of *x* right by *shift* places and
    return the result as a string.  
    If *shift* > number of digits, return the digits reversed.

    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """
    pass


# HumanEval/68
def pluck(arr):
    """
    Return [value, index] for the node with the smallest even value in *arr*.
    On ties choose the lowest index.  
    Return [] if no even number exists or *arr* is empty.

    >>> pluck([4, 2, 3])
    [2, 1]
    >>> pluck([5, 0, 3, 0, 4, 2])
    [0, 1]
    """
    pass


# HumanEval/93
def encode(message):
    """
    Swap the case of every letter in *message* and replace each vowel with the
    letter two places ahead in the alphabet (preserving case).

    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    pass


# HumanEval/124
def valid_date(date):
    """
    Validate a date string in 'mm-dd-yyyy' format.

    Day limits  
        • 31 days for months 1,3,5,7,8,10,12  
        • 30 days for months 4,6,9,11  
        • 29 days for month 2 (leap-year rules are ignored)

    >>> valid_date('03-11-2000')
    True
    >>> valid_date('15-01-2012')
    False
    >>> valid_date('06/04/2020')
    False
    """
    pass


# HumanEval/127
def intersection(interval1, interval2):
    """
    Return 'YES' if the (inclusive) intersection of *interval1* and *interval2*
    has prime length, otherwise 'NO'.  
    If they do not intersect, return 'NO'.

    >>> intersection((1, 2), (2, 3))
    'NO'
    >>> intersection((-3, -1), (-5, 5))
    'YES'
    """
    pass


# HumanEval/129
def minPath(grid, k):
    """
    Given an N×N grid (N ≥ 2) containing each integer 1…N² exactly once,
    return the lexicographically minimum path of length *k* (k cells) that
    can be walked by 4-neighbour moves.  The path itself is returned as the
    ordered list of values on the visited cells.  The answer is guaranteed
    to be unique.
    """
    pass


# HumanEval/132
def is_nested(string):
    """
    Return True iff *string* (containing only '[' and ']') has at least one
    valid bracket subsequence in which some bracket is nested.

    >>> is_nested('[[]]')
    True
    >>> is_nested('[]]]]]]][[[[[]')
    False
    >>> is_nested('[][]')
    False
    """
    pass


# HumanEval/140
def fix_spaces(text):
    """
    Replace every single space with '_' and every run of **≥ 2** consecutive
    spaces with '-'.

    >>> fix_spaces("Example") == "Example"
    >>> fix_spaces("Example 1") == "Example_1"
    >>> fix_spaces(" Example 2") == "_Example_2"
    >>> fix_spaces(" Example   3") == "_Example-3"
    """
    pass


# HumanEval/141
def file_name_check(file_name):
    """
    Return 'Yes' if *file_name* is valid, else 'No'.

    Criteria
    --------
    • At most three digits in total  
    • Exactly one dot '.'  
    • Name before the dot is non-empty and starts with a letter (A-Z / a-z)  
    • Extension after the dot is one of: 'txt', 'exe', 'dll'

    >>> file_name_check("example.txt")
    'Yes'
    >>> file_name_check("1example.dll")
    'No'
    """
    pass


# HumanEval/156
def int_to_mini_roman(number):
    """
    Convert *number* (1 ≤ number ≤ 1000) to its Roman-numeral representation
    and return it in lower-case.

    >>> int_to_mini_roman(19)
    'xix'
    >>> int_to_mini_roman(152)
    'clii'
    >>> int_to_mini_roman(426)
    'cdxxvi'
    """
    pass


# HumanEval/39
def prime_fib(n: int):
    """
    Return the n-th Fibonacci number that is also prime.

    >>> prime_fib(1)
    2
    >>> prime_fib(5)
    89
    """
    pass


# HumanEval/81
def numerical_letter_grade(grades):
    """
    Map each GPA in *grades* to its letter grade.

                 GPA        Letter
                 4.0         A+
               > 3.7          A
               > 3.3          A-
               > 3.0          B+
               > 2.7          B
               > 2.3          B-
               > 2.0          C+
               > 1.7          C
               > 1.3          C-
               > 1.0          D+
               > 0.7          D
               > 0.0          D-
                 0.0          E

    >>> numerical_letter_grade([4.0, 3, 1.7, 2, 3.5])
    ['A+', 'B', 'C-', 'C', 'A-']
    """
    pass


# HumanEval/99
def closest_integer(value):
    """
    Return the integer nearest to *value* (a numeric string).  
    If equidistant, round **away from zero**.

    >>> closest_integer("14.5")
    15
    >>> closest_integer("-14.5")
    -15
    """
    pass


# HumanEval/105
def by_length(arr):
    """
    Keep only the digits 1-9 in *arr*, sort them, reverse the order,
    and map each digit to its English name.

    >>> by_length([2, 1, 1, 4, 5, 8, 2, 3])
    ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
    >>> by_length([])
    []
    >>> by_length([1, -1, 55])
    ['One']
    """
    pass


# HumanEval/118
def get_closest_vowel(word):
    """
    Return the right-most vowel that lies between two consonants inside *word*
    (excluding the first and last characters).  Case-sensitive.  
    Return '' if no such vowel exists.

    >>> get_closest_vowel("yogurt")
    'u'
    >>> get_closest_vowel("FULL")
    'U'
    """
    pass


# HumanEval/122
def add_elements(arr, k):
    """
    Sum the elements that have **at most two digits** among the first *k*
    items of *arr*.

    >>> add_elements([111, 21, 3, 4000, 5], 4)
    24
    """
    pass


# HumanEval/133
def sum_squares(lst):
    """
    Round every element of *lst* up (ceiling), square it, and return the sum.

    >>> sum_squares([1, 2, 3])
    14
    >>> sum_squares([1.4, 4.2, 0])
    29
    """
    pass


# HumanEval/146
def specialFilter(nums):
    """
    Count how many numbers in *nums* are > 10 **and** whose first & last
    digits are both odd (1,3,5,7,9).

    >>> specialFilter([15, -73, 14, -15])
    1
    >>> specialFilter([33, -2, -3, 45, 21, 109])
    2
    """
    pass


# HumanEval/58
def common(l1: list, l2: list):
    """
    Return the sorted list of unique elements common to *l1* and *l2*.

    >>> common([1, 4, 3, 34, 653, 2, 5],
    ...        [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    """
    pass


# HumanEval/71
def triangle_area(a, b, c):
    """
    Return the area of a triangle with side lengths *a*, *b*, *c*
    (Heron's formula), rounded to 2 decimals.  
    Return -1 if the sides cannot form a triangle.

    >>> triangle_area(3, 4, 5)
    6.00
    >>> triangle_area(1, 2, 10)
    -1
    """
    pass


# HumanEval/75
def is_multiply_prime(a):
    """
    Return True iff *a* (a < 100) equals the product of **three** primes.

    >>> is_multiply_prime(30)
    True    # 30 = 2 × 3 × 5
    """
    pass


# HumanEval/89
def encrypt(s):
    """
    Shift every letter in *s* **forward by 4** positions (2 × 2) in the
    alphabet, wrapping around, and return the new string.

    >>> encrypt('hi')
    'lm'
    >>> encrypt('asdfghjkl')
    'ewhjklnop'
    """
    pass


# HumanEval/95
def check_dict_case(dict):
    """
    Return True if **all** keys of *dict* are strings that are either all-lower
    or all-upper case.  
    Empty dict → False.

    >>> check_dict_case({"a": "apple", "b": "banana"})
    True
    >>> check_dict_case({"Name": "John", "Age": "36"})
    False
    """
    pass
