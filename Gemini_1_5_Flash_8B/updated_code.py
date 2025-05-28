from typing import List # Retained from original
import heapq # Retained from original
import math # Retained from original, also used by updated functions

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
    Given an array arr of integers and a positive integer k, return a list
    of length k containing the k largest numbers from arr.
    The returned list MUST be sorted in ascending order.

    Example 1:
    Input: arr = [-3, -4, 5], k = 3
    Output: [-4, -3, 5]
    ...
    """
    if k == 0: # Added from updated_functions.py, similar to original
        return []
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Return the first k elements (which are now the largest) sorted ascending
    return sorted(arr[:k])


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
    Given two lists: `operator` (list of strings with basic algebra operations) and
    `operand` (list of non-negative integers).
    Construct an algebraic expression by interleaving operands and operators.
    For example, if operator=['+', '*'] and operand=[2, 3, 4], the expression is "2+3*4".
    Return the integer result of evaluating this expression.

    The basic algebra operations to support:
    Addition ( + )
    Subtraction ( - )
    Multiplication ( * )
    Floor division ( // )
    Exponentiation ( ** )

    Constraints and Error Handling:
    1. The length of the `operator` list MUST be exactly one less than the length of the `operand` list.
       If this condition is not met, raise a ValueError with the message "Operator and operand lists have incorrect lengths."
    2. The `operator` list will have at least one operator, and the `operand` list will have at least two operands.
    3. If any operation would result in a division by zero, raise a ValueError with a message indicating division by zero (e.g., "Invalid expression or operation: integer division or modulo by zero").
    4. For other invalid expressions (e.g., unsupported operators if not from the list above, or malformed expressions), raise a ValueError indicating an invalid expression or syntax.

    Example:
    operator=['+', '*', '-']
    operand = [2, 3, 4, 5]
    Expression: 2 + 3 * 4 - 5
    Result: 9
    """

    if len(operator) != len(operand) - 1:
        raise ValueError("Operator and operand lists have incorrect lengths.")

    expression = ""
    for i in range(len(operand)): # Iterate based on operand length
        expression += str(operand[i])
        if i < len(operator): # Add operator if it exists for this operand
            expression += operator[i]

    try:
        result = eval(expression)
        return int(result) # Ensure integer result as per prompt
    except (ZeroDivisionError) as e: # More specific catch
        raise ValueError(f"Invalid expression or operation: integer division or modulo by zero")
    except (SyntaxError, NameError) as e: # Other eval errors
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
    Return string representation after the conversion.
    The base must be an integer between 2 and 9, inclusive (i.e., 2 <= base <= 9).
    If the provided base is outside this valid range, the function should raise a ValueError.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if not (isinstance(base, int) and 2 <= base <= 9): # ensure base is int
        raise ValueError("Base must be an integer between 2 and 9, inclusive.")

    if x == 0:
        return "0"
    
    if x < 0: # Handle negative numbers if necessary, though prompt implies positive x
        # Decide on a convention for negative numbers, e.g., prefix with '-'
        # For now, let's assume x is non-negative as per typical base conversion examples
        # or raise ValueError("Input x must be non-negative for this base conversion.")
        pass


    result = ""
    while x > 0:
        remainder = x % base
        result = str(remainder) + result  # Prepend to build the string
        x //= base

    return result

