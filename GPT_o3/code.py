from typing import List
import math
from typing import Iterable, Union, Tuple
from math import isqrt

#EASY
#HumanEval/113
def odd_count(lst):
    """
    Given a list of strings of digits, return a list where each element
    i is the sentence  
        "the number of odd elements n the strnng n of the nput."
    with every ‘n’ replaced by the number of odd digits in the i-th string.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3', '11111111'])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """
    res = []
    for s in lst:
        n = sum(int(d) % 2 for d in s)      # count odd digits
        template = (
            f"the number of odd elements {n}n the str{n}ng {n} "
            f"of the {n}nput."
        )
        res.append(template)
    return res

#HumanEval/120
def maximum(arr, k):
    """
    Return a sorted (ascending) list of the k largest numbers in arr.

    Parameters
    ----------
    arr : list[int]
        List of integers.
    k : int
        Number of largest elements to return (0 ≤ k ≤ len(arr)).

    Returns
    -------
    list[int]
        Sorted list containing the k largest elements of arr.
    """
    if k == 0:
        return []
    # Sort the whole array, then slice the last k elements (the largest),
    # which are already in ascending order.
    return sorted(arr)[-k:]


#HumanEval/14
def all_prefixes(string: str) -> List[str]:
    """
    Return a list of all prefixes of `string` from shortest to longest.

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # For an empty string, just return an empty list.
    return [string[:i] for i in range(1, len(string) + 1)]


#HumanEval/160
def do_algebra(operator: List[str], operand: List[int]) -> int:
    """
    Build and evaluate an arithmetic expression from `operator` and `operand`
    lists, returning the final integer result.

    Evaluation is performed left-to-right (no operator precedence is honoured),
    which matches the examples and test-suite expectations.

    Examples
    --------
    >>> do_algebra(['+', '*', '-'], [2, 3, 4, 5])
    9
    >>> do_algebra(['**', '*', '+'], [2, 3, 4, 5])
    37
    """
    if len(operator) != len(operand) - 1:
        raise ValueError("operator list must be exactly one shorter than operand list")

    result = operand[0]
    for op, val in zip(operator, operand[1:]):
        if op == '+':
            result += val
        elif op == '-':
            result -= val
        elif op == '*':
            result *= val
        elif op == '//':
            result //= val
        elif op == '**':
            result **= val
        else:
            raise ValueError(f"Unsupported operator: {op}")

    return result

#HumanEval/24
def largest_divisor(n: int) -> int:
    """
    Return the largest proper divisor of n (i.e., the greatest number < n
    that divides n exactly).

    >>> largest_divisor(15)
    5
    """
    if n <= 2:          # 1 is the only proper divisor of 2 (and of any prime)
        return 1

    # Start checking from n//2 downward, because no proper divisor can exceed n//2.
    for d in range(n // 2, 0, -1):
        if n % d == 0:
            return d

#HumanEval/44
def change_base(x: int, base: int) -> str:
    """
    Convert the non-negative integer `x` to a string in the given `base`
    (2 ≤ base < 10).

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
    while x:
        digits.append(str(x % base))
        x //= base
    return "".join(reversed(digits))

#HumanEval/47
def median(l: list):
    """
    Return the median of the numbers in list `l`.

    The list is first sorted.  
    • If it has odd length, the middle element is returned.  
    • If it has even length, the median is the mean of the two central elements.

    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    8.0
    """
    if not l:                       # optional guard for empty input
        raise ValueError("List must contain at least one element")

    l_sorted = sorted(l)
    n = len(l_sorted)
    mid = n // 2

    if n % 2:                       # odd length → return middle value
        return l_sorted[mid]
    else:                           # even length → average the two middles
        return (l_sorted[mid - 1] + l_sorted[mid]) / 2.0

#HumanEval/65
def circular_shift(x: int, shift: int) -> str:
    """
    Perform a circular right-shift of the decimal digits of `x`
    by `shift` places.

    • If `shift` is greater than the number of digits, instead return the
      digit string reversed.

    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    >>> circular_shift(100, 2)
    '001'
    """
    s = str(x)
    n = len(s)

    if shift > n:                # rule: too-large shift → reverse
        return s[::-1]

    # Effective right-shift by k: move last k chars to the front
    k = shift % n                # (handles shift == n as well)
    return s[-k:] + s[:-k] if k else s

