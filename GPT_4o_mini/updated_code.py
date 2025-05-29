""""@Authors
Student Names: Muhammed Yunus Doğru
Student IDs: 150210092
"""
def odd_count(lst):
    """
    Given a list of numeric strings, return a new list whose i-th element is
    the sentence

        "the number of odd elements in the string i of the input."

    but with every lower-case letter 'i' replaced by the actual count of
    odd digits in the corresponding input string.
    """
    template = "the number of odd elements in the string i of the input."
    result = []
    for s in lst:
        count = sum(1 for ch in s if ch.isdigit() and int(ch) % 2 == 1)
        # replace every 'i' with the count
        result.append(template.replace('i', str(count)))
    return result

def maximum(arr, k):
    """
    Return the k largest values in arr as an ascending list.
    Duplicates are preserved. If k is 0, return [].
    """
    if k == 0:
        return []
    # sort ascending, then take the last k elements (which are the k largest),
    # preserving ascending order
    sorted_arr = sorted(arr)
    return sorted_arr[-k:]


from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return a list containing every prefix of *string* from shortest to longest.

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # For each length i = 1..len(string), take string[:i]
    return [string[:i] for i in range(1, len(string) + 1)]


from typing import List, Union

def do_algebra(operator: List[str], operand: List[int]) -> Union[int, float]:
    """
    Evaluate the algebraic expression constructed from
    *operand* and *operator* lists:

        result = operand[0] <op[0]> operand[1] <op[1]> operand[2] ...

    respecting standard Python operator precedence.

    Supported operators: +, -, *, //, **.

    >>> operator = ['+', '*', '-']
    >>> operand  = [2, 3, 4, 5]
    >>> do_algebra(operator, operand)
    9
    """
    if not operand:
        raise ValueError("operand list must contain at least one value")
    # Build the expression string
    expr = str(operand[0])
    for op, val in zip(operator, operand[1:]):
        expr += f" {op} {val}"
    # Evaluate using Python's precedence rules
    return eval(expr)

def largest_divisor(n: int) -> int:
    """
    Return the greatest proper divisor of *n* (1 ≤ result < n).

    >>> largest_divisor(15)
    5
    >>> largest_divisor(13)
    1
    >>> largest_divisor(100)
    50
    """
    if n <= 1:
        raise ValueError("n must be greater than 1")
    max_div = 1
    # Check up to sqrt(n) for divisors
    i = 2
    while i * i <= n:
        if n % i == 0:
            # i is a divisor, so is n//i
            other = n // i
            if other != n and other > max_div:
                max_div = other
            if i != n and i > max_div:
                max_div = i
        i += 1
    return max_div


def change_base(x: int, base: int) -> str:
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
    if x == 0:
        return '0'
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    # The remainders produce the digits in reverse order
    return ''.join(reversed(digits))


def median(l: list):
    """
    Return the median of numeric list *l*.  
    For even-length lists use the average of the two middle values.

    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    8.0
    """
    if not l:
        raise ValueError("median() arg is an empty list")
    sorted_l = sorted(l)
    n = len(sorted_l)
    mid = n // 2
    if n % 2 == 1:
        # odd length: return the middle element
        return sorted_l[mid]
    else:
        # even length: average the two middle elements
        return (sorted_l[mid - 1] + sorted_l[mid]) / 2

def circular_shift(x: int, shift: int) -> str:
    """
    Circularly shift the decimal digits of *x* right by *shift* places and
    return the result as a string.  
    If *shift* > number of digits, return the digits reversed.

    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    >>> circular_shift(12, 3)
    '21'
    >>> circular_shift(12345, 2)
    '45123'
    >>> circular_shift(12345, 5)
    '12345'
    >>> circular_shift(12345, 6)
    '54321'
    """
    s = str(x)
    n = len(s)
    if shift > n:
        return s[::-1]
    # normalize shift to [0, n)
    k = shift % n
    if k == 0:
        return s
    # take last k chars to front
    return s[-k:] + s[:-k]