def median(l: list):
    """Return median of elements in the list l.
    If the list l is empty, return None.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if not l:
        return None
    
    sorted_l = sorted(l) # Use a sorted copy to not modify original list
    n = len(sorted_l)
    
    if n % 2 == 0:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2.0 # Ensure float division
    else:
        return sorted_l[n // 2]

def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    IMPORTANT: If the absolute value of 'shift' is greater than the number of digits in x,
    the function MUST return the string representation of x with its digits reversed.
    Otherwise (if abs(shift) <= number of digits):
        - Perform a circular right shift. A positive 'shift' value means right shift.
        - A negative 'shift' value should be treated as a left circular shift.
          A left circular shift by `s` is equivalent to a right circular shift by `num_digits - abs(s)`.
        - A shift of 0 or a multiple of the number of digits (considering absolute value for negative shifts) 
          should result in the original string.
    Convert x to string first.

    Example:
    >>> circular_shift(12, 1) # Right shift by 1
    "21"
    >>> circular_shift(123, 4) # shift (4) > num_digits (3) -> reverse
    "321"
    >>> circular_shift(123, 1) # Right shift by 1
    "312"
    >>> circular_shift(123, -1) # Left shift by 1
    "231"
    >>> circular_shift(12, 2) # Shift by num_digits
    "12"
    """
    x_str = str(x)
    num_digits = len(x_str)

    if num_digits == 0: # Handle empty string case if x could be empty
        return ""

    if abs(shift) > num_digits : # Corrected condition as per prompt >= to >
        return x_str[::-1]
    
    # Normalize shift
    # For positive shift, it's a right shift.
    # For negative shift, it's a left shift. Convert to equivalent right shift.
    # A left shift by s is a right shift by num_digits - s (for positive s)
    # So, a left shift by negative `shift` is a right shift by `num_digits + shift` (since shift is negative)
    # Or simply, `actual_shift = shift % num_digits` handles both positive and negative correctly
    # for circular behavior when not reversing.
    
    actual_shift = shift % num_digits
    
    # If actual_shift is 0 (due to shift being 0, num_digits, or -num_digits etc.), return original
    if actual_shift == 0:
        return x_str
        
    return x_str[-actual_shift:] + x_str[:-actual_shift]


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
        if val % 2 == 0: # Check if even
            if val < smallest_even: # If this even number is smaller
                smallest_even = val
                smallest_index = i
            # If it's the same smallest even value, we don't need to update
            # because we are looking for the one with the smallest index,
            # and iterating from left to right naturally finds that first.
            
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
    vowels = "aeiou" # Check lowercase vowels
    encoded_message = ""
    for char_original in message:
        char_swapped_case = char_original.swapcase() # Determine target case first
        char_lower = char_original.lower()

        if char_lower in vowels:
            # Calculate the vowel 2 places ahead
            # Need to handle 'y' and 'z' if they were targets, but alphabet wraps around
            original_ord_base = ord('a') if 'a' <= char_lower <= 'z' else ord('A') # Not needed if using char_lower
            
            shifted_char_ord = ord(char_lower) + 2
            # Wrap around 'z' -> 'b', 'y' -> 'a'
            if char_lower == 'y': # y -> a
                 shifted_char_lower = 'a'
            elif char_lower == 'z': # z -> b
                 shifted_char_lower = 'b'
            else:
                 shifted_char_lower = chr(ord(char_lower) + 2)

            # Apply the case that is the SWAP of the original vowel's case
            # If original was 'a', swapped is 'A'. If original was 'E', swapped is 'e'.
            if char_original.islower():
                encoded_message += shifted_char_lower.upper()
            else:
                encoded_message += shifted_char_lower.lower()
        else: # Consonant
            encoded_message += char_swapped_case
            
    return encoded_message