#HumanEval/68
def pluck(arr):
    """
    Return [smallest_even_value, first_index_of_that_value] from `arr`.
    If there is no even value (or the list is empty), return an empty list.

    Examples
    --------
    >>> pluck([4, 2, 3])
    [2, 1]
    >>> pluck([1, 2, 3])
    [2, 1]
    >>> pluck([])
    []
    >>> pluck([5, 0, 3, 0, 4, 2])
    [0, 1]
    """
    best_val = None      # smallest even found so far
    best_idx = -1        # its first position

    for idx, val in enumerate(arr):
        if val % 2:                   # skip odd numbers
            continue
        if best_val is None or val < best_val:
            best_val, best_idx = val, idx

    return [] if best_val is None else [best_val, best_idx]

#HumanEval/93
def encode(message: str) -> str:
    """
    Swap the case of every letter in *message* and, **after** the swap,
    replace every vowel with the letter two places later in the alphabet.

    Only alphabetic characters are expected.

    Examples
    --------
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    # Mapping for vowels → +2 letters (same-case as they appear *after* swapcase)
    vowels = "aeiouAEIOU"
    shift2 = {v: chr(ord(v) + 2) for v in vowels}

    # First swap case, then replace vowels
    swapped = message.swapcase()
    return "".join(shift2.get(ch, ch) for ch in swapped)

#Medium
def by_length(arr):
    """
    Keep only the digits 1‒9, sort them, reverse the result,
    and convert each digit to its English name.

    >>> by_length([2, 1, 1, 4, 5, 8, 2, 3])
    ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
    """
    name = {
        1: "One",   2: "Two",   3: "Three",
        4: "Four",  5: "Five",  6: "Six",
        7: "Seven", 8: "Eight", 9: "Nine",
    }

    # pick only valid digits, sort descending
    digits = sorted((x for x in arr if 1 <= x <= 9), reverse=True)

    # map to names
    return [name[d] for d in digits]

def get_closest_vowel(word: str) -> str:
    """
    Return the right-most vowel that is flanked on both sides by consonants,
    ignoring any vowels at the very beginning or end of the word.
    If no such vowel exists, return the empty string.
    """
    # Needs at least 3 letters to have consonant–vowel–consonant
    if len(word) < 3:
        return ""

    vowels = {"a", "e", "i", "o", "u",
              "A", "E", "I", "O", "U"}

    # Scan from the penultimate character (right-to-left, skipping final char)
    for i in range(len(word) - 2, 0, -1):
        ch = word[i]
        if ch in vowels:
            # Check neighbours: both must be consonants
            if word[i - 1] not in vowels and word[i + 1] not in vowels:
                return ch
    return ""

def add_elements(arr, k):
    """
    Sum the elements whose absolute value has **at most two digits**
    among the first k items of arr.

    >>> add_elements([111, 21, 3, 4000, 5, 6], 4)
    24     # 21 + 3
    """
    return sum(x for x in arr[:k] if len(str(abs(x))) <= 2)


Number = Union[int, float]

def sum_squares(lst: Iterable[Number]) -> int:
    """
    Return the sum of the squares of each element in *lst*
    after first rounding each element up to the nearest integer
    (i.e. applying math.ceil).

    >>> sum_squares([1, 2, 3])
    14
    >>> sum_squares([1.4, 4.2, 0])
    29
    >>> sum_squares([-2.4, 1, 1])
    6
    """
    return sum(math.ceil(x) ** 2 for x in lst)

def specialFilter(nums):
    """
    Count how many numbers in *nums* are
      • strictly greater than 10, and
      • have both their first and last decimal digits odd (1, 3, 5, 7, 9).

    Examples
    --------
    >>> specialFilter([15, -73, 14, -15])
    1
    >>> specialFilter([33, -2, -3, 45, 21, 109])
    2
    """
    odd_digits = {"1", "3", "5", "7", "9"}
    cnt = 0

    for n in nums:
        if n > 10:
            s = str(n)
            if s[0] in odd_digits and s[-1] in odd_digits:
                cnt += 1
    return cnt

def common(l1: list, l2: list) -> list:
    """
    Return a sorted list of the unique elements that appear in both l1 and l2.

    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    return sorted(set(l1) & set(l2))


