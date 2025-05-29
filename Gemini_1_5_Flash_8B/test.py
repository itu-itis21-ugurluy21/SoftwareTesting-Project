#from code import *
from code import *
import unittest

# New added
class TestOddCount(unittest.TestCase):
    def test_odd_count_single_string(self):
        self.assertEqual(odd_count(['1234567']), ['the number of odd elements 4n the str4ng 4 of the 4nput.'])
        self.assertEqual(odd_count(['2468']), ['the number of odd elements 0n the str0ng 0 of the 0nput.'])
		
    def test_odd_count_multiple_strings(self):
        self.assertEqual(odd_count(['3', '11111111']), ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 8n the str8ng 8 of the 8nput.'])
        self.assertEqual(odd_count(['12', '345']), ['the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.'])

    def test_odd_count_empty_list(self):
        self.assertEqual(odd_count([]), [])  # Empty list case

    def test_odd_count_mixed_digits(self):
        self.assertEqual(odd_count(['123', '456', '789']), ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.'])

    # New unit tests
    def test_odd_count_zero(self):
        self.assertEqual(odd_count(['024680']),['the number of odd elements 0n the str0ng 0 of the 0nput.'])
    def test_odd_count_all_odd(self):
        self.assertEqual(odd_count(['13579']), ['the number of odd elements 5n the str5ng 5 of the 5nput.'])

# New added
class TestMaximum(unittest.TestCase):
    def test_maximum_positive(self):
        self.assertEqual(maximum([1, 2, 3, 4, 5], 3), [5, 4, 3])
        self.assertEqual(maximum([1, 2, 3, 4, 5], 2), [5, 4])

    def test_maximum_negative(self):
        self.assertEqual(maximum([-1, -2, -3, -4, -5], 3), [-1, -2, -3])
        self.assertEqual(maximum([-1, -2, -3, -4, -5], 2), [-1, -2])

    def test_maximum_mixed(self):
        self.assertEqual(maximum([-3, -4, 5], 3), [-4, -3, 5])
        self.assertEqual(maximum([-3, -4, 5], 2), [-3, 5])

    def test_maximum_duplicates(self):
        self.assertEqual(maximum([4, -4, 4], 2), [4, 4])


    def test_maximum_k_zero(self):
        self.assertEqual(maximum([1, 2, 3], 0), [])

    def test_maximum_k_equal_length(self):
        self.assertEqual(maximum([1, 2, 3], 3), [3, 2, 1])

    # New unit tests
    def test_maximum_all_same_elements(self):
        self.assertEqual(maximum([0, 0, 0, 0], 2), [0, 0])

    def test_maximum_k_bigger_than_array_length(self):
        self.assertEqual(maximum([0, 0, 0, 0], 5), [0, 0,0,0]) 

# New added
class TestAllPrefixes(unittest.TestCase):
    def test_all_prefixes_normal(self):
        self.assertEqual(all_prefixes("abc"), ["a", "ab", "abc"])
        self.assertEqual(all_prefixes("abcd"), ["a", "ab", "abc", "abcd"])

    def test_all_prefixes_empty(self):
        self.assertEqual(all_prefixes(""), [])

    def test_all_prefixes_single_char(self):
        self.assertEqual(all_prefixes("a"), ["a"])

    def test_all_prefixes_multiple_same_chars(self):
        self.assertEqual(all_prefixes("aaa"), ["a", "aa", "aaa"])
    
    # New unit tests
    def test_all_prefixes_numbers(self):
        self.assertEqual(all_prefixes("1234"), ["1", "12", "123", "1234"])  

    def test_all_prefixes_special_characters(self):
        self.assertEqual(all_prefixes("a!@#"), ["a", "a!", "a!@", "a!@#"]) 

# New added
class TestDoAlgebra(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(do_algebra(['+'], [2, 3]), 5)
        self.assertEqual(do_algebra(['+'], [10, 20]), 30)

    def test_subtraction(self):
        self.assertEqual(do_algebra(['-'], [5, 3]), 2)
        self.assertEqual(do_algebra(['-'], [20, 10]), 10)

    def test_multiplication(self):
        self.assertEqual(do_algebra(['*'], [2, 3]), 6)
        self.assertEqual(do_algebra(['*'], [5, 4]), 20)

    def test_multiple_operations(self):
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)
        self.assertEqual(do_algebra(['*', '-', '+'], [5, 3, 2, 1]), 6)

    def test_error_mismatched_lengths(self):
        with self.assertRaisesRegex(ValueError, "Operator and operand lists have incorrect lengths."):
            do_algebra(['+', '*'], [1, 2, 3])  # Incorrect length
        with self.assertRaisesRegex(ValueError, "Operator and operand lists have incorrect lengths."):
            do_algebra([], [1, 2])
    
    def test_error_division_by_zero(self):
        with self.assertRaisesRegex(ValueError, "Invalid expression or operation: division by zero"):
            do_algebra(['//'], [5, 0])
        with self.assertRaisesRegex(ValueError, "Invalid expression or operation: division by zero"):
            do_algebra(['//'], [10, 0, 5])

    def test_error_invalid_expression(self):
        with self.assertRaisesRegex(ValueError, "Invalid expression or operation: invalid syntax"):
            do_algebra(['+', '**'], [2, 3]) 
    
    # New unit tests
    def test_single_floor_division_returns_zero(self):
        self.assertEqual(do_algebra(['//'], [1,2]), 0)

# New added
class TestLargestDivisor(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(largest_divisor(15), 5)
        self.assertEqual(largest_divisor(12), 6)
        self.assertEqual(largest_divisor(20), 10)

    def test_edge_cases(self):
        self.assertEqual(largest_divisor(1), 1)  # Divisor of 1 is 1 # Test case yanlışmış
        self.assertEqual(largest_divisor(2), 1)  # Divisor of 2 is 1

    def test_large_number(self):
        self.assertEqual(largest_divisor(99), 33)

    def test_prime_number(self):
        self.assertEqual(largest_divisor(7), 1)

    # New unit tests
    def test_negative_numbers(self):
        self.assertEqual(largest_divisor(-7), 1)

    def test_zero(self):
        self.assertEqual(largest_divisor(0), 1)

# New added
class TestChangeBase(unittest.TestCase):
    def test_decimal_to_base3(self):
        self.assertEqual(change_base(8, 3), "22")
        self.assertEqual(change_base(10, 3), "101")

    def test_decimal_to_base2(self):
        self.assertEqual(change_base(8, 2), "1000")
        self.assertEqual(change_base(7, 2), "111")

    def test_decimal_to_base5(self):
        self.assertEqual(change_base(12, 5), "22")
        self.assertEqual(change_base(25, 5), "100")

    def test_zero_input(self):
        self.assertEqual(change_base(0, 2), "0")
        self.assertEqual(change_base(0, 5), "0")

    def test_invalid_base(self):
      with self.assertRaises(ValueError):
        change_base(10, 11) 

    # New unit tests
    def test_change_base_boundary_base(self):
        self.assertEqual(change_base(2, 2), "10")

    def test_change_base_nearly_boundary_base(self):
        self.assertEqual(change_base(1, 2), "1")

# New added
class TestMedian(unittest.TestCase):
    def test_odd_length(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)
        self.assertEqual(median([1, 5, 2, 8, 3]), 3)  # Another example
        self.assertEqual(median([1]), 1)  # Single element
	
    def test_even_length(self):
        self.assertEqual(median([3, 1, 2, 4, 5, 6]), 3.5)
        self.assertEqual(median([1, 2, 3, 4]), 2.5)  # Another example

    def test_empty_list(self):
        self.assertIsNone(median([]))

    def test_mixed_values(self):
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)
        self.assertEqual(median([100, -10, 0, 10, 5, 20]), 10.0)

    # New unit tests
    def test_only_negative_numbers(self):
        self.assertEqual(median([-1, -2, -3, -4]), -2.5)
    
    def test_all_same(self):
        self.assertEqual(median([1, 1, 1, 1]), 1) 

# New added
class TestCircularShift(unittest.TestCase):
    def test_positive_shifts(self):
        self.assertEqual(circular_shift(12, 1), "21")
        self.assertEqual(circular_shift(12345, 2), "45123")
        self.assertEqual(circular_shift(12345, 5), "51234")
        self.assertEqual(circular_shift(12345, 0), "12345")

    def test_negative_shifts(self):
        self.assertEqual(circular_shift(12, -1), "21")  # Negative shift is equivalent to positive
        self.assertEqual(circular_shift(12345, -2), "34512")  # Negative shift example
        self.assertEqual(circular_shift(12345, -5), "23451")
        self.assertEqual(circular_shift(123, -1), "312")

    def test_shift_greater_than_digits(self):
      self.assertEqual(circular_shift(123, 4), "312")
      self.assertEqual(circular_shift(123, 6), "312") #shift greater than digits

    def test_single_digit(self):
        self.assertEqual(circular_shift(5, 1), "5")
        self.assertEqual(circular_shift(5, 2), "5")

    # New unit tests
    def test_circular_zero_shift(self):
        self.assertEqual(circular_shift(123, 0), "123") 

    def test_circular_shift_same_as_digit_length(self):
        self.assertEqual(circular_shift(123, 3), "123")

# New added
class TestPluck(unittest.TestCase):
    def test_basic_examples(self):
        self.assertEqual(pluck([4, 2, 3]), [2, 1])
        self.assertEqual(pluck([1, 2, 3]), [2, 1])
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

    def test_no_even_numbers(self):
        self.assertEqual(pluck([1, 3, 5, 7]), [])
		
    def test_empty_array(self):
        self.assertEqual(pluck([]), [])

    def test_multiple_same_smallest_even(self):
        self.assertEqual(pluck([0, 2, 0, 4]), [0, 0])  # First occurrence of 0
        self.assertEqual(pluck([2, 4, 6]), [2, 0])  # Smallest even is 2
        
    def test_large_array(self):
        self.assertEqual(pluck([10,8, 6, 4, 2, 0]), [0, 5])

    def test_pluck_first_even_is_largest(self):
        self.assertEqual(pluck([0, 2, 4]), [0, 0])

    ###self added tests###
    def test_smallest_in_the_end(self):
        self.assertEqual(pluck([1,2,3,4,5,6,0]), [0,6])
    def test_all_same(self):
        self.assertEqual(pluck([2,2,2,2,2,2]), [2,0])

# New added
class TestEncode(unittest.TestCase):
    def test_basic_examples(self):
        self.assertEqual(encode("test"), "TGST")
        self.assertEqual(encode("This is a message"), "tHKS KS C MGSSCGG")

    def test_vowels_upper(self):
        self.assertEqual(encode("AEIOU"), "CGIKU")
        self.assertEqual(encode("HELLO"), "hELLo")

    def test_vowels_lower(self):
        self.assertEqual(encode("aeiou"), "CGIKU")
		
    def test_no_vowels(self):
        self.assertEqual(encode("bcdfghjklmnpqrstvwxyz"), "BCDFGHJKLMNPQRSTVWXYZ")
        self.assertEqual(encode("BCDFGHJKLMNPQRSTVWXYZ"), "bcdfghjklmnpqrstvwxyz")

    def test_mixed_case_and_no_vowels(self):
        self.assertEqual(encode("ThIs Is a TeSt"), "tHKS ks c tgst")

    # New unit tests
    def test_encode_with_nonletters(self):
        self.assertEqual(encode("t1e2st-"), "T1G2ST-")

    def test_encode_with_boundary_letters(self):
        self.assertEqual(encode("azAZ"), "CZcz")  

class TestValidDate(unittest.TestCase):
    def test_valid_dates(self):
        self.assertTrue(valid_date("03-11-2000"))
        self.assertTrue(valid_date("06-04-2020"))
        self.assertTrue(valid_date("01-31-2024")) #Example of 31st day in month 1.
        self.assertTrue(valid_date("02-29-2024")) #Example of a leap year February 29th date.

    def test_invalid_dates(self):
        self.assertFalse(valid_date("15-01-2012"))  # Invalid day
        self.assertFalse(valid_date("04-0-2040"))  # Invalid day
        self.assertFalse(valid_date("13-04-2024"))  # Invalid month
        self.assertFalse(valid_date("02-30-2024"))  # Invalid day in February
        self.assertFalse(valid_date("02-30-2024"))
        self.assertFalse(valid_date("04-31-2024")) # Example of invalid day in April
        self.assertFalse(valid_date("02-29-2023")) # Example of invalid day for non-leap year


    def test_empty_string(self):
        self.assertFalse(valid_date(""))  # Empty string


    def test_invalid_format(self):
      self.assertFalse(valid_date("04/05/2024"))  # Incorrect format

# New Added
class TestIntersection(unittest.TestCase):
    def test_positive_intersections(self):
        self.assertEqual(intersection((1, 3), (2, 4)), "NO")  # Intersection is (2, 3) - length 1
        self.assertEqual(intersection((1, 5), (3, 6)), "YES")  # Intersection is (3, 5) - length 3
        self.assertEqual(intersection((1, 10), (5, 8)), "YES") # Intersection (5, 6) length 2
        self.assertEqual(intersection((1, 10), (11, 15)), "NO") # No intersection.

    def test_no_intersection(self):
        self.assertEqual(intersection((1, 5), (6, 10)), "NO")  # No overlap

    def test_one_interval_inside_another(self):
      self.assertEqual(intersection((1, 10), (5, 5)), "NO") # One point intersection.
      self.assertEqual(intersection((1,10), (2,9)), "YES") # Intersection (2, 9) = Length 8.

    def test_length_one(self):
      self.assertEqual(intersection((1, 3), (3,3)), "YES")  # Length is 1, which is not prime

    def test_length_zero(self):
      self.assertEqual(intersection((1, 3), (4, 5)), "NO")  # Length is 0

    # New Unit tests
    def test_intersection_negative_ranges(self):
        self.assertEqual(intersection((-5, -1), (-3, -2)), "NO")
    
    def test_intersection_mixed_ranges(self):
        self.assertEqual(intersection((-5, -1), (-3, 2)), "YES") 

class TestMinPath(unittest.TestCase):
    def test_small_grid(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(minPath(grid, 3), [1, 2, 3])
        self.assertEqual(minPath(grid, 4), [1, 2, 3, 4])


    def test_not_found(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(minPath(grid, 5), [])  # Path of length 5 not found
        grid2 = [[1]]
        self.assertEqual(minPath(grid2, 1), [1])


    def test_corner_cases(self):
        grid = [[1,2],[3,4]]
        self.assertEqual(minPath(grid, 2), [1, 2])
        self.assertEqual(minPath(grid, 3), [1,2,3])
        grid3 = [[1, 2,3], [4, 5,6], [7,8,9]]
        self.assertEqual(minPath(grid3, 1), [1])

    def test_empty_grid(self):
      self.assertEqual(minPath([], 1), []) #Test with empty grid
      self.assertEqual(minPath([[1]], 1), [1])

# New added
class TestIsNested(unittest.TestCase):
    def test_nested_subsequences(self):
        self.assertTrue(is_nested("[[]]"))
        self.assertTrue(is_nested("[[][]]"))
        self.assertTrue(is_nested("[[]][["))  # Another nested example

    def test_no_nested_subsequences(self):
        self.assertFalse(is_nested("[]]]]]]][[[[[]"))
        self.assertFalse(is_nested("[][]"))
        self.assertFalse(is_nested("[]"))  # No nesting
        self.assertFalse(is_nested("[[ ]]"))

    def test_unbalanced(self):
        self.assertFalse(is_nested("[[["))
        self.assertFalse(is_nested("]]]"))
        self.assertFalse(is_nested("]["))

    def test_empty_string(self):
        self.assertFalse(is_nested("")) 

    # New Unit tests
    def test_is_nested_multiple_levels(self):
        self.assertTrue(is_nested("[[[[]]]]")) 

# New added
class TestFixSpaces(unittest.TestCase):
    def test_basic_examples(self):
        self.assertEqual(fix_spaces("Example"), "Example")
        self.assertEqual(fix_spaces("Example 1"), "Example_1")
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")


    def test_multiple_spaces(self):
        self.assertEqual(fix_spaces("   Example   "), "---Example---")
        self.assertEqual(fix_spaces("  "), "--")


    def test_leading_and_trailing_spaces(self):
        self.assertEqual(fix_spaces("   Example"), "---Example")
        self.assertEqual(fix_spaces("Example   "), "Example---")
		
    def test_internal_consecutive_spaces(self):
        self.assertEqual(fix_spaces("Example  one   two"), "Example__one-two")

    def test_empty_string(self):
        self.assertEqual(fix_spaces(""), "")

    # New Unit tests
    def test_fix_spaces_two_spaces(self):
        self.assertEqual(fix_spaces("  "), "__") 

    def test_fix_spaces_three_spaces(self):
        self.assertEqual(fix_spaces("   "), "-") 

# New added
class TestFileNameCheck(unittest.TestCase):
    def test_valid_file_names(self):
        self.assertEqual(file_name_check("example.txt"), "Yes")
        self.assertEqual(file_name_check("MyFile.txt"), "Yes")
        self.assertEqual(file_name_check("a123.exe"), "Yes")
        self.assertEqual(file_name_check("valid_name.dll"), "Yes") #Valid with letters, number
        self.assertEqual(file_name_check("myFile.exe"), "Yes")

    def test_invalid_file_names(self):
        self.assertEqual(file_name_check("1example.txt"), "No")  # Starts with a digit
        self.assertEqual(file_name_check("example.doc"), "No")  # Invalid extension
        self.assertEqual(file_name_check("invalid..txt"), "No")  # Multiple dots
        self.assertEqual(file_name_check(".txt"), "No")  # Empty name part
        self.assertEqual(file_name_check("12345example.txt"), "No")  # More than 3 digits
        self.assertEqual(file_name_check("123example"), "No")  # Missing extension
        self.assertEqual(file_name_check("..txt"), "No")
        self.assertEqual(file_name_check("1234.txt"), "No")

    def test_empty_string(self):
      self.assertEqual(file_name_check(""), "No")

    # New Unit tests
    def test_wrong_extension(self):
        self.assertEqual(file_name_check("abc.png"), "No")
        self.assertEqual(file_name_check("abc.pdf"), "No")
        self.assertEqual(file_name_check("abc.jpeg"), "No")

    def test_invalid_starting_letter(self):
        self.assertEqual(file_name_check("1abc.png"), "No")
        self.assertEqual(file_name_check("-abc.pdf"), "No")
        self.assertEqual(file_name_check(" abc.pdf"), "No")

    def test_exactly_three_numbers(self):
        self.assertEqual(file_name_check("abc123.exe"), "Yes")

# New added
class TestIntToMiniRoman(unittest.TestCase):
    def test_basic_conversions(self):
        self.assertEqual(int_to_mini_roman(19), "xix")
        self.assertEqual(int_to_mini_roman(152), "clii")
        self.assertEqual(int_to_mini_roman(426), "cdxxvi")
        self.assertEqual(int_to_mini_roman(1000), "m")

    def test_smaller_numbers(self):
        self.assertEqual(int_to_mini_roman(1), "i")
        self.assertEqual(int_to_mini_roman(4), "iv")
        self.assertEqual(int_to_mini_roman(9), "ix")


    def test_larger_numbers(self):
        self.assertEqual(int_to_mini_roman(99), "xcix")
        self.assertEqual(int_to_mini_roman(499), "cdxcvi")
        self.assertEqual(int_to_mini_roman(890), "DCCCXC")
        self.assertEqual(int_to_mini_roman(895), "DCCCXCV")


    def test_boundary_cases(self):
        self.assertEqual(int_to_mini_roman(1), "i")  # Single digit
        self.assertEqual(int_to_mini_roman(1000), "m") # Maximum number

    # New unit test
    def test_int_to_mini_roman_all_symbols(self):
        self.assertEqual(int_to_mini_roman(944), "cmxliv")

# New Added
class TestPrimeFib(unittest.TestCase):
    def test_prime_fib_examples(self):
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 5)
        self.assertEqual(prime_fib(4), 13)  # 5th prime Fibonacci number.

    def test_prime_fib_larger_values(self):
        self.assertEqual(prime_fib(5), 89) #6th prime fibonacci number
        self.assertEqual(prime_fib(6), 233)  # 7th prime Fibonacci number

    def test_not_prime(self):
        self.assertEqual(prime_fib(7), 610)



# New Added
class TestSpecialFilter(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(specialFilter([15, 73, 14, 11]), 2)
        self.assertEqual(specialFilter([33, 45, 21, 109]), 2)
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)  # Example with negative numbers

    def test_single_digit_numbers(self):
        self.assertEqual(specialFilter([3, 7]), 0)
        self.assertEqual(specialFilter([1]), 0)  # Single-digit numbers
        
    def test_numbers_not_greater_than_ten(self):
        self.assertEqual(specialFilter([5, 11, 13]), 1) #Test case with numbers not greater than 10
        self.assertEqual(specialFilter([2, 12, 13]), 1)

    def test_empty_list(self):
        self.assertEqual(specialFilter([]), 0)  

    def test_numbers_less_than_or_equal_to_ten(self):
        self.assertEqual(specialFilter([1,2,11,13,15,17,9]), 4)

    # New Unit Tests
    def test_negative_numbers_ignored(self):
        self.assertEqual(specialFilter([-11, -33, -75, -44]), 0)

    def test_exactly_ten(self):
        self.assertEqual(specialFilter([10, 10, 10]), 0)  

# New Added
class TestNumericalLetterGrade(unittest.TestCase):

    def test_various_grades(self):
        grades = [4.0, 3.8, 3.4, 3.0, 2.8, 2.4, 2.0, 1.8, 1.4, 1.0, 0.8, 0.0]
        expected_grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "E"]
        self.assertEqual(numerical_letter_grade(grades), expected_grades)

    def test_single_grade(self):
        self.assertEqual(numerical_letter_grade([3.5]), ['B+'])

    def test_empty_list(self):
        self.assertEqual(numerical_letter_grade([]), [])

    def test_border_cases(self):
        grades = [3.7, 2.0, 0.7, 3.0, 0.0]
        expected = ['A', 'C+', 'D', 'B+', 'E']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_all_A_plus(self):
        grades = [4.0] * 5
        expected = ["A+"] * 5
        self.assertEqual(numerical_letter_grade(grades), expected),

    def test_grade_bigger_than_four(self):
        with self.assertRaises(ValueError):
            numerical_letter_grade([4.1])

    def test_grade_less_than_zero(self):
        with self.assertRaises(ValueError):
            numerical_letter_grade([-1])
        with self.assertRaises(ValueError):
            numerical_letter_grade([-15])

# New Added
class TestClosestInteger(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("15.3"), 15)
        self.assertEqual(closest_integer("14.5"), 15)  # Away from zero
        self.assertEqual(closest_integer("2.5"), 3)
        self.assertEqual(closest_integer("0.5"), 1) # Away from zero
    
    def test_negative_numbers(self):
        self.assertEqual(closest_integer("-10"), -10)
        self.assertEqual(closest_integer("-15.3"), -15)
        self.assertEqual(closest_integer("-14.5"), -15)  # Away from zero
        self.assertEqual(closest_integer("-2.5"), -2)
        self.assertEqual(closest_integer("-0.5"), 0) # Away from zero
    
    def test_zero(self):
      self.assertEqual(closest_integer("0"), 0)
      self.assertEqual(closest_integer("0.0"), 0)

    def test_invalid_input(self):
        self.assertEqual(closest_integer("abc"), "Invalid input")
        self.assertEqual(closest_integer(""), "Invalid input")

    # No new unit test

# New added
class TestByLength(unittest.TestCase):

    def test_valid_input(self):
        arr = [2, 1, 1, 4, 5, 8, 2, 3]
        expected = ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
        self.assertEqual(by_length(arr), expected)
    
    def test_empty_array(self):
        self.assertEqual(by_length([]), [])
    
    def test_invalid_numbers(self):
        arr = [1, -1, 55]
        expected = ["One"]
        self.assertEqual(by_length(arr), expected)
    
    def test_all_valid_numbers(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
        self.assertEqual(by_length(arr), expected)


    def test_duplicate_numbers(self):
        arr = [1, 1, 2, 2, 3, 3, 8, 8]
        expected = ["Eight", "Eight", "Three", "Three", "Two", "Two", "One", "One"]
        self.assertEqual(by_length(arr), expected)

    # New Unit Test
    def test_all_invalid_numbers(self):
        arr = [-1, 0, 10, 55, 1000]
        self.assertEqual(by_length(arr), [])


# New added
class TestGetClosestVowel(unittest.TestCase):

    def test_positive_cases(self):
        self.assertEqual(get_closest_vowel("yogurt"), "u")
        self.assertEqual(get_closest_vowel("FULL"), "U")
        self.assertEqual(get_closest_vowel("beautiful"), "e")  #added test
        self.assertEqual(get_closest_vowel("a"), "")
        self.assertEqual(get_closest_vowel("aeiou"), "")
        self.assertEqual(get_closest_vowel("oo"), "")
        self.assertEqual(get_closest_vowel("quick"), "")
        self.assertEqual(get_closest_vowel("ab"), "")  #added test
        self.assertEqual(get_closest_vowel("a"), "")
        self.assertEqual(get_closest_vowel(""), "")  #added test


    def test_edge_cases(self):
      self.assertEqual(get_closest_vowel("o"), "")
      self.assertEqual(get_closest_vowel("a"), "")
      self.assertEqual(get_closest_vowel("apple"), "e") #add test


    # New Unit Tests
    def test_case_sensitivity(self):
        self.assertNotEqual(get_closest_vowel("yogurt"), "U")
        self.assertEqual(get_closest_vowel("FULL"), "U")
    
    def test_vowel_not_between_consonants(self):
        self.assertEqual(get_closest_vowel("ear"), "")

# New added
class TestAddElements(unittest.TestCase):

    def test_positive_cases(self):
        arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
        k = 4
        self.assertEqual(add_elements(arr, k), 24)
        
        arr = [12, 34, 56, 78, 90]
        k = 5
        self.assertEqual(add_elements(arr,k), 260)

        arr = [1,2,3,4,5,6,7,8,9]
        k = 9
        self.assertEqual(add_elements(arr,k), 45)

        arr = [1,2,3,4,5,6]
        k = 6
        self.assertEqual(add_elements(arr,k), 21)


        arr = [10, 20, 30, 40, 50]
        k= 5
        self.assertEqual(add_elements(arr, k), 0)

    def test_negative_cases(self):
        arr = [-11, -21, -3, -4000, -5, -6, -7, -8, -9]
        k = 4
        self.assertEqual(add_elements(arr,k), -29)
    
    def test_zero(self):
      arr = [1, 0, 3, 100]
      k = 4
      self.assertEqual(add_elements(arr, k), 1) #Only 1 is counted


    # New Unit tests
    def test_three_digit_numbers(self):
        arr = [100, 999, 123]
        k = 3
        self.assertEqual(add_elements(arr, k), 0)

    def test_edge_digit_range(self):
        arr = [99, 100, -99, -100]
        k = 4
        self.assertEqual(add_elements(arr, k), 0) 

# New added 
class TestSumSquares(unittest.TestCase):

    def test_positive_cases(self):
        self.assertEqual(sum_squares([1, 2, 3]), 14)
        self.assertEqual(sum_squares([1, 4, 9]), 98)
        self.assertEqual(sum_squares([1, 3, 5, 7]), 84)
        self.assertEqual(sum_squares([1.4, 4.2, 0]), 29)
        self.assertEqual(sum_squares([2.9, 4.8, -1]), 32) # Added test
        self.assertEqual(sum_squares([2.1, 2.1, 2.9]), 20) # Added test case


    def test_negative_cases(self):
        self.assertEqual(sum_squares([-2.4, 1, 1]), 6)
        self.assertEqual(sum_squares([-1.1, 1.2, 2.9]), 14) # Added test case
        self.assertEqual(sum_squares([-5.4, -1.2, -2]), 28) # Added test case
    def test_zero(self):
        self.assertEqual(sum_squares([0, 0, 0]), 0)
        self.assertEqual(sum_squares([1, 0, 3.14]), 11)
    
    def test_mixed_types(self):
      with self.assertRaises(TypeError):
        sum_squares([1, "a", 3])

    # New Unit Test
    def test_rounding_to_ceiling(self):
        self.assertEqual(sum_squares([1.1, 1.000001, 1.000000000001]), 12)
        self.assertEqual(sum_squares([-1.1, -1.000000001]), 2)
        self.assertEqual(sum_squares([1.999999, 2.999999]), 4 + 9)

    def test_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

class TestCommon(unittest.TestCase):

    def test_positive_cases(self):
        l1 = [1, 4, 3, 34, 653, 2, 5]
        l2 = [5, 7, 1, 5, 9, 653, 121]
        expected = [1, 5, 653]
        self.assertEqual(common(l1, l2), expected)
    
        l1 = [5, 3, 2, 8]
        l2 = [3, 2]
        expected = [2, 3]
        self.assertEqual(common(l1, l2), expected)
    
        l1 = [1,2,3,4,5,6,7,8]
        l2 = [5,6,7,8,9,10,11]
        expected = [5,6,7,8]
        self.assertEqual(common(l1,l2),expected)


    def test_empty_lists(self):
        l1 = []
        l2 = [1, 2, 3]
        self.assertEqual(common(l1, l2), [])
        
        l1 = [1, 2, 3]
        l2 = []
        self.assertEqual(common(l1, l2), [])
    
        l1 = []
        l2 = []
        self.assertEqual(common(l1, l2), [])
    
    def test_no_common_elements(self):
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        self.assertEqual(common(l1, l2), [])

    def test_duplicates_in_lists(self):
        l1 = [1, 2, 2, 3, 4]
        l2 = [2, 2, 3, 5, 6]
        expected = [2, 3]
        self.assertEqual(common(l1,l2),expected)

class TestTriangleArea(unittest.TestCase):
    def test_valid_triangles(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.0)
        self.assertEqual(triangle_area(5, 12, 13), 30.0)
        self.assertEqual(triangle_area(8, 6, 7), 22.76) #A different example


    def test_invalid_triangles(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)
        self.assertEqual(triangle_area(1, 1, 1), 0.43) #Valid triangle
        self.assertEqual(triangle_area(1, 2, 3), -1) #Another invalid triangle
        self.assertEqual(triangle_area(7, 7, 1), -1) #Another invalid triangle

    def test_zero_and_negative_sides(self):
        self.assertEqual(triangle_area(0, 4, 5), -1) #Zero side.
        self.assertEqual(triangle_area(-1, 4, 5), -1) #Negative side.
    
    def test_float_input(self):
        self.assertEqual(triangle_area(1.0, 2.0, 2.0), 0.97)

class TestIsMultiplyPrime(unittest.TestCase):

    def test_positive_cases(self):
        self.assertTrue(is_multiply_prime(30))  # 2 * 3 * 5
        self.assertTrue(is_multiply_prime(42))  # 2 * 3 * 7
        self.assertTrue(is_multiply_prime(210)) # 2*3*5*7 (is not only 3 prime)
        self.assertTrue(is_multiply_prime(51)) # 3* 17


    def test_negative_cases(self):
        self.assertFalse(is_multiply_prime(25))  # 5*5
        self.assertFalse(is_multiply_prime(28))  # 2*2*7
        self.assertFalse(is_multiply_prime(12))  # 2 * 2 * 3
        self.assertFalse(is_multiply_prime(0))
        self.assertFalse(is_multiply_prime(1))


    def test_prime_number(self):
        self.assertFalse(is_multiply_prime(7))

# New added
class TestEncrypt(unittest.TestCase):

    def test_positive_cases(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')
    
    def test_mixed_case(self):
        self.assertEqual(encrypt("HeLlO"), "LiPpO")
    
    def test_non_alphabetic(self):
      self.assertEqual(encrypt("!@#$%^"), "!@#$%^")
      self.assertEqual(encrypt("Hello, world!"), "LiPpO, world!")
    def test_empty_string(self):
      self.assertEqual(encrypt(""), "")

    def test_large_input(self):
        self.assertEqual(encrypt("abcdefghijklmnopqrstuvwxyz"), "uvwxyzabcdefghijk"),
    def test_wrap_around(self):
        self.assertEqual(encrypt('zyxw'), 'cdef')
        self.assertEqual(encrypt('ZYXW'), 'CDEF')

# New added
class TestCheckDictCase(unittest.TestCase):
    def test_all_lower(self):
        self.assertTrue(check_dict_case({"a": "apple", "b": "banana"}))

    def test_all_upper(self):
        self.assertTrue(check_dict_case({"STATE": "NC", "ZIP": "12345"}))

    def test_mixed_case(self):
        self.assertFalse(check_dict_case({"a": "apple", "A": "banana", "B": "banana"}))
        self.assertFalse(check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}))

    def test_non_string_key(self):
        self.assertFalse(check_dict_case({"a": "apple", 8: "banana", "a": "apple"}))

    def test_empty_dict(self):
        self.assertFalse(check_dict_case({}))
	
    def test_one_key(self):
        self.assertTrue(check_dict_case({"a":"a"})) #Test case with single key
        self.assertTrue(check_dict_case({"A":"A"})) #Test case with single key (all upper)

    # Newly added unit tests #
    def test_mixed_strings(self):
        self.assertTrue(check_dict_case({"KEY-1231231": "1", "K123E123Y": 2, "K--123E12387Y": False}))
    
    def test_non_letters(self):
        self.assertFalse(check_dict_case({".*123": 1, "+12": 2, "1-2/3": 3}))
        

class TestCombinedOperations(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(combined_operations("Example"), "Example")
        self.assertEqual(combined_operations("Example 1"), "Example_1")
        self.assertEqual(combined_operations(" Example   3"), "Example-3")
        self.assertEqual(combined_operations("Yellow Yellow  Dirty  Fellow"), "Yellow_Yellow__Dirty__Fellow")


    def test_spaces_and_encoding(self):
      self.assertEqual(combined_operations("Exa   mple"), "Exa-mple")
      self.assertEqual(combined_operations("   Exa 1 2 2 mple"), "-Exa_1_2_2_mple")
      self.assertEqual(combined_operations("This is a message"), "tHKS_KS_C_MGSSCGG")
      self.assertEqual(combined_operations("   Hello   World"), "-Hello--World")



    def test_edge_case_encryption(self):
        self.assertEqual(combined_operations("hi"), "lm")
        self.assertEqual(combined_operations("et"), "ix")
        self.assertEqual(combined_operations("asdfghjkl"), "ewhjklnop")
        
    def test_empty_string(self):
        self.assertEqual(combined_operations(""), "")


    def test_non_string_input(self):
        self.assertEqual(combined_operations(123), "")