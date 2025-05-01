""""@Authors
Student Names: Muhammed Yunus Doğru
Student IDs: 150210092
"""
#HumanEval/113
def odd_count(lst):
    result = []
    for s in lst:
        count = sum(1 for c in s if c in '13579')
        template = "the number of odd elements in the string i of the input."
        replaced = template.replace("i", str(count))
        result.append(replaced)
    return result



#HumanEval/120
def maximum(arr, k):
    return sorted(sorted(arr, reverse=True)[:k])


#HumanEval/14
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]


#HumanEval/160
def do_algebra(operator, operand):
    expression = str(operand[0])
    for op, val in zip(operator, operand[1:]):
        expression += f' {op} {val}'
    return eval(expression)


#HumanEval/24
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i


#HumanEval/44
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base. Return string representation."""
    if x == 0:
        return '0'
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    return ''.join(reversed(digits))


#HumanEval/47
def median(l: list):
    """Return median of elements in the list l."""
    l_sorted = sorted(l)
    n = len(l_sorted)
    mid = n // 2
    if n % 2 == 1:
        return l_sorted[mid]
    else:
        return (l_sorted[mid - 1] + l_sorted[mid]) / 2


#HumanEval/65
def circular_shift(x, shift):
    """Circular shift the digits of x to the right by `shift` positions."""
    s = str(x)
    n = len(s)
    if shift > n:
        return s[::-1]
    return s[-shift:] + s[:-shift]


#HumanEval/68
def pluck(arr):
    min_even = None
    min_index = -1
    for i, val in enumerate(arr):
        if val % 2 == 0:
            if min_even is None or val < min_even:
                min_even = val
                min_index = i
    return [min_even, min_index] if min_even is not None else []


#HumanEval/93
def encode(message):
    vowels = 'aeiouAEIOU'
    result = []
    for ch in message:
        if ch in vowels:
            new_char = chr(ord(ch) + 2)
            result.append(new_char.swapcase())
        else:
            result.append(ch.swapcase())
    return ''.join(result)


#HumanEval/124
def valid_date(date):
    if not date or len(date) != 10:
        return False
    
    parts = date.split('-')
    if len(parts) != 3:
        return False
    
    month_str, day_str, year_str = parts

    if not (month_str.isdigit() and day_str.isdigit() and year_str.isdigit()):
        return False

    month = int(month_str)
    day = int(day_str)

    if month < 1 or month > 12:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= day <= 31
    elif month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    elif month == 2:
        return 1 <= day <= 29

    return False


#HumanEval/127
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


#HumanEval/129
import heapq

def minPath(grid, k):
    n = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    # Min-heap with entries: (path_list, row, col)
    heap = []

    # Start from every cell
    for i in range(n):
        for j in range(n):
            heapq.heappush(heap, ([grid[i][j]], i, j))

    while heap:
        path, x, y = heapq.heappop(heap)
        if len(path) == k:
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                heapq.heappush(heap, (path + [grid[nx][ny]], nx, ny))


#HumanEval/132
def is_nested(string):
    depth = 0
    for char in string:
        if char == '[':
            depth += 1
            if depth > 1:
                return True  # nested!
        elif char == ']':
            if depth > 0:
                depth -= 1
    return False


#HumanEval/140
import re

def fix_spaces(text):
    # Step 1: Replace 3+ spaces with dash
    text = re.sub(r' {3,}', '-', text)
    # Step 2: Replace remaining spaces (1 or 2) with underscores
    text = re.sub(r' {1,2}', '_', text)
    return text


#HumanEval/141
def file_name_check(file_name):
    # Rule 1: Count digits
    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'
    
    # Rule 2: Check dot presence
    if file_name.count('.') != 1:
        return 'No'
    
    name, ext = file_name.split('.')
    
    # Rule 3: Validate name before dot
    if not name or not name[0].isalpha():
        return 'No'
    
    # Rule 4: Validate extension
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'


#HumanEval/156
def int_to_mini_roman(number):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman = ""
    for i in range(len(val)):
        while number >= val[i]:
            roman += syms[i]
            number -= val[i]
    return roman.lower()


#HumanEval/39
def prime_fib(n: int) -> int:
    fibs = [0, 1]
    count = 0
    i = 2
    while True:
        fib = fibs[-1] + fibs[-2]
        fibs.append(fib)
        if is_prime(fib):
            count += 1
            if count == n:
                return fib
        i += 1


#HumanEval/81
def numerical_letter_grade(grades):
    result = []
    for gpa in grades:
        if gpa == 4.0:
            result.append('A+')
        elif gpa > 3.7:
            result.append('A')
        elif gpa > 3.3:
            result.append('A-')
        elif gpa > 3.0:
            result.append('B+')
        elif gpa > 2.7:
            result.append('B')
        elif gpa > 2.3:
            result.append('B-')
        elif gpa > 2.0:
            result.append('C+')
        elif gpa > 1.7:
            result.append('C')
        elif gpa > 1.3:
            result.append('C-')
        elif gpa > 1.0:
            result.append('D+')
        elif gpa > 0.7:
            result.append('D')
        elif gpa > 0.0:
            result.append('D-')
        else:
            result.append('E')
    return result


#HumanEval/99
def closest_integer(value):
    num = float(value)
    if num > 0:
        return int(num + 0.5)
    else:
        return int(num - 0.5)


#HumanEval/105
def by_length(arr):
    digit_names = {
        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }

    # Filter only valid digits
    valid_digits = [x for x in arr if 1 <= x <= 9]
    # Sort and reverse
    valid_digits.sort()
    valid_digits.reverse()
    # Map to names
    return [digit_names[x] for x in valid_digits]


#HumanEval/118
def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    n = len(word)
    
    # Start from the second last character and go backwards (excluding first and last)
    for i in range(n - 2, 0, -1):
        if word[i] in vowels:
            if word[i - 1] not in vowels and word[i + 1] not in vowels:
                return word[i]
    return ""


#HumanEval/122
def add_elements(arr, k):
    return sum(x for x in arr[:k] if -99 <= x <= 99)


#HumanEval/133
import math

def sum_squares(lst):
    return sum(math.ceil(x)**2 for x in lst)


#HumanEval/146
def specialFilter(nums):
    def is_odd_digit(d):
        return d in {'1', '3', '5', '7', '9'}
    
    count = 0
    for num in nums:
        if num > 10:
            s = str(num)
            if is_odd_digit(s[0]) and is_odd_digit(s[-1]):
                count += 1
    return count


#HumanEval/58
def common(l1: list, l2: list):
    return sorted(set(l1) & set(l2))


#HumanEval/71
import math

def triangle_area(a, b, c):
    # Check for triangle validity
    if a + b <= c or a + c <= b or b + c <= a:
        return -1

    # Calculate semi-perimeter
    s = (a + b + c) / 2

    # Calculate area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Return area rounded to 2 decimal places
    return round(area, 2)


#HumanEval/75
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [p for p in range(2, 100) if is_prime(p)]

    # Try all combinations of 3 primes (not necessarily distinct)
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            for k in range(j, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False


#HumanEval/89
def encrypt(s):
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            shifted = chr(((ord(char) - ord('a') + 4) % 26) + ord('a'))
            result += shifted
        else:
            result += char  # Keep non-lowercase letters unchanged (optional)
    return result


#HumanEval/95
def check_dict_case(dict):
    if not dict:
        return False
    keys = dict.keys()
    if all(isinstance(k, str) and k.islower() for k in keys):
        return True
    if all(isinstance(k, str) and k.isupper() for k in keys):
        return True
    return False