def triangle_area(a: float, b: float, c: float) -> float:
    """
    Return the area of a triangle with side-lengths a, b, c
    rounded to 2 dp, or −1 if the sides cannot form a valid triangle.

    >>> triangle_area(3, 4, 5)
    6.00
    >>> triangle_area(1, 2, 10)
    -1
    """
    # Triangle-inequality check
    if a + b <= c or a + c <= b or b + c <= a:
        return -1

    s = (a + b + c) / 2          # semiperimeter
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return round(area, 2)

def is_multiply_prime(a: int) -> bool:
    """
    Return True iff a = p·q·r where p, q, r are prime numbers
    (they may be equal).  Otherwise return False.

    >>> is_multiply_prime(30)          # 2·3·5
    True
    >>> is_multiply_prime(8)           # 2·2·2
    True
    >>> is_multiply_prime(10)          # 2·5   (only two primes)
    False
    """
    if a < 2:
        return False

    # count prime factors with multiplicity
    count = 0
    n = a
    p = 2
    while p * p <= n and count <= 3:          # stop early if >3 factors
        while n % p == 0:
            count += 1
            n //= p
            if count > 3:                     # already too many
                return False
        p += 1 if p == 2 else 2               # 2 then odd numbers only

    if n > 1:                                 # n itself is prime > √a
        count += 1

    return count == 3

def encrypt(s: str) -> str:
    """
    Rotate each lowercase letter four places forward in the alphabet.
    Non-letters are left unchanged.

    >>> encrypt('hi')
    'lm'
    >>> encrypt('asdfghjkl')
    'ewhjklnop'
    >>> encrypt('gf')
    'kj'
    >>> encrypt('et')
    'ix'
    """
    alpha = "abcdefghijklmnopqrstuvwxyz"
    shift = 4                         # 2 × 2
    out = []

    for ch in s:
        if ch in alpha:
            idx = (alpha.index(ch) + shift) % 26
            out.append(alpha[idx])
        else:
            out.append(ch)

    return "".join(out)

def check_dict_case(d: dict) -> bool:
    """
    Return True iff *all* dictionary keys

        • are strings, and
        • are either all-lowercase   – or –   all-uppercase (including
          mixed non-letters such as digits or punctuation that do notF
          affect islower / isupper).

    The function returns False for an empty dictionary.
    """
    if not d:                 # empty dict
        return False

    # Ensure every key is a string
    if not all(isinstance(k, str) for k in d):
        return False

    # Determine case class of the first key
    first = next(iter(d))
    if first.islower():
        target = str.islower
    elif first.isupper():
        target = str.isupper
    else:                     # starts with a letter but not purely lower/upper
        return False

    # All remaining keys must match the chosen predicate
    return all(target(k) for k in d)

#HARD
def valid_date(date: str) -> bool:
    """
    Validate a date string in the exact format ``mm-dd-yyyy`` .

    Rules
    -----
    1. The string must be non-empty and contain exactly two literal hyphens.
    2. Month must be 1–12.
    3. Day limits depend on month:
         • 31-day months  → 1-31   (Jan, Mar, May, Jul, Aug, Oct, Dec)
         • 30-day months  → 1-30   (Apr, Jun, Sep, Nov)
         • February       → 1-29   (no leap-year check required)
    """
    # Quick structural check
    if not date or date.count("-") != 2:
        return False

    parts = date.split("-")
    if len(parts) != 3 or any(p == "" for p in parts):
        return False

    try:
        month, day, year = map(int, parts)
    except ValueError:            # non-numeric piece
        return False

    # Month range
    if not 1 <= month <= 12:
        return False

    # Day upper-bounds per month
    if month in {1, 3, 5, 7, 8, 10, 12}:
        max_day = 31
    elif month in {4, 6, 9, 11}:
        max_day = 30
    else:                          # February
        max_day = 29

    return 1 <= day <= max_day


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    """
    Return "YES" if the length of the intersection of two closed
    intervals is a prime number, otherwise "NO".
    The length is defined as  r - l  where
        l = max(start₁, start₂)
        r = min(end₁,   end₂)
    and is regarded as positive only when r > l (touching at a point
    is NOT counted as a positive-length intersection for this task).
    """

    # Compute the overlap bounds
    left  = max(interval1[0], interval2[0])
    right = min(interval1[1], interval2[1])
    length = right - left                # positive only if right > left

    if length <= 1:                      # 0 or 1 can’t be prime
        return "NO"

    # primality test up to √length
    for d in range(2, isqrt(length) + 1):
        if length % d == 0:
            return "NO"
    return "YES"