from typing import List, Union

def pluck(arr: List[int]) -> Union[List[int], List]:
    """
    Return [value, index] for the node with the smallest even value in *arr*.
    On ties choose the lowest index.  
    Return [] if no even number exists or *arr* is empty.

    >>> pluck([4, 2, 3])
    [2, 1]
    >>> pluck([5, 0, 3, 0, 4, 2])
    [0, 1]
    >>> pluck([1, 3, 5])
    []
    >>> pluck([])
    []
    """
    best_val = None
    best_idx = None
    for idx, val in enumerate(arr):
        if val % 2 == 0:  # it's even
            if best_val is None or val < best_val:
                best_val = val
                best_idx = idx
    if best_val is None:
        return []
    return [best_val, best_idx]


def encode(message: str) -> str:
    """
    Swap the case of every letter in *message* and replace each vowel with the
    letter two places ahead in the alphabet (preserving case).

    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    # Mapping for vowels two places ahead
    vowel_map = {
        'a': 'c',
        'e': 'g',
        'i': 'k',
        'o': 'q',
        'u': 'w',
    }

    result = []
    for ch in message:
        if ch.isalpha():
            # Swap case
            swapped = ch.swapcase()
            lower = swapped.lower()
            # If it's a vowel after swapping, map it
            if lower in vowel_map:
                mapped = vowel_map[lower]
                # Preserve the swapped-case
                swapped = mapped.upper() if swapped.isupper() else mapped
            result.append(swapped)
        else:
            # Non-letter characters remain unchanged
            result.append(ch)
    return ''.join(result)

def valid_date(date: str) -> bool:
    """
    Validate a date string in 'mm-dd-yyyy' format.

    Day limits:
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
    parts = date.split('-')
    # Must be exactly three parts separated by '-'
    if len(parts) != 3:
        return False
    mm, dd, yyyy = parts
    # Check lengths and numeric
    if not (mm.isdigit() and dd.isdigit() and yyyy.isdigit()):
        return False
    if not (len(mm) == 2 and len(dd) == 2 and len(yyyy) == 4):
        return False

    month = int(mm)
    day = int(dd)
    # Month must be 1..12
    if not (1 <= month <= 12):
        return False

    # Determine max days in month
    if month in {1, 3, 5, 7, 8, 10, 12}:
        max_day = 31
    elif month in {4, 6, 9, 11}:
        max_day = 30
    else:  # month == 2
        max_day = 29

    # Day must be between 1 and max_day
    return 1 <= day <= max_day


import math

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
    a1, b1 = interval1
    a2, b2 = interval2

    # Compute intersection bounds
    low = max(a1, a2)
    high = min(b1, b2)

    # No intersection
    if low > high:
        return 'NO'

    length = high - low + 1

    # Helper to test primality
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        limit = int(math.isqrt(n))
        for i in range(3, limit + 1, 2):
            if n % i == 0:
                return False
        return True

    return 'YES' if is_prime(length) else 'NO'


from typing import List, Tuple

