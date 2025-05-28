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
        2. 1 <= k <= len(arr)  (Your function should correctly process up to the k-th element or end of array if k is larger, but tests will adhere to k <= len(arr)).
    """
    sum_of_elements = 0
    for i in range(min(k, len(arr))):  # Important: use min to handle k > len(arr)
        if abs(arr[i]) < 100:
            sum_of_elements += arr[i]
    return sum_of_elements

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
    if not 2 <= base <= 9:
        raise ValueError("Base must be between 2 and 9, inclusive.")

    if x == 0:
        return "0"

    result = ""
    while x > 0:
        remainder = x % base
        result = str(remainder) + result  # Prepend to build the string
        x //= base

    return result

def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    IMPORTANT: If the absolute value of 'shift' is greater than the number of digits in x,
    the function MUST return the string representation of x with its digits reversed.
    Otherwise (if abs(shift) <= number of digits):
        - Perform a circular right shift. A positive 'shift' value means right shift.
        - A negative 'shift' value should be treated as a left circular shift.
          A left circular shift by `s` is equivalent to a right circular shift by `num_digits - s`.
        - A shift of 0 or a multiple of the number of digits should result in the original string.
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
    
    if abs(shift) >= num_digits:
        return x_str[::-1]  # Reverse the string
    
    shift = shift % num_digits  # Handle shifts larger than the number of digits
    
    if shift > 0:
        return x_str[-shift:] + x_str[:-shift]
    else:
        return x_str[shift:] + x_str[:shift]
    
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
    by returning an appropriate error indicator or raising a ValueError if specified by tests
    (though current tests don't check for invalid string input error raising,
    they expect "Invalid input" for "abc").
    Consider that the input number string might be just an integer string like "10".
    '''
    try:
        num = float(value)
        fractional_part = num - int(num)
        if fractional_part == 0.5:
            return int(num) + 1 if num > 0 else int(num) - 1
        elif fractional_part < 0.5:
            return int(num)
        else:
            return int(num) + 1
    except ValueError:
        return "Invalid input"
    
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
    for i in range(len(operand)):
        expression += str(operand[i])
        if i < len(operator):
            expression += operator[i]

    try:
        result = eval(expression)
        return int(result)
    except (ZeroDivisionError, SyntaxError, NameError) as e:
        raise ValueError(f"Invalid expression or operation: {e}")
    
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
    while i < len(text):
        if text[i] == ' ':
            count = 0
            j = i
            while j < len(text) and text[j] == ' ':
                count += 1
                j += 1
            if count >= 3:
                result += "-"
            elif count == 2:
                result += "__"
            elif count == 1:
                result += "_"
            i = j
        else:
            result += text[i]
            i += 1

    return result

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
    is_nested('[]]]]]]][[[[[]') ➞ False (While '[[]]' appears, the leading '[[[[' are unclosed before it, making it not part of a validly formed nested structure starting from an outer bracket in that context)
    is_nested('[][]')         ➞ False (No nesting, just sequential)
    is_nested('[]')           ➞ False (No nesting)
    is_nested('[[')           ➞ False (Unclosed)
    is_nested(']]')           ➞ False (Unclosed)
    is_nested('')             ➞ False
    """
    if not string:
        return False

    count = 0
    for i in range(len(string)):
        if string[i] == '[':
            count += 1
        elif string[i] == ']':
            count -= 1
        if count >= 2:
            # Check if the inner bracket is closed before the outer bracket is closed
            if string[i] == ']':
                inner_count = 0
                inner_end = -1
                for j in range(i - 1, -1, -1):
                  if string[j] == '[':
                      inner_count +=1
                  elif string[j] == ']':
                      inner_count -= 1
                  if inner_count == 0:
                    inner_end = j
                    break
                if inner_end != -1:
                    return True
    return False

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
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Return the first k elements (which are now the largest)
    return sorted(arr[:k])

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
    
    sorted_l = sorted(l)
    n = len(sorted_l)
    
    if n % 2 == 0:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2
    else:
        return sorted_l[n // 2]
    

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

    if not grid:
        return []

    rows = len(grid)
    cols = len(grid[0])
    
    min_path = []
    
    def find_paths(row, col, path, steps_left):
        nonlocal min_path
        
        path.append(grid[row][col])
        steps_left -= 1
        
        if steps_left == 0:
          if not min_path or path < min_path:
            min_path = path[:]
          return

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols:
              find_paths(new_row, new_col, path[:], steps_left)
        path.pop()  #Backtrack

    for row in range(rows):
        for col in range(cols):
            find_paths(row, col, [], k)

    return min_path

def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
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

    if not date or '-' not in date:
        return False
    
    parts = date.split('-')
    if len(parts) != 3:
        return False
    
    try:
        month, day, year = int(parts[0]), int(parts[1]), int(parts[2])
    except ValueError:
        return False
    
    if month < 1 or month > 12 or year <= 0:
        return False

    if month == 2:
        is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        if is_leap:
            max_days = 29
        else:
            max_days = 28
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
        max_days = 31
        
    if day < 1 or day > max_days:
        return False

    return True