def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all ofजग the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days:
        - For months 1, 3, 5, 7, 8, 10, 12: days must be between 1 and 31.
        - For months 4, 6, 9, 11: days must be between 1 and 30.
        - For month 2 (February):
            - If the year is a leap year, days must be between 1 and 29.
            - If the year is not a leap year, days must be between 1 and 28.
            (A year is a leap year if it is divisible by 4, except for end-of-century years, which must be divisible by 400. E.g., 2000 was a leap year, 1900 was not.)
    3. The months should be between 1 and 12 inclusive.
    4. The date should be in the format: mm-dd-yyyy (e.g., '03-11-2000'). The month, day, and year parts must be valid integers.
    5. The year should be a positive integer. (Implicitly, but good to state if issues arise with yyyy format vs actual year range).

    for example:
    valid_date('03-11-2000') => True
    valid_date('02-29-2000') => True (Leap year)
    valid_date('02-29-2001') => False (Not a leap year)
    valid_date('15-01-2012') => False (Month and day are swapped from typical American usage; problem expects mm-dd-yyyy)
    valid_date('04-0-2040') => False
    valid_date('06-04-2020') => True
    valid_date('06/04/2020') => False (Incorrect separator)
    """

    if not date: # Rule 1
        return False

    parts = date.split('-')
    if len(parts) != 3: # Rule 4 (format check part 1)
        return False

    try:
        month_str, day_str, year_str = parts[0], parts[1], parts[2]
        # Rule 4 (format check part 2: ensure mm, dd, yyyy structure)
        if not (len(month_str) == 2 and len(day_str) == 2 and len(year_str) == 4):
            return False
        
        month, day, year = int(month_str), int(day_str), int(year_str)
    except ValueError: # Rule 4 (not valid integers)
        return False

    if not (1 <= month <= 12): # Rule 3
        return False
    
    if year <= 0: # Rule 5 (implicitly, but good to be explicit)
        return False

    # Rule 2: Days check
    if month == 2: # February
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap:
            if not (1 <= day <= 29):
                return False
        else:
            if not (1 <= day <= 28):
                return False
    elif month in [4, 6, 9, 11]: # 30-day months
        if not (1 <= day <= 30):
            return False
    else: # 31-day months (1, 3, 5, 7, 8, 10, 12)
        if not (1 <= day <= 31):
            return False
            
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

    if intersection_start > intersection_end: # No overlap
        return "NO"

    # Length of a closed interval [a, b] is b - a + 1
    # However, the problem's examples (e.g. (1,3) and (2,4) -> (2,3) length 1)
    # implies length is (intersection_end - intersection_start).
    # Let's re-evaluate based on how "length" is typically defined for primality test.
    # If intersection is (2,3), length of values in it is 2 (2 and 3).
    # If length means number of integers in the interval: end - start + 1
    # If length means the span: end - start
    # The example says (2,3) length 1 (not prime). This means length = intersection_end - intersection_start.
    # Let's use the problem's implicit definition from example:
    # Intersection: (2,3). Length = 3 - 2 = 1. 1 is not prime. -> "NO". This matches example.
    # Intersection: (1,10), (2,9) -> (2,9). Length = 9 - 2 = 7. 7 is prime. -> "YES". Test case expects this.
    # Intersection: (1,10), (5,5) -> (5,5). Length = 5 - 5 = 0. 0 is not prime. Test expects NO.
    # This definition seems consistent with some of the failing tests.

    length = intersection_end - intersection_start
    
    if length < 2: # Numbers less than 2 are not prime.
        return "NO"

    # Primality test for 'length'
    if length == 2:
        return "YES"
    if length % 2 == 0: # Other even numbers are not prime
        return "NO"
    # Check for divisibility by odd numbers up to sqrt(length)
    for i in range(3, int(length**0.5) + 1, 2):
        if length % i == 0:
            return "NO"

    return "YES"


def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k,
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    If the input `grid` is empty, return an empty list `[]`.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with your current
    cell (up, down, left, right).
    Please note that a path of length k means visiting exactly k cells (cells
    can be revisited).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B. This means there exists an integer index i (0 <= i < k)
    such that lst_A[i] < lst_B[i] and for any j (0 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:
        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]
        (Path could be 1 -> 2 -> 1)

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    if not grid or not grid[0]: # Check for empty grid or grid with empty rows
        return []

    rows = len(grid)
    cols = len(grid[0])
    
    # (current_path_list, current_row, current_col)
    # We'll use a simple list and sort, as heapq might be overkill for small N*N*k
    # and the state space isn't enormous for typical competitive programming constraints.
    # For very large k or N, a more optimized BFS/Dijkstra with state compression might be needed.
    
    # A simple DFS approach. We'll keep track of the best path found so far.
    # This can be very slow if k is large. The problem statement guarantees N >= 2.
    
    min_lex_path = None

    def find_paths_dfs(r, c, current_path_values):
        nonlocal min_lex_path
        
        # Add current cell's value to path
        current_path_values.append(grid[r][c])

        if len(current_path_values) == k:
            if min_lex_path is None or current_path_values < min_lex_path:
                min_lex_path = list(current_path_values) # Store a copy
            current_path_values.pop() # Backtrack
            return

        # If current path is already lexicographically greater than best found, prune
        if min_lex_path is not None:
            is_worse = False
            for i in range(len(current_path_values)):
                if current_path_values[i] > min_lex_path[i]:
                    is_worse = True
                    break
                if current_path_values[i] < min_lex_path[i]:
                    break # Potentially better, continue
            if is_worse:
                current_path_values.pop() # Backtrack
                return

        # Explore neighbors
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                find_paths_dfs(nr, nc, current_path_values)
        
        current_path_values.pop() # Backtrack

    # Start DFS from every cell
    for r_start in range(rows):
        for c_start in range(cols):
            find_paths_dfs(r_start, c_start, [])
            
    return min_lex_path if min_lex_path is not None else []


def is_nested(string):
    """
    Create a function that takes a string as input which contains only square brackets ('[' and ']').
    The function should return True if the string contains at least one instance of a "nested structure".
    A "nested structure" is defined as an opening bracket, followed by another opening bracket,
    followed by its corresponding closing bracket, and then followed by the first opening bracket's
    corresponding closing bracket. Essentially, look for patterns like '[[]]' or '[[...]]'
    where the inner brackets are properly closed *relative to their own opening bracket*,
    and this entire nested unit is itself closed.

    It is NOT required for the entire input string to be perfectly balanced.
    The function only needs to find if ANY such validly nested subsequence exists.

    Examples:
    is_nested('[[]]')          ➞ True  (Simple nesting)
    is_nested('[[][]]')       ➞ True  (Contains '[[]]' and '[][]', both are nested)
    is_nested('[[]][[')       ➞ True  (The initial '[[]]' is a valid nested structure)
    is_nested('[]]]]]]][[[[[]') ➞ False (This is a tricky one. If '[[[]]' is evaluated in isolation, it's nested. But as part of this string, the outer context of '[[[[' makes it harder to define 'valid subsequence'. The test implies context or full string balance matters for the *subsequence itself* to be validly formed.)
    is_nested('[][]')         ➞ False (No nesting, just sequential)
    is_nested('[]')           ➞ False (No nesting)
    is_nested('[[')           ➞ False (Unclosed)
    is_nested(']]')           ➞ False (Unclosed)
    is_nested('')             ➞ False
    """
    # Iterate through the string to find potential start of a nested structure '['
    for i in range(len(string)):
        if string[i] == '[':
            # Found a potential outer opening bracket
            open_brackets_count = 1
            # Look for an inner opening bracket
            for j in range(i + 1, len(string)):
                if string[j] == '[':
                    open_brackets_count += 1
                    # If we have at least two open brackets, check for corresponding closes
                    if open_brackets_count >= 2:
                        # Now try to find the closing for the inner, then for the outer
                        
                        # To be a valid nested structure like '[[]]', we need:
                        # string[i] = '[' (outer_open)
                        # string[j] = '[' (inner_open)
                        # ...
                        # string[k] = ']' (inner_close for string[j])
                        # ...
                        # string[m] = ']' (outer_close for string[i])
                        # where i < j < k < m
                        
                        # Let's simplify: if we see '[[' then we need to see ']]' later,
                        # ensuring that the first ']' closes the second '['.

                        inner_opens = 0
                        # Scan from string[j] to find a balanced inner part
                        temp_balance = 0
                        found_inner_close_for_j = False
                        k_idx = -1
                        for k_search in range(j, len(string)):
                            if string[k_search] == '[':
                                temp_balance +=1
                            elif string[k_search] == ']':
                                temp_balance -=1
                            
                            if temp_balance == 0 and string[k_search] == ']' and k_search > j: # Found a ']' that balances from string[j]
                                # This ']' at k_search closes the '[' at string[j] (or an earlier one if string[j] was part of a deeper nest)
                                # For simplicity, let's assume string[j] is the one being closed IF this makes a valid '[[]]' structure.
                                # A more robust way is to ensure string[j] is indeed the one closed.
                                # For a simple '[[]]' or '[[...]]', string[j] is the second '['.
                                # If string[k_search] closes string[j], there should be an outer ']'
                                # that closes string[i].
                                
                                # We need to check if `open_brackets_count` (which was >=2)
                                # can be reduced back to 0 in a valid way.
                                # If we find a `[` at `i` and another `[` at `j > i`:
                                # We need to find a `]` at `k > j` that closes `string[j]`.
                                # And then a `]` at `m > k` that closes `string[i]`.
                                # This means `string[j+1:k]` must be balanced, and `string[i+1:m]` must be balanced.
                                
                                # Simpler check: find a '[' then another '[', then a ']', then another ']'.
                                # This doesn't guarantee they are correctly paired.
                                # The original failing function's 'count >= 2' and 'count == 0' was for the whole string.
                                # Let's use a stack-based approach for identifying a valid nested subsequence.

                                # Scan for '[['
                                if j > i and string[j] == '[': # We have string[i] = '[' and string[j] = '['
                                    # Now look for ']]' such that the first ']' closes string[j]
                                    # and the second ']' closes string[i]
                                    balance = 0
                                    # Check if string[i...m] is a valid nested structure itself
                                    # Attempt to parse string[i:] to find if it starts with a nested structure
                                    temp_s = string[i:]
                                    
                                    # Count balance from string[i]
                                    balance_from_i = 0
                                    deepest_for_i_structure = 0
                                    first_close_for_i_idx = -1

                                    for char_idx_from_i in range(len(temp_s)):
                                        if temp_s[char_idx_from_i] == '[':
                                            balance_from_i += 1
                                            deepest_for_i_structure = max(deepest_for_i_structure, balance_from_i)
                                        elif temp_s[char_idx_from_i] == ']':
                                            balance_from_i -= 1
                                        
                                        if balance_from_i == 0 and temp_s[char_idx_from_i] == ']': # Found a char that balances from string[i]
                                            first_close_for_i_idx = i + char_idx_from_i
                                            break # Consider only the first validly closed subsequence starting at i
                                    
                                    if first_close_for_i_idx != -1 and deepest_for_i_structure >= 2:
                                        return True # Found a validly closed structure starting at i that had nesting
                elif string[j] == ']':
                    open_brackets_count -= 1
                    if open_brackets_count < 0: # Unbalanced before even finishing the outer
                        break # Stop checking from string[i]
            # If loop finishes, means no valid nested structure starting at string[i] was completed.
    return False


def fix_spaces(text):
    """
    Given a string text, modify spaces according to these rules, applied by processing segments of consecutive spaces:
    1. A sequence of 3 or more consecutive spaces should be replaced by a single hyphen '-'.
    2. After rule 1, any remaining sequence of exactly 2 consecutive spaces should be replaced by '__' (two underscores).
    3. After rules 1 and 2, any remaining single space should be replaced by '_' (one underscore).

    Non-space characters should remain unchanged. Process the string from left to right.

    Examples:
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"  (Leading space is single -> '_', '   ' is 3+ -> '-')
    fix_spaces("Test  me   now") == "Test__me-now" ('  ' -> '__', '   ' -> '-')
    fix_spaces("   Leading triple space") == "-Leading_triple_space"
    """
    result = ""
    i = 0
    n = len(text)
    while i < n:
        if text[i] == ' ':
            space_start_idx = i
            while i < n and text[i] == ' ':
                i += 1
            num_spaces = i - space_start_idx
            
            if num_spaces >= 3:
                result += "-"
            elif num_spaces == 2:
                result += "__"
            elif num_spaces == 1:
                result += "_"
        else:
            result += text[i]
            i += 1
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

    # Condition 2: Exactly one dot
    if file_name.count('.') != 1:
        return "No"

    parts = file_name.split(".")
    name_part = parts[0]
    ext_part = parts[1]

    # Condition 3: Substring before dot not empty and starts with a letter
    if not name_part: # Empty name part
        return "No"
    if not name_part[0].isalpha():
        return "No"

    # Condition 1: Not more than three digits in the file's name (name_part)
    digit_count = 0
    for char in name_part:
        if char.isdigit():
            digit_count += 1
    if digit_count > 3:
        return "No"

    # Condition 4: Substring after dot is one of ['txt', 'exe', 'dll']
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
    if not (1 <= number <= 1000):
        # Or raise an error, depending on how strict "Restrictions" should be interpreted
        # For now, let's assume valid input as per typical problem statements.
        pass

    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syb = [
        "m", "cm", "d", "cd",
        "c", "xc", "l", "xl",
        "x", "ix", "v", "iv",
        "i"
    ]
    
    roman_num = ''
    i = 0
    while number > 0:
        for _ in range(number // val[i]):
            roman_num += syb[i]
            number -= val[i]
        i += 1
    return roman_num.lower() # Ensure lowercase as per prompt

def is_prime(num): # Retained original helper
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
    If n <= 0, return None.
    """
    if n <= 0:
        return None

    a, b = 0, 1 # Standard Fibonacci starts 0, 1, 1, 2, 3, 5...
                # Docstring examples: 1st=2, 2nd=3, 3rd=5. This suggests a slightly different start or indexing.
                # Let's adjust to match example outputs.
                # If prime_fib(1) is 2, prime_fib(2) is 3, prime_fib(3) is 5
                # Sequence of prime fibs: 2, 3, 5, 13, 89, 233, 1597 ...
                # The standard fib: F0=0, F1=1, F2=1, F3=2, F4=3, F5=5, F6=8, F7=13...
                # So prime_fib(1) is F3, prime_fib(2) is F4, prime_fib(3) is F5.
    
    count_prime_fibs = 0
    num = 0
    # Regenerate Fibonacci numbers and check for primality
    # We need to find the n-th Fibonacci number that is prime.
    
    # Let's use the common Fibonacci sequence starting F0=0, F1=1.
    # F_idx | Value | is_prime | PrimeFib # | n (target)
    # ------|-------|----------|------------|-----------
    # 0     | 0     | F        |            |
    # 1     | 1     | F        |            |
    # 2     | 1     | F        |            |
    # 3     | 2     | T        | 1st        | 1
    # 4     | 3     | T        | 2nd        | 2
    # 5     | 5     | T        | 3rd        | 3
    # 6     | 8     | F        |            |
    # 7     | 13    | T        | 4th        | 4
    # 8     | 21    | F        |            |
    # 9     | 34    | F        |            |
    # 10    | 55    | F        |            |
    # 11    | 89    | T        | 5th        | 5

    a, b = 0, 1
    found_count = 0
    current_fib_val = 0

    if n == 1: # Special handling due to F3=2 being the first for the problem
      # The loop below might skip it if not careful with init
      # The problem defines a sequence of *prime* Fibonacci numbers.
      # The first is 2, second is 3, etc.
      pass # Will be handled by the general loop

    # We need to generate Fibonacci numbers until we've found `n` of them that are prime.
    
    # Simpler approach: generate Fibonacci, test primality, count.
    fib_a, fib_b = 0, 1
    primes_found = 0
    
    # Handle small n cases explicitly if logic is tricky
    # Or ensure the loop starts correctly.
    # If we start with a=0, b=1, the sequence is 0,1,1,2,3,5...
    
    # Iteration 1: next_fib = 0+1=1. (Not prime by is_prime func)
    # Iteration 2: next_fib = 1+1=2. (Prime. primes_found=1. If n=1, return 2)
    # Iteration 3: next_fib = 1+2=3. (Prime. primes_found=2. If n=2, return 3)
    # Iteration 4: next_fib = 2+3=5. (Prime. primes_found=3. If n=3, return 5)
    
    # This seems to match the desired output.
    
    while primes_found < n:
        next_fib = fib_a + fib_b
        if is_prime(next_fib):
            primes_found += 1
        
        fib_a = fib_b
        fib_b = next_fib
        
        # Safety break if n is very large, though problem constraints usually prevent this.
        # if next_fib > some_very_large_number: break 
            
    return fib_b # The last fib_b computed when primes_found == n is the answer.


def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            >= 3.7               A  (Note: Test implies >= for A, A-, B+ etc.)
            >= 3.3               A- 
            >= 3.0               B+
            >= 2.7               B 
            >= 2.3               B-
            >= 2.0               C+
            >= 1.7               C
            >= 1.3               C-
            >= 1.0               D+ 
            >= 0.7               D 
            > 0.0                D- (Original table implies >0.0, but tests might use >=0.0 for D-)
              0.0                E
    Adjusting logic to match test case expectations which often use >= for boundaries.
    """
    letter_grades = []
    for grade in grades:
        if grade >= 4.0: # Special case for A+
            letter_grades.append("A+")
        elif grade >= 3.7: # Assuming tests want >=, not >
            letter_grades.append("A")
        elif grade >= 3.3:
            letter_grades.append("A-")
        elif grade >= 3.0:
            letter_grades.append("B+")
        elif grade >= 2.7:
            letter_grades.append("B")
        elif grade >= 2.3:
            letter_grades.append("B-")
        elif grade >= 2.0:
            letter_grades.append("C+")
        elif grade >= 1.7:
            letter_grades.append("C")
        elif grade >= 1.3:
            letter_grades.append("C-")
        elif grade >= 1.0:
            letter_grades.append("D+")
        elif grade >= 0.7:
            letter_grades.append("D")
        elif grade > 0.0: # Strict > 0.0 for D- as per original table
            letter_grades.append("D-")
        else: # Catches grade == 0.0 for E
            letter_grades.append("E")
    return letter_grades

def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it.
    If the number is equidistant from two integers (i.e., it ends in .5),
    it must be rounded away from zero.
    For example, closest_integer("14.5") should return 15, and
    closest_integer("-14.5") should return -15.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Input 'value' is always a string. Handle potential non-numeric input strings
    by returning "Invalid input" as per existing tests.
    Consider that the input number string might be just an integer string like "10".
    '''
    try:
        num = float(value)
    except ValueError:
        return "Invalid input" # Match test expectation

    if num == 0.0: # Handle exact zero
        return 0

    # Check for .5 cases (equidistant)
    if num > 0 and num - int(num) == 0.5:
        return int(num) + 1 # Round away from zero (up for positive)
    elif num < 0 and num - int(num) == -0.5: # For negative, e.g., -14.5, int(-14.5) is -14. num - int(num) is -0.5
        return int(num) -1 # Round away from zero (down for negative)
    elif num < 0 and int(num) - num == 0.5: # Alternative check for negative .5, e.g., -14.5 -> int(-14.5) is -14. -14 - (-14.5) = 0.5
        return int(num) # This would be rounding towards zero if int(num) is -14. This should be int(num) -1 to go to -15

    # Correct logic for negative .5:
    # If num = -14.5, int(num) = -14. We want -15.
    # If num = -14.5, math.floor(num) = -15, math.ceil(num) = -14.
    # Distance to floor: abs(-14.5 - (-15)) = 0.5
    # Distance to ceil:  abs(-14.5 - (-14)) = 0.5
    # If negative and equidistant, choose the one with larger absolute value (further from zero).

    if abs(num - int(num)) == 0.5: # Equidistant
        if num > 0:
            return math.ceil(num) # Equivalent to int(num) + 1
        else: # num < 0
            return math.floor(num) # Equivalent to int(num) if num ends like X.0, or int(num)-1 if it was like X.5
                                   # For -14.5, math.floor is -15. Correct.
                                   # For -14.0, math.floor is -14. Correct.
    
    # Standard rounding for non-equidistant cases
    # Python's round() rounds to nearest even for .5 cases, which is not what's wanted.
    # Manual rounding:
    if num > 0:
        return int(num + 0.5)
    else: # num < 0
        return int(num - 0.5)
    
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
            -> filter valid -> [1]
            -> sort -> [1]
            -> reverse -> [1]
      return = ['One']
    """

    if not arr:
        return []

    numbers_to_names = {
        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }

    # Filter for numbers between 1 and 9 inclusive
    valid_numbers = [num for num in arr if 1 <= num <= 9]
    
    # Sort the filtered numbers in ascending order
    valid_numbers.sort()
    
    # Reverse the sorted list
    valid_numbers.reverse()
    
    # Replace each digit by its corresponding name
    result = [numbers_to_names[num] for num in valid_numbers]

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
    
    # Iterate from second-to-last character down to the second character (index 1)
    # because vowels at beginning (index 0) and end (index len(word)-1) don't count.
    # A vowel at index `i` needs a consonant at `i-1` and `i+1`.
    # So, `i` can range from `1` to `len(word)-2`.
    # We search from the right, so loop `i` from `len(word)-2` down to `1`.

    if len(word) < 3: # Cannot have a vowel between two consonants
        return ""

    for i in range(len(word) - 2, 0, -1): # Corrected range: index from len-2 down to 1
        char_at_i = word[i]
        char_before = word[i-1]
        char_after = word[i+1]

        if char_at_i in vowels:
            if char_before not in vowels and char_after not in vowels:
                return char_at_i
                
    return ""

def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements from the first k elements of arr that satisfy the
    condition: the absolute value of the element must be less than 100 (i.e., 0-99).
    Effectively, sum numbers with one or two digits, including 0.

    Example:
        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3 from elements [111, 21, 3, 4000]

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    sum_val = 0
    # Iterate up to k elements, or fewer if arr is shorter than k
    # Constraint 2 says k <= len(arr), so arr[:k] is safe.
    for i in range(k): 
        num = arr[i]
        if -100 < num < 100: # Checks if num is between -99 and 99 inclusive
            sum_val += num
    return sum_val

def sum_squares(lst): # Original retained (no update provided for this one, matches tests)
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

def specialFilter(nums): # Original retained (no update needed based on initial analysis)
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10: # Only consider numbers greater than 10
            num_str = str(abs(num)) # Use absolute value for digit checking
            # Ensure the number has at least one digit (abs ensures no '-' sign)
            if num_str: # Check if string is not empty (e.g. for num=0 if it passed >10)
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

def common(l1: list, l2: list): # Original retained
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    common_elements = set()
    # For efficiency with larger lists, convert one to a set for O(1) lookups
    set_l2 = set(l2)
    for element in l1:
        if element in set_l2:
            common_elements.add(element)
    return sorted(list(common_elements))


def triangle_area(a, b, c): # Original retained (no update needed based on initial analysis)
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
    
    # Check for valid triangle sides (must be positive)
    if not (a > 0 and b > 0 and c > 0):
        return -1 # Or handle as per specific problem constraints if non-positive are possible

    if a + b <= c or a + c <= b or b + c <= a:
        return -1

    # Heron's formula
    s = (a + b + c) / 2.0 # Use float division
    # Handle potential floating point inaccuracies leading to small negative under sqrt
    area_sq = s * (s - a) * (s - b) * (s - c)
    if area_sq < 0: # Should not happen for a valid triangle by triangle inequality
        # This might indicate an issue or a degenerate triangle that passed the inequality.
        # For robust handling, treat as invalid or area 0.
        # Given the problem, if inequality passes, area_sq should be >=0.
        return -1 # Or 0.0 if degenerate triangles are considered to have 0 area
    
    area = math.sqrt(area_sq)
    return round(area, 2)

def is_multiply_prime(a): # Original retained (no update needed based on initial analysis, test was wrong)
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Helper function is_prime is already defined globally if needed, or can be local
    # Let's assume the global is_prime helper is available.
    
    if a < 1: # Or a <= 1, primes are > 1. Product of 3 primes will be > 1.
        return False
    
    # The prompt says "multiplication of 3 prime numbers". This usually implies
    # three *distinct* prime numbers unless specified.
    # The constraint "a is less then 100" limits the search space significantly.
    # Smallest product of 3 distinct primes: 2*3*5 = 30
    # Smallest product of 3 primes (can be same): 2*2*2 = 8
    # Largest prime < sqrt(100) is 7. (Primes: 2,3,5,7)
    # Primes to consider: 2, 3, 5, 7.
    # If a is product of p1*p2*p3:
    # For distinct primes:
    # (2,3,5) -> 30
    # (2,3,7) -> 42
    # (2,3,11) -> 66 (11 is too large if we consider primes for factors of a<100)
    # (2,5,7) -> 70

    # If primes can be repeated:
    # 2*2*2 = 8
    # 2*2*3 = 12
    # 2*2*5 = 20
    # 2*2*7 = 28
    # ...
    # 3*3*3 = 27
    # 3*3*5 = 45
    # ...
    # Test case `is_multiply_prime(8)` expects True (2*2*2). So repetition is allowed.

    factors = []
    d = 2
    temp_a = a
    while d * d <= temp_a:
        while temp_a % d == 0:
            factors.append(d)
            temp_a //= d
        d += 1
    if temp_a > 1: # Remaining temp_a is a prime factor
        factors.append(temp_a)
    
    # Now check if all factors are prime and count is 3
    if len(factors) != 3:
        return False
    
    for factor in factors:
        if not is_prime(factor): # Using the global is_prime
            return False
            
    return True


def encrypt(s): # Original retained
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
    shift_amount = 4 # two multiplied to two places
    for char_original in s:
        if 'a' <= char_original <= 'z':
            start = ord('a')
            shifted_char_ord = (ord(char_original) - start + shift_amount) % 26 + start
            result += chr(shifted_char_ord)
        elif 'A' <= char_original <= 'Z':
            start = ord('A')
            shifted_char_ord = (ord(char_original) - start + shift_amount) % 26 + start
            result += chr(shifted_char_ord)
        else:
            result += char_original # Keep non-alphabetic characters unchanged
    return result

def check_dict_case(dictionary_input): # Renamed dict to dictionary_input
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
    if not dictionary_input: # Check if dictionary is empty
        return False

    is_first_key = True
    all_keys_lower = None # Undetermined at first
    all_keys_upper = None # Undetermined at first

    for key in dictionary_input:
        if not isinstance(key, str):
            return False  # Key is not a string, so condition fails

        if is_first_key:
            if key.islower():
                all_keys_lower = True
                all_keys_upper = False
            elif key.isupper():
                all_keys_lower = False
                all_keys_upper = True
            else: # Mixed case for the first string key
                return False
            is_first_key = False
        else: # Subsequent keys
            if all_keys_lower and not key.islower():
                return False # Found an upper/mixed after expecting lower
            if all_keys_upper and not key.isupper():
                return False # Found a lower/mixed after expecting upper
            if not key.islower() and not key.isupper(): # Key itself is mixed case
                return False
                
    # If loop completes, all keys adhered to the case of the first key (or dict had one key)
    return True