def minPath(grid: List[List[int]], k: int) -> List[int]:
    """
    Given an N×N grid (N ≥ 2) containing each integer 1…N² exactly once,
    return the lexicographically minimum path of length k (k cells) that
    can be walked by 4-neighbour moves. The path itself is returned as the
    ordered list of values on the visited cells. The answer is guaranteed
    to be unique.
    """
    if k == 0:
        return []
    N = len(grid)
    # Directions: up, down, left, right
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Find the coordinate of the minimal value (which must be 1)
    min_val = float('inf')
    start: Tuple[int, int] = (0, 0)
    for r in range(N):
        for c in range(N):
            if grid[r][c] < min_val:
                min_val = grid[r][c]
                start = (r, c)

    # Helper to count how many as-yet-unvisited cells are reachable from (r,c)
    # using 4-neighbor moves (inclusive of (r,c)), up to a max of `needed`.
    def reachable_count(r: int, c: int, needed: int, visited: List[List[bool]]) -> int:
        from collections import deque
        seen = [[False]*N for _ in range(N)]
        q = deque()
        q.append((r, c))
        seen[r][c] = True
        count = 0
        while q and count < needed:
            rr, cc = q.popleft()
            # Skip globally visited cells
            if visited[rr][cc]:
                continue
            count += 1
            for dr, dc in dirs:
                nr, nc = rr+dr, cc+dc
                if 0 <= nr < N and 0 <= nc < N and not seen[nr][nc]:
                    seen[nr][nc] = True
                    q.append((nr, nc))
        return count

    visited = [[False]*N for _ in range(N)]
    path: List[int] = []

    # Depth-first search with lexicographic pruning
    def dfs(r: int, c: int) -> List[int]:
        path.append(grid[r][c])
        visited[r][c] = True

        if len(path) == k:
            return path.copy()

        # Gather unvisited neighbors, sorted by their grid value
        nbrs = []
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                nbrs.append((grid[nr][nc], nr, nc))
        nbrs.sort()

        rem = k - len(path)
        for _, nr, nc in nbrs:
            # Prune if not enough reachable cells from this neighbor
            if reachable_count(nr, nc, rem, visited) >= rem:
                result = dfs(nr, nc)
                if result:
                    return result

        # Backtrack
        visited[r][c] = False
        path.pop()
        return []

    return dfs(*start)


def is_nested(string: str) -> bool:
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
    # Find first opening bracket
    i = string.find('[')
    if i == -1:
        return False
    # Find a second opening bracket after the first
    j = string.find('[', i + 1)
    if j == -1:
        return False
    # Find a closing bracket after the second opening
    k = string.find(']', j + 1)
    if k == -1:
        return False
    # Find another closing bracket after that
    l = string.find(']', k + 1)
    return l != -1


import re

def fix_spaces(text: str) -> str:
    """
    Replace every single space with '_' and every run of ≥2 consecutive
    spaces with '-'.

    >>> fix_spaces("Example") == "Example"
    True
    >>> fix_spaces("Example 1") == "Example_1"
    True
    >>> fix_spaces(" Example 2") == "_Example_2"
    True
    >>> fix_spaces(" Example   3") == "_Example-3"
    True
    """
    # First replace any run of two or more spaces with a single hyphen
    text = re.sub(r' {2,}', '-', text)
    # Then replace any remaining single space with underscore
    text = re.sub(r' ', '_', text)
    return text


def file_name_check(file_name: str) -> str:
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
    # Exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    # At most three digits total
    if sum(ch.isdigit() for ch in file_name) > 3:
        return 'No'
    name, ext = file_name.split('.')
    # Name must be non-empty and start with a letter
    if not name or not name[0].isalpha():
        return 'No'
    # Extension must be one of the allowed set
    if ext not in {'txt', 'exe', 'dll'}:
        return 'No'
    return 'Yes'
 
def int_to_mini_roman(number: int) -> str:
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
    if not (1 <= number <= 1000):
        raise ValueError("number must be between 1 and 1000 inclusive")
    roman_map = [
        (1000, "M"), (900, "CM"),
        (500, "D"),  (400, "CD"),
        (100, "C"),  (90, "XC"),
        (50, "L"),   (40, "XL"),
        (10, "X"),   (9, "IX"),
        (5, "V"),    (4, "IV"),
        (1, "I"),
    ]
    result = []
    n = number
    for value, symbol in roman_map:
        count, n = divmod(n, value)
        result.append(symbol * count)
        if n == 0:
            break
    return "".join(result).lower()


import math