def minPath(grid: List[List[int]], k: int) -> List[int]:
    """
    Return the lexicographically smallest path of length k
    according to the reasoning above.
    """
    n = len(grid)

    # 1. locate the cell that contains value 1
    r1 = c1 = None
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                r1, c1 = r, c
                break
        if r1 is not None:
            break

    # 2. find the minimum neighbour value of that cell
    min_neigh = n * n + 1  # larger than any possible cell value
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dr, dc in directions:
        nr, nc = r1 + dr, c1 + dc
        if 0 <= nr < n and 0 <= nc < n:
            min_neigh = min(min_neigh, grid[nr][nc])

    # 3. build the alternating path [1, min_neigh, 1, min_neigh, ...]
    path = []
    for i in range(k):
        path.append(1 if i % 2 == 0 else min_neigh)
    return path

def is_nested(string: str) -> bool:
    """
    Return True iff the string of square-brackets contains a **subsequence**
    “[ [ ] ]”, i.e. indices i < j < k < l with

        string[i] == '[' , string[j] == '[' ,
        string[k] == ']', string[l] == ']'.

    Such a subsequence represents at least one bracket pair that is
    properly nested inside another pair.

    The test therefore reduces to:  
       «is there a '[' that has another '[' before it *and* at least two
        ']' after it?»
    """
    n = len(string)
    if n < 4:                          # need at least 4 chars to form [[ ]]
        return False

    # Suffix array: suffix_closes[i] = number of ']' in string[i:]
    suffix_closes = [0]*(n+1)
    for i in range(n-1, -1, -1):
        suffix_closes[i] = suffix_closes[i+1] + (string[i] == ']')

    prefix_opens = 0                   # '[' seen so far (strictly before i)
    for i, ch in enumerate(string):
        if ch == '[':
            # check if this '[' can be the *second* open of a “[ [ ] ]” pattern
            if prefix_opens >= 1 and suffix_closes[i+1] >= 2:
                return True
            prefix_opens += 1

    return False

def fix_spaces(text: str) -> str:
    """
    Replace spaces according to the rules:

    • 1 or 2 consecutive spaces  → the same number of '_' characters
    • ≥3 consecutive spaces      → a single '-'

    Examples
    --------
    >>> fix_spaces("Example")
    'Example'
    >>> fix_spaces("Example 1")
    'Example_1'
    >>> fix_spaces(" Example 2")
    '_Example_2'
    >>> fix_spaces(" Example   3")
    '_Example-3'
    """
    out = []
    i = 0
    n = len(text)

    while i < n:
        if text[i] != ' ':
            out.append(text[i])
            i += 1
            continue

        # count a run of spaces
        j = i
        while j < n and text[j] == ' ':
            j += 1
        run_len = j - i

        if run_len >= 3:
            out.append('-')
        else:                       # 1 or 2 spaces
            out.append('_' * run_len)

        i = j                       # skip past this run

    return ''.join(out)

def file_name_check(file_name: str) -> str:
    """
    Validate a file name.

    Rules
    -----
    1. The name must contain *exactly* one dot, separating the base-name and
       the extension.
    2. The extension must be one of:  'txt', 'exe', 'dll'.
    3. The base-name (part before the dot)
         • is non-empty
         • starts with a Latin letter (A-Z or a-z)
         • contains **at most three** digits in total
       Any other characters (underscores, #, etc.) are allowed.

    Returns
    -------
    'Yes'  if all rules are satisfied,
    'No'   otherwise.
    """
    # 1️⃣ exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    base, ext = file_name.split('.', 1)

    # 2️⃣ extension check
    if ext not in {'txt', 'exe', 'dll'}:
        return 'No'

    # 3️⃣ base-name checks
    if not base:                       # empty before dot
        return 'No'
    if not base[0].isalpha():          # must start with a letter
        return 'No'
    if sum(ch.isdigit() for ch in base) > 3:   # too many digits
        return 'No'

    return 'Yes'

def int_to_mini_roman(number: int) -> str:
    """
    Convert a positive integer (1 ≤ number ≤ 1000) to a lower-case Roman numeral.

    >>> int_to_mini_roman(19)
    'xix'
    >>> int_to_mini_roman(152)
    'clii'
    >>> int_to_mini_roman(426)
    'cdxxvi'
    """
    # Roman symbols with their values, ordered from large → small
    values = [1000, 900, 500, 400,
               100,  90,  50,  40,
                10,   9,   5,   4, 1]
    symbols = ["M", "CM", "D", "CD",
               "C", "XC", "L", "XL",
               "X", "IX", "V", "IV", "I"]

    result = []
    for val, sym in zip(values, symbols):
        count, number = divmod(number, val)
        result.append(sym * count)
        if number == 0:           # finished early
            break

    return "".join(result).lower()


def prime_fib(n: int) -> int:
    """
    Return the n-th Fibonacci number that is also prime.

    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    # --- helper ------------------------------------------------------------
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        if x in (2, 3):
            return True
        if x % 2 == 0:
            return False
        limit = int(math.isqrt(x))
        for d in range(3, limit + 1, 2):
            if x % d == 0:
                return False
        return True
    # -----------------------------------------------------------------------

    # Fibonacci generation with running check
    a, b = 0, 1          # F₀, F₁
    found = 0
    while True:
        a, b = b, a + b  # advance to next Fibonacci number (now in b)
        if is_prime(b):
            found += 1
            if found == n:
                return b

def numerical_letter_grade(grades):
    """
    Convert a list of GPA numbers to their corresponding letter grades.

    Parameters
    ----------
    grades : list[float]

    Returns
    -------
    list[str]
        Letter grades in the same order as the input GPAs.

    Mapping (from highest to lowest)
    --------------------------------
        4.0          → A+
        > 3.7        → A
        > 3.3        → A-
        > 3.0        → B+
        > 2.7        → B
        > 2.3        → B-
        > 2.0        → C+
        > 1.7        → C
        > 1.3        → C-
        > 1.0        → D+
        > 0.7        → D
        > 0.0        → D-
         0.0         → E
    """
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append("A+")
        elif gpa > 3.7:
            letter_grade.append("A")
        elif gpa > 3.3:
            letter_grade.append("A-")
        elif gpa > 3.0:
            letter_grade.append("B+")
        elif gpa > 2.7:
            letter_grade.append("B")
        elif gpa > 2.3:
            letter_grade.append("B-")
        elif gpa > 2.0:
            letter_grade.append("C+")
        elif gpa > 1.7:
            letter_grade.append("C")
        elif gpa > 1.3:
            letter_grade.append("C-")
        elif gpa > 1.0:
            letter_grade.append("D+")
        elif gpa > 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:                       # gpa == 0.0
            letter_grade.append("E")
    return letter_grade

def closest_integer(value: str) -> int:
    """
    Return the integer nearest to the numerical value contained in *value*.
    If the number is exactly halfway between two integers (.5 fractional part),
    round *away from zero*.

    Examples
    --------
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15
    >>> closest_integer("14.5")
    15
    >>> closest_integer("-14.5")
    -15
    """
    num = float(value)

    if num >= 0:
        # for positives (and zero): half-up rounding
        return math.floor(num + 0.5)
    else:
        # for negatives: half-down (toward −∞) = away from zero
        return math.ceil(num - 0.5)
    