def prime_fib(n: int) -> int:
    """
    Return the n-th Fibonacci number that is also prime.

    >>> prime_fib(1)
    2
    >>> prime_fib(5)
    89
    """
    if n < 1:
        raise ValueError("n must be at least 1")
    
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        if num in (2, 3):
            return True
        if num % 2 == 0:
            return False
        limit = int(math.isqrt(num))
        for i in range(3, limit + 1, 2):
            if num % i == 0:
                return False
        return True

    # Generate Fibonacci numbers
    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        # Check for primality
        if is_prime(a):
            count += 1
            if count == n:
                return a


from typing import List

def numerical_letter_grade(grades: List[float]) -> List[str]:
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
    """
    result = []
    for g in grades:
        if g == 4.0:
            result.append('A+')
        elif g > 3.7:
            result.append('A')
        elif g > 3.3:
            result.append('A-')
        elif g > 3.0:
            result.append('B+')
        elif g > 2.7:
            result.append('B')
        elif g > 2.3:
            result.append('B-')
        elif g > 2.0:
            result.append('C+')
        elif g > 1.7:
            result.append('C')
        elif g > 1.3:
            result.append('C-')
        elif g > 1.0:
            result.append('D+')
        elif g > 0.7:
            result.append('D')
        elif g > 0.0:
            result.append('D-')
        else:
            result.append('E')
    return result


def closest_integer(value: str) -> int:
    """
    Return the integer nearest to *value* (a numeric string).
    If equidistant, round away from zero.

    >>> closest_integer("14.5")
    15
    >>> closest_integer("-14.5")
    -15
    """
    # Handle sign
    sign = -1 if value.startswith('-') else 1
    s = value.lstrip('+-')
    # Split integer and fractional parts
    if '.' in s:
        int_part, frac_part = s.split('.', 1)
    else:
        # No fractional part: already integral
        return int(value)
    # Normalize empty parts
    int_part = int_part or '0'
    frac_part = frac_part.rstrip('0')  # drop trailing zeros
    if not frac_part:
        # Fractional was all zeros
        return sign * int(int_part)
    # Compute fractional numerator / denominator
    frac_num = int(frac_part)
    denom = 10 ** len(frac_part)
    # Compare 2*frac_num vs denom to decide <, =, or > .5
    twice = frac_num * 2
    if twice < denom:
        # fractional part < 0.5 -> round toward zero
        return sign * int(int_part)
    else:
        # fractional part >= 0.5 -> round away from zero
        return sign * (int(int_part) + 1)


from typing import List

def by_length(arr: List[int]) -> List[str]:
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
    # Mapping of digits to English names
    names = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }
    # Filter to keep only 1-9, sort ascending, then reverse for descending
    filtered = sorted([x for x in arr if 1 <= x <= 9], reverse=True)
    # Map to names
    return [names[x] for x in filtered]


def get_closest_vowel(word: str) -> str:
    """
    Return the right-most vowel that lies between two consonants inside *word*
    (excluding the first and last characters). Case-sensitive.  
    Return '' if no such vowel exists.

    >>> get_closest_vowel("yogurt")
    'u'
    >>> get_closest_vowel("FULL")
    'U'
    >>> get_closest_vowel("aeiou")
    ''
    """
    vowels = set('aeiouAEIOU')
    n = len(word)
    # Scan from right to left, excluding first and last character
    for i in range(n - 2, 0, -1):
        ch = word[i]
        if ch in vowels:
            left, right = word[i - 1], word[i + 1]
            # Check that both neighbors are consonants: alphabetic but not vowels
            if left.isalpha() and left not in vowels and right.isalpha() and right not in vowels:
                return ch
    return ''


from typing import List

def add_elements(arr: List[int], k: int) -> int:
    """
    Sum the elements that have **at most two digits** among the first *k*
    items of *arr*.

    >>> add_elements([111, 21, 3, 4000, 5], 4)
    24
    """
    total = 0
    for x in arr[:k]:
        # Count digits ignoring the sign
        if len(str(abs(x))) <= 2:
            total += x
    return total


import math
from typing import List

def sum_squares(lst: List[float]) -> int:
    """
    Round every element of *lst* up (ceiling), square it, and return the sum.

    >>> sum_squares([1, 2, 3])
    14
    >>> sum_squares([1.4, 4.2, 0])
    29
    """
    total = 0
    for x in lst:
        c = math.ceil(x)
        total += c * c
    return total


from typing import List

def specialFilter(nums: List[int]) -> int:
    """
    Count how many numbers in *nums* are > 10 **and** whose first & last
    digits are both odd (1,3,5,7,9).

    >>> specialFilter([15, -73, 14, -15])
    1
    >>> specialFilter([33, -2, -3, 45, 21, 109])
    2
    """
    count = 0
    for n in nums:
        if n > 10:
            s = str(abs(n))
            first, last = int(s[0]), int(s[-1])
            if first % 2 == 1 and last % 2 == 1:
                count += 1
    return count


def common(l1: list, l2: list) -> list:
    """
    Return the sorted list of unique elements common to *l1* and *l2*.

    >>> common([1, 4, 3, 34, 653, 2, 5],
    ...        [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    """
    # Use set intersection to find unique common elements, then sort
    return sorted(set(l1) & set(l2))


import math

def triangle_area(a: float, b: float, c: float) -> float:
    """
    Return the area of a triangle with side lengths *a*, *b*, *c*
    (Heron's formula), rounded to 2 decimals.  
    Return -1 if the sides cannot form a triangle.

    >>> triangle_area(3, 4, 5)
    6.00
    >>> triangle_area(1, 2, 10)
    -1
    """
    # Check triangle inequality
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    # Semi-perimeter
    s = (a + b + c) / 2.0
    # Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    # Round to 2 decimal places
    return round(area, 2)


import math

import math

def is_multiply_prime(a: int) -> bool:
    """
    Return True iff *a* (a < 100) equals the product of three primes.

    >>> is_multiply_prime(30)
    True    # 30 = 2 × 3 × 5
    >>> is_multiply_prime(12)
    True    # 12 = 2 × 2 × 3
    >>> is_multiply_prime(16)
    False   # 16 = 2 × 2 × 2 × 2 (four primes)
    >>> is_multiply_prime(1)
    False
    >>> is_multiply_prime(17)
    False   # prime itself only one factor
    """
    if a < 2:
        return False

    count = 0
    n = a
    # trial division up to sqrt(n)
    for p in range(2, int(math.isqrt(n)) + 1):
        while n % p == 0:
            count += 1
            n //= p
            if count > 3:
                return False
    # any remaining n > 1 is a prime factor
    if n > 1:
        count += 1
    return count == 3


def encrypt(s: str) -> str:
    """
    Shift every letter in *s* forward by 4 positions (2 × 2) in the
    alphabet, wrapping around, and return the new string.

    >>> encrypt('hi')
    'lm'
    >>> encrypt('asdfghjkl')
    'ewhjklnop'
    """
    result = []
    for ch in s:
        if 'a' <= ch <= 'z':
            # Compute 0–25 index, add 4, wrap mod 26, convert back
            result.append(chr((ord(ch) - ord('a') + 4) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + 4) % 26 + ord('A')))
        else:
            # Non-letters unchanged
            result.append(ch)
    return ''.join(result)


def check_dict_case(d: dict) -> bool:
    """
    Return True if all keys of d are strings that are either all-lower
    or all-upper case.  
    Empty dict → False.

    >>> check_dict_case({"a": "apple", "b": "banana"})
    True
    >>> check_dict_case({"Name": "John", "Age": "36"})
    False
    >>> check_dict_case({})
    False
    >>> check_dict_case({"A1": "x", "B2": "y"})
    True
    """
    # Empty dict should return False
    if not d:
        return False
    keys = d.keys()
    # All keys must be strings
    if not all(isinstance(k, str) for k in keys):
        return False
    # Check if all keys are all-lowercase
    if all(k.islower() for k in keys):
        return True
    # Check if all keys are all-uppercase
    if all(k.isupper() for k in keys):
        return True
    return False
