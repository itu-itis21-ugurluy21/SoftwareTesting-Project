import unittest
# Adjust the import path to where odd_count is defined
from GPT_o3.code import *     # ← replace with real module


class TestOddCount(unittest.TestCase):

    def test_all_even_digits(self):
        """String has no odd digits – expect zero everywhere."""
        self.assertEqual(
            odd_count(["2468024680"]),
            ["the number of odd elements 0n the str0ng 0 of the 0nput."]
        )

    def test_multiple_strings_mixed_counts(self):
        """List with various odd‐digit counts."""
        expected = [
            "the number of odd elements 3n the str3ng 3 of the 3nput.",
            "the number of odd elements 1n the str1ng 1 of the 1nput.",
            "the number of odd elements 3n the str3ng 3 of the 3nput."
        ]
        self.assertEqual(odd_count(["135", "2048", "999"]), expected)

    def test_single_digit_string(self):
        """Single odd digit should yield n = 1."""
        self.assertEqual(
            odd_count(["7"]),
            ["the number of odd elements 1n the str1ng 1 of the 1nput."]
        )

    def test_empty_string(self):
        """Empty string edge case – treat as having zero odd digits."""
        self.assertEqual(
            odd_count([""]),
            ["the number of odd elements 0n the str0ng 0 of the 0nput."]
        )
    ###self added tests###
    def test_6(self):
        self.assertEqual(
            odd_count(["012345"]),
            ["the number of odd elements 3n the str3ng 3 of the 3nput."]
        )
    def test_7(self):
        self.assertEqual(
            odd_count(["111111111111111"]),
            ["the number of odd elements 15n the str15ng 15 of the 15nput."]
        )

class TestMaximum(unittest.TestCase):

    def test_basic_mixed_numbers(self):
        """Typical case with positive, negative, and repeated values."""
        arr = [4, -4, 4, 10, 2]
        self.assertEqual(maximum(arr, 2), [4, 10])

    def test_all_elements_requested(self):
        """k == len(arr) should return the whole array sorted."""
        arr = [3, 1, 2]
        self.assertEqual(maximum(arr, 3), [1, 2, 3])

    def test_zero_requested(self):
        """k == 0 must yield an empty list."""
        self.assertEqual(maximum([5, 4, 3], 0), [])

    def test_with_negatives_and_duplicates(self):
        """Array contains negatives and duplicates; ensure correct ordering."""
        arr = [-5, -1, -3, -1, 0]
        # 3 largest are: -1, -1, 0  → sorted ascending
        self.assertEqual(maximum(arr, 3), [-1, -1, 0])
    ###self added tests###
    def test_6(self):
        self.assertEqual(maximum([1,1,1,1,1,1,1],3), [1,1,1])
    def test_7(self):
        self.assertEqual(maximum([1,1,1,1,1,1,1],15), [1,1,1,1,1,1,1])

class TestAllPrefixes(unittest.TestCase):

    def test_regular_string(self):
        """Standard multi-character string."""
        self.assertEqual(all_prefixes("abc"), ["a", "ab", "abc"])

    def test_single_character(self):
        """One-character input should return a one-element list."""
        self.assertEqual(all_prefixes("x"), ["x"])

    def test_repeated_characters(self):
        """Ensure each progressive slice is returned, even with duplicates."""
        self.assertEqual(
            all_prefixes("aaaa"),
            ["a", "aa", "aaa", "aaaa"]
        )

    def test_empty_string(self):
        """Empty input must yield an empty list."""
        self.assertEqual(all_prefixes(""), [])
    ###self added tests###
    def test_6(self):
        self.assertEqual(all_prefixes("ababab"), ["a","ab","aba","abab","ababa","ababab"])
    def test_7(self):
        self.assertEqual(all_prefixes("12ab"), ["1","12","12a","12ab"])

class TestDoAlgebra(unittest.TestCase):

    def test_sample_add_mul_sub(self):
        """Matches example: 2 + 3 * 4 - 5 = 9 (evaluated left-to-right)."""
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)

    def test_exponent_chain(self):
        """Left-to-right exponentiation differs from normal precedence."""
        # ((((2 ** 3) * 4) + 5) = 37)
        self.assertEqual(do_algebra(['**', '*', '+'], [2, 3, 4, 5]), 37)

    def test_floor_division(self):
        """Ensure integral floor division is handled."""
        self.assertEqual(do_algebra(['//', '*'], [7, 3, 4]), 8)  # (7 // 3)=2, 2*4=8

    def test_single_operator_mismatch(self):
        """Operator/operand length mismatch should raise ValueError."""
        with self.assertRaises(ValueError):
            do_algebra(['+'], [1])        # needs 2 operands for 1 operator

    def test_unknown_operator(self):
        """Unsupported operator symbol must raise an error."""
        with self.assertRaises(ValueError):
            do_algebra(['@'], [2, 3])
    ###self added tests###
    def test_6(self):
        self.assertEqual(do_algebra(['//'], [1,2]), 0)
    def test_7(self):
        self.assertEqual(do_algebra(['-'], [12,13]), -1)

class TestLargestDivisor(unittest.TestCase):

    def test_perfect_square(self):
        """Composite number whose largest proper divisor is its square-root."""
        self.assertEqual(largest_divisor(49), 7)

    def test_even_composite(self):
        """Largest divisor of an even composite should be n//2 (if n/2 is integer)."""
        self.assertEqual(largest_divisor(100), 50)

    def test_odd_composite(self):
        """Typical odd composite (15 → 5)."""
        self.assertEqual(largest_divisor(15), 5)

    def test_prime_number(self):
        """For a prime > 2, the only proper divisor is 1."""
        self.assertEqual(largest_divisor(13), 1)

    def test_two_edge_case(self):
        """n == 2 edge case – by definition returns 1."""
        self.assertEqual(largest_divisor(2), 1)
    ###self added tests###
    def test_6(self):
        self.assertEqual(largest_divisor(0), 1)
    def test_7(self):
        self.assertEqual(largest_divisor(1500), 750)
        
class TestChangeBase(unittest.TestCase):

    def test_examples_from_docstring(self):
        """Verify the examples provided in the function docstring."""
        self.assertEqual(change_base(8, 3), "22")
        self.assertEqual(change_base(8, 2), "1000")
        self.assertEqual(change_base(7, 2), "111")

    def test_zero_input(self):
        """x == 0 should return the string '0' irrespective of base."""
        for b in range(2, 10):
            self.assertEqual(change_base(0, b), "0")

    def test_max_base_9(self):
        """Convert a larger number to base-9."""
        # 100 in base-9 is 121 (since 1*81 + 2*9 + 1)
        self.assertEqual(change_base(100, 9), "121")

    def test_min_base_2_large(self):
        """Check binary representation of a multi-bit number."""
        # 255 → '11111111'
        self.assertEqual(change_base(255, 2), "11111111")

    def test_non_power_of_two_base(self):
        """Random value in base-7."""
        # 50 in base-7: 7^2=49 … remainder 1
        self.assertEqual(change_base(50, 7), "101")
    ###self added tests###
    def test_6(self):
        self.assertEqual(change_base(36, 6), "100")
    def test_7(self):
        self.assertEqual(change_base(17, 3), "122")

class TestMedian(unittest.TestCase):

    def test_odd_count(self):
        """List with odd length returns the central element."""
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)

    def test_even_count(self):
        """Even-length list returns the mean of the two middle elements."""
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 8.0)

    def test_with_negatives_and_duplicates(self):
        """Handles negative numbers and duplicates correctly."""
        self.assertEqual(median([7, -3, 7, 0, -3]), 0)

    def test_single_element(self):
        """Single-item list should simply return that item."""
        self.assertEqual(median([42]), 42)
    ###self added tests###
    def test_6(self):
        with self.assertRaises(ValueError):
            median([])
    def test_7(self):
        self.assertEqual(median([12,12,12,12]), 12)

class TestCircularShift(unittest.TestCase):

    def test_single_right_shift(self):
        """Normal right-shift by 1 within digit length."""
        self.assertEqual(circular_shift(12, 1), "21")

    def test_full_length_shift_returns_same(self):
        """Shift equal to digit count should yield original string."""
        self.assertEqual(circular_shift(12, 2), "12")

    def test_shift_exceeds_length_reverses(self):
        """If shift > digits, result should be reversed string."""
        self.assertEqual(circular_shift(97, 8), "79")

    def test_leading_zeros_preserved(self):
        """Ensure leading zeros after shift are kept as characters."""
        self.assertEqual(circular_shift(100, 2), "001")

    def test_no_shift(self):
        """Zero shift should leave the number unchanged."""
        self.assertEqual(circular_shift(54321, 0), "54321")

    #  Newly added unit tests #
    def test_nearly_full_shift(self):
        self.assertEqual(circular_shift(12345, 4), "23451")

    def test_negative_shift(self):
        self.assertEqual(circular_shift(123, -1), "231")

class TestPluck(unittest.TestCase):

    def test_single_smallest_even(self):
        """Simple list with one even candidate."""
        self.assertEqual(pluck([4, 2, 3]), [2, 1])

    def test_multiple_zeros(self):
        """Two zeros: choose the first occurrence (index 1)."""
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

    def test_no_even_numbers(self):
        """Return empty list when no evens are present."""
        self.assertEqual(pluck([7, 9, 13]), [])

    def test_empty_input(self):
        """Empty array → empty result."""
        self.assertEqual(pluck([]), [])

    def test_negative_and_positive_evens(self):
        """Handles negative evens; smallest even is -8 at index 3."""
        self.assertEqual(pluck([10, -2, 6, -8, 4]), [-8, 3])
    ###self added tests###
    def test_6(self):
        self.assertEqual(pluck([1,2,3,4,5,6,0]), [0,6])
    def test_7(self):
        self.assertEqual(pluck([2,2,2,2,2,2]), [2,0])

class TestEncode(unittest.TestCase):

    def test_basic_lowercase(self):
        """Simple word with lowercase letters only."""
        self.assertEqual(encode("test"), "TGST")

    def test_mixed_case_sentence(self):
        """Sentence with spaces and mixed casing."""
        self.assertEqual(encode("This is a message"), "tHKS KS C MGSSCGG")

    def test_all_vowels(self):
        """String containing only vowels (upper- and lower-case)."""
        self.assertEqual(encode("aeiouAEIOU"), "CGKQWcgkqw")

    def test_no_vowels(self):
        """String with no vowels should just swap case."""
        self.assertEqual(encode("BCDF"), "bcdf")

    def test_single_letter(self):
        """Edge case: one character."""
        self.assertEqual(encode("A"), "c")

    # Newly Added Test Cases #
    def test_edge_letters(self):
        self.assertEqual(encode("uU"), "Ww")


class TestByLength(unittest.TestCase):

    def test_example_from_docstring(self):
        """Matches the example provided in the docstring."""
        inp = [2, 1, 1, 4, 5, 8, 2, 3]
        expected = ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
        self.assertEqual(by_length(inp), expected)

    def test_with_strange_numbers(self):
        """Non-digit and out-of-range values are ignored."""
        inp = [1, -1, 55, 9, 0, 7]
        # keep [1, 7, 9] → sort desc → 9, 7, 1
        expected = ["Nine", "Seven", "One"]
        self.assertEqual(by_length(inp), expected)

    def test_empty_input(self):
        """Empty list should return an empty list."""
        self.assertEqual(by_length([]), [])

    def test_all_digits_one_through_nine(self):
        """All valid digits present once each."""
        inp = [1,2,3,4,5,6,7,8,9]
        # sort descending → 9 … 1
        expected = [
            "Nine","Eight","Seven","Six","Five",
            "Four","Three","Two","One"
        ]
        self.assertEqual(by_length(inp), expected)
    ###self added tests###
    def test_6(self):
        inp = [1, 100, 10, 5]
        expected = ["Five", "One"]
        self.assertEqual(by_length(inp), expected)
    def test_7(self):
        inp = [500, 100, 10, 300]
        expected = []
        self.assertEqual(by_length(inp), expected)

class TestGetClosestVowel(unittest.TestCase):

    def test_examples_from_prompt(self):
        """Verify the examples given in the original description."""
        self.assertEqual(get_closest_vowel("yogurt"), "u")
        self.assertEqual(get_closest_vowel("FULL"),   "U")
        self.assertEqual(get_closest_vowel("quick"),  "")
        self.assertEqual(get_closest_vowel("ab"),     "")

    def test_multiple_candidates_rightmost_returned(self):
        """When multiple vowels meet the rule, the right-most one is chosen."""
        # 'b a d e' : 'a' is between b/d, 'e' is at end (ignored) – expect 'a'
        self.assertEqual(get_closest_vowel("bade"), "a")
        # 'p a s t o r' : 'a' & 'o' both flanked, right-most is 'o'
        self.assertEqual(get_closest_vowel("pastor"), "o")

    def test_single_valid_in_middle(self):
        """Single valid pattern in the middle of the word."""
        self.assertEqual(get_closest_vowel("basket"), "e")

    def test_no_internal_vowel_between_consonants(self):
        """Word with vowels only at edges should return empty."""
        self.assertEqual(get_closest_vowel("apple"), "")   # 'a' and 'e' at edges only

    def test_short_words_return_empty(self):
        """Words shorter than three characters cannot satisfy the rule."""
        self.assertEqual(get_closest_vowel("a"), "")
        self.assertEqual(get_closest_vowel("to"), "")
    ###self added tests###
    def test_6(self):
        self.assertEqual(get_closest_vowel("car"), "a")
    def test_7(self):
        self.assertEqual(get_closest_vowel("hUmAn"), "A")

class TestAddElements(unittest.TestCase):

    def test_basic_mix(self):
        """Typical mix of small and large numbers, check first-k slice."""
        arr = [111, 21, 3, 4000, 5, 6]
        self.assertEqual(add_elements(arr, 4), 24)   # 21 + 3

    def test_all_small_with_negatives(self):
        """All first-k items meet the ≤2-digit rule, including negatives."""
        arr = [-9, 10, -50, 7]
        self.assertEqual(add_elements(arr, 4), -42)  # -9+10-50+7

    def test_none_qualify(self):
        """No element in first-k has ≤2 digits."""
        arr = [300, 4567, 123, 999]
        self.assertEqual(add_elements(arr, 3), 0)

    def test_k_equals_zero(self):
        """Edge case k == 0 should always return 0."""
        self.assertEqual(add_elements([1, 2, 3], 0), 0)
    ###self added tests###
    def test_6(self):
        arr = [300]
        self.assertEqual(add_elements(arr, 1), 0)
    def test_7(self):
        arr = [0,0,0,0,0,0]
        self.assertEqual(add_elements(arr, 5), 0)
    

class TestSumSquares(unittest.TestCase):

    def test_all_integers(self):
        """Pure integers should just square and sum."""
        self.assertEqual(sum_squares([1, 2, 3]), 14)      # 1²+2²+3²

    def test_positive_floats_round_up(self):
        """Floats are ceiled before squaring (1.4→2, 4.2→5)."""
        self.assertEqual(sum_squares([1.4, 4.2, 0]), 29)  # 2² + 5² + 0²

    def test_negatives_and_mixed(self):
        """Ceiling of a negative float (−2.4→−2) then squared."""
        self.assertEqual(sum_squares([-2.4, 1, 1]), 6)    # (−2)² + 1² + 1²

    def test_empty_list(self):
        """Empty input should return 0 (no elements to sum)."""
        self.assertEqual(sum_squares([]), 0)
    ###self added tests###
    def test_6(self):
        self.assertEqual(sum_squares([0.1,-0.1]), 1)
    def test_7(self):
        self.assertEqual(sum_squares([10,20,30]), 1400)

class TestSpecialFilter(unittest.TestCase):

    def test_examples_from_docstring(self):
        """Verify examples given in the function’s docstring."""
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)

    def test_mixed_values(self):
        """List with values greater than 10, but only some with odd first/last digits."""
        data = [17, 42, 131, 808, 99, 57]   # 17, 131, 99, 57 qualify → 4
        self.assertEqual(specialFilter(data), 4)

    def test_no_matches(self):
        """Return 0 when no element satisfies both conditions."""
        self.assertEqual(specialFilter([10, -11, 22, 8, 4]), 0)

    def test_edge_cases_and_negatives(self):
        """Numbers ≤10 or negative should never be counted."""
        data = [11, -15, 5, 1357, 20]  # Only 11 and 1357 ≥10, but 1357 last digit 7 -> qualifies, 11 qualifies
        self.assertEqual(specialFilter(data), 2)
    ###self added tests###
    def test_6(self):
        data = [31,-13,57] 
        self.assertEqual(specialFilter(data), 2)
    def test_7(self):
        data = [1,10,97] 
        self.assertEqual(specialFilter(data), 1)

class TestCommon(unittest.TestCase):

    def test_basic_overlap(self):
        """Typical input with several shared values and duplicates."""
        l1 = [1, 4, 3, 34, 653, 2, 5]
        l2 = [5, 7, 1, 5, 9, 653, 121]
        self.assertEqual(common(l1, l2), [1, 5, 653])

    def test_no_overlap(self):
        """Lists have no elements in common—expect empty list."""
        self.assertEqual(common([1, 2, 3], [4, 5, 6]), [])

    def test_all_overlap(self):
        """Every element appears in both lists; duplicates ignored."""
        self.assertEqual(common([4, 3, 2, 8], [3, 2, 4]), [2, 3, 4])

    def test_with_empty_list(self):
        """If either list is empty, result is empty."""
        self.assertEqual(common([4, 3, 2], []), [])
        self.assertEqual(common([], [1, 2, 3]), [])
    ###self added tests###
    def test_6(self):
        self.assertEqual(common([], [1,2,3]), [])
    def test_7(self):
        self.assertEqual(common([1,1,1,1,1], [1,1,2,3]), [1])

class TestTriangleArea(unittest.TestCase):

    def test_right_triangle(self):
        """3-4-5 right triangle should have area 6.00."""
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6.00, places=2)

    def test_equilateral_triangle(self):
        """Equilateral triangle with side 1 should have area ≈ 0.4330127019 → 0.43."""
        self.assertAlmostEqual(triangle_area(1, 1, 1), 0.43, places=2)

    def test_invalid_triangle(self):
        """Fails triangle inequality → returns -1."""
        self.assertEqual(triangle_area(1, 2, 10), -1)
        self.assertEqual(triangle_area(2, 6, 3), -1)

    def test_scalene_triangle(self):
        """Arbitrary valid triangle; verify area rounded to two decimals."""
        # sides 10, 5, 7  → s = 11, area = sqrt(11·1·6·4) = sqrt(264) ≈ 16.248...
        self.assertAlmostEqual(triangle_area(10, 5, 7), 16.25, places=2)
    ###self added tests###
    def test_6(self):
        self.assertAlmostEqual(triangle_area(0,10,100), -1)
    def test_7(self):
        self.assertAlmostEqual(triangle_area(5,12,13), 30.00, places=2)

class TestIsMultiplyPrime(unittest.TestCase):

    def test_examples_from_docstring(self):
        """Verify the three examples shown in the docstring."""
        self.assertTrue(is_multiply_prime(30))   # 2·3·5
        self.assertTrue(is_multiply_prime(8))    # 2·2·2
        self.assertFalse(is_multiply_prime(10))  # only two primes (2·5)

    def test_large_valid_product(self):
        """Product of three distinct primes."""
        self.assertTrue(is_multiply_prime(11 * 13 * 7))

    def test_too_many_prime_factors(self):
        """Has more than three prime factors (with multiplicity)."""
        self.assertFalse(is_multiply_prime(2 * 3 * 3 * 7))   # four factors

    def test_contains_composite_factor(self):
        """Includes a composite factor, e.g., 6 = 2·3, overall count > 3."""
        self.assertFalse(is_multiply_prime(3 * 6 * 7))       # factors = 3,2,7 → 4 primes

    def test_non_positive_and_prime_inputs(self):
        """Edge cases: numbers < 2 and a single prime."""
        self.assertFalse(is_multiply_prime(1))
        self.assertFalse(is_multiply_prime(0))
        self.assertFalse(is_multiply_prime(-30))
        self.assertFalse(is_multiply_prime(13))
    ###self added tests###
    def test_6(self):
        self.assertFalse(is_multiply_prime(13*17*15))   
    def test_7(self):
        self.assertFalse(is_multiply_prime(13*17*7*0)) 

class TestEncrypt(unittest.TestCase):

    def test_examples_from_docstring(self):
        """Check all examples listed in the function docstring."""
        self.assertEqual(encrypt("hi"), "lm")
        self.assertEqual(encrypt("asdfghjkl"), "ewhjklnop")
        self.assertEqual(encrypt("gf"), "kj")
        self.assertEqual(encrypt("et"), "ix")

    def test_wrap_around_z(self):
        """Letters near the end of alphabet should wrap correctly (w→a, z→d)."""
        self.assertEqual(encrypt("wxyz"), "abcd")

    def test_non_letters_preserved(self):
        """Characters outside a–z remain unchanged."""
        self.assertEqual(encrypt("a1.b!"), "e1.f!")

    def test_mixed_case_ignored(self):
        """Uppercase letters are not transformed (only lowercase handled)."""
        self.assertEqual(encrypt("AbCz"), "AbCd")

    def test_empty_string(self):
        """Edge case: empty input should return empty output."""
        self.assertEqual(encrypt(""), "")
    ###self added tests###
    def test_6(self):
        self.assertEqual(encrypt("a1b2C3"), "e1f2C3")
    def test_7(self):
        self.assertEqual(encrypt(".*123.*"), ".*123.*")

class TestCheckDictCase(unittest.TestCase):

    def test_all_lowercase_keys(self):
        """All-lowercase string keys → True."""
        self.assertTrue(check_dict_case({"a": 1, "b2": 3, "c_c": 4}))

    def test_all_uppercase_keys(self):
        """All-uppercase string keys → True."""
        self.assertTrue(check_dict_case({"KEY": 1, "ZIP": "12345"}))

    def test_mixed_case_keys(self):
        """Mixed lower & upper keys should return False."""
        self.assertFalse(check_dict_case({"a": 1, "B": 2, "c": 3}))

    def test_non_string_key(self):
        """Presence of any non-string key → False."""
        self.assertFalse(check_dict_case({"a": 1, 5: "x"}))

    def test_empty_dict(self):
        """Empty dictionary must return False."""
        self.assertFalse(check_dict_case({}))

    # Newly added unit tests #
    def test_mixed_strings(self):
        self.assertTrue(check_dict_case({"KEY-1231231": "1", "K123E123Y": 2, "K--123E12387Y": False}))
    
    def test_non_letters(self):
        self.assertFalse(check_dict_case({".*123": 1, "+12": 2, "1-2/3": 3}))
    

class TestValidDate(unittest.TestCase):

    def test_valid_dates(self):
        """Several correct dates in different months."""
        self.assertTrue(valid_date("03-11-2000"))   # March 11
        self.assertTrue(valid_date("06-04-2020"))   # June 4
        self.assertTrue(valid_date("02-29-1999"))   # Feb 29 (leap-year check not required)

    def test_invalid_day_for_month(self):
        """Day exceeds month’s max (30-Apr vs 31-Apr)."""
        self.assertFalse(valid_date("04-31-3000"))  # April has only 30 days

    def test_invalid_month_range(self):
        """Month outside 1–12 should be rejected."""
        self.assertFalse(valid_date("15-01-2012"))  # month 15 invalid

    def test_incorrect_format_or_missing_parts(self):
        """Wrong delimiter or missing fields should fail."""
        self.assertFalse(valid_date("06/04/2020"))  # uses '/' not '-'
        self.assertFalse(valid_date("2003-04"))     # missing day
        self.assertFalse(valid_date(""))            # empty string

    def test_non_numeric(self):
        """Non-numeric components must cause rejection."""
        self.assertFalse(valid_date("ab-cd-efgh"))
        self.assertFalse(valid_date("04-XX-2040"))
    ###self added tests###
    def test_6(self):
        self.assertFalse(valid_date("02-00-2012")) 
    def test_7(self):
        self.assertTrue(valid_date("02-29-1000")) 

class TestIntersection(unittest.TestCase):

    # ── 1. Sample cases taken from the explanation ────────────────────
    def test_examples_from_description(self):
        # Touching at a single point → length = 0  → "NO"
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")

        # Length 1 is not prime
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")

        # Length 2 (prime)  → "YES"
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

    # ── 2. Prime-length intersection (>2) ─────────────────────────────
    def test_positive_prime_length(self):
        # Overlap: (4,10) ∩ (7,13) = (7,10)  → length = 3 (prime)
        self.assertEqual(intersection((4, 10), (7, 13)), "YES")

    # ── 3. Composite-length intersection ──────────────────────────────
    def test_composite_length(self):
        # Overlap length = 4 (not prime)  → "NO"
        self.assertEqual(intersection((0, 9), (5, 13)), "NO")

    # ── 4. No intersection at all ─────────────────────────────────────
    def test_no_overlap(self):
        self.assertEqual(intersection((1, 2), (3, 4)), "NO")

    # ── 5. Identical intervals (length 1) ─────────────────────────────
    def test_identical_intervals(self):
        # (5,6) ∩ (5,6) → (5,6) length = 1 → "NO"
        self.assertEqual(intersection((5, 6), (5, 6)), "NO")

    # ── 6. Large prime length check ───────────────────────────────────
    def test_large_prime_length(self):
        # Overlap length = 17 (prime) → "YES"
        self.assertEqual(intersection((0, 20), (3, 20)), "YES")

    # ── 7. Large composite length check ───────────────────────────────
    def test_large_composite_length(self):
        # Overlap length = 18 (composite) → "NO"
        self.assertEqual(intersection((0, 20), (2, 20)), "NO")
    ###self added tests###
    def test_6(self):
        self.assertEqual(intersection((0, 0), (0, 0)), "NO")
    def test_7(self):
        self.assertEqual(intersection((100, 101), (99, 101)), "NO")

class TestMinPath(unittest.TestCase):

    def test_simple_3_by_3(self):
        """Grid from the prompt, k = 3 → [1,2,1]."""
        grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.assertEqual(minPath(grid, 3), [1, 2, 1])

    def test_neighbors_with_duplicate_min(self):
        """Two equal smallest neighbours – still deterministic (first value)."""
        grid = [
            [5, 9, 3],
            [4, 1, 6],
            [7, 8, 2],
        ]  # neighbours of 1 are 4,9,8,6 → min = 4
        self.assertEqual(minPath(grid, 1), [1])
        self.assertEqual(minPath(grid, 5), [1, 4, 1, 4, 1])

    def test_larger_grid_k_7(self):
        grid = [
            [6, 4, 13, 10],
            [5, 7, 12, 1],
            [3, 16, 11, 15],
            [8, 14, 9, 2],
        ]  # min neighbour of 1 is 10
        self.assertEqual(minPath(grid, 7), [1, 10, 1, 10, 1, 10, 1])

    def test_alternating_with_zero_min_neighbour(self):
        """Min neighbour happens to be 0 - make sure 0 alternates with 1."""
        grid = [
            [5, 0, 3],
            [2, 1, 4],
            [7, 8, 9],
        ]
        self.assertEqual(minPath(grid, 4), [1, 0, 1, 0])
    ###self added tests###
    def test_6(self):
        with self.assertRaises(TypeError):
            minPath([], 5)
    def test_7(self):
        grid = [
            [1, 0, 3],
            [2, 5, 4],
            [7, 8, 9],
        ]
        self.assertEqual(minPath(grid, 1), [1])

class TestIsNested(unittest.TestCase):

    def test_valid_nested_patterns(self):
        """Strings that clearly contain a ‘[[ ]]’ subsequence."""
        self.assertTrue(is_nested("[[]]"))
        self.assertTrue(is_nested("[[][]]"))          # nested deeper
        self.assertTrue(is_nested("[[]][["))          # pattern before trailing '['

    def test_no_nested_patterns(self):
        """Strings that do NOT contain a valid nested pattern."""
        self.assertFalse(is_nested("[]]]]]]][[[[[]"))  # mismatched groups
        self.assertFalse(is_nested("[][]"))            # adjacent pairs only
        self.assertFalse(is_nested("[]"))              # too short, no nesting
        self.assertFalse(is_nested(""))                # empty string

    def test_single_side_only(self):
        """All opens or all closes cannot form nesting."""
        self.assertFalse(is_nested("[[[[["))
        self.assertFalse(is_nested("]]]]]"))

    def test_mixed_but_touching_only(self):
        """Sequences like '[[]' (missing close) or '[]]' (extra close)."""
        self.assertFalse(is_nested("[[]"))
        self.assertFalse(is_nested("[]]"))

    def test_long_string_multiple_sections(self):
        """Complex string with both valid and invalid segments."""
        self.assertTrue(is_nested("[]][[]][][[[[]]]"))
    ###self added tests###
    def test_6(self):
        self.assertTrue(is_nested("[][[]]"))
    def test_7(self):
        self.assertFalse(is_nested("]]][]][]"))

class TestFixSpaces(unittest.TestCase):

    def test_examples_from_docstring(self):
        """Verify every example shown in the docstring."""
        self.assertEqual(fix_spaces("Example"), "Example")
        self.assertEqual(fix_spaces("Example 1"), "Example_1")
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")

    def test_leading_and_trailing_runs(self):
        """Runs of spaces at both ends follow the same rules."""
        self.assertEqual(fix_spaces("   text  "), "-text__")

    def test_mixed_lengths_in_one_string(self):
        """String containing 1-, 2-, and ≥3-space runs."""
        s = "a  b   c d    e"
        # 2→"__", 3→"-", 1→"_", 4→"-"
        self.assertEqual(fix_spaces(s), "a__b-c_d-e")

    def test_all_spaces(self):
        """String composed solely of spaces should collapse to '_' or '-'."""
        self.assertEqual(fix_spaces(" "), "_")
        self.assertEqual(fix_spaces("  "), "__")
        self.assertEqual(fix_spaces("   "), "-")
        self.assertEqual(fix_spaces("      "), "-")   # 6 spaces → one '-'

    def test_empty_string(self):
        """Empty input should return empty output."""
        self.assertEqual(fix_spaces(""), "")
    ###self added tests###
    def test_6(self):
        self.assertEqual(fix_spaces(" a a  a   a"), "_a_a__a-a")
    def test_7(self):
        self.assertEqual(fix_spaces("asdfg"), "asdfg")

class TestFileNameCheck(unittest.TestCase):

    def test_valid_examples(self):
        """Typical valid file names that satisfy every rule."""
        self.assertEqual(file_name_check("example.txt"), "Yes")
        self.assertEqual(file_name_check("K.dll"), "Yes")
        self.assertEqual(file_name_check("MY16FILE3.exe"), "Yes")   # three digits
        self.assertEqual(file_name_check("no_one#knows.dll"), "Yes")

    def test_bad_extension_or_dot_count(self):
        """Incorrect extension or wrong number of dots."""
        self.assertEqual(file_name_check("this_is_valid.wow"), "No")  # invalid ext
        self.assertEqual(file_name_check("all.exe.txt"), "No")        # two dots
        self.assertEqual(file_name_check("final132"), "No")           # no dot

    def test_too_many_digits_or_bad_start(self):
        """Base-name starts incorrectly or contains >3 digits."""
        self.assertEqual(file_name_check("1example.dll"), "No")       # starts with digit
        self.assertEqual(file_name_check("His12FILE94.exe"), "No")    # 4 digits
        self.assertEqual(file_name_check("_Y.txt"), "No")             # starts with underscore

    def test_empty_or_missing_parts(self):
        """Edge cases: empty base or missing pieces."""
        self.assertEqual(file_name_check(".txt"), "No")     # empty base
        self.assertEqual(file_name_check("s."), "No")       # missing extension
        self.assertEqual(file_name_check(""), "No")         # empty string

    def test_non_string_characters_allowed(self):
        """Ensure unusual but valid characters (underscores, #) are allowed."""
        self.assertEqual(file_name_check("Weird#Name_3.dll"), "Yes")
    ###self added tests###
    def test_6(self):
        self.assertEqual(file_name_check("Android."), "No")
    def test_7(self):
        self.assertEqual(file_name_check("A__*12b.exe"), "Yes")

class TestIntToMiniRoman(unittest.TestCase):

    def test_examples_from_docstring(self):
        """Verify all values shown in the function’s docstring."""
        self.assertEqual(int_to_mini_roman(19),  "xix")
        self.assertEqual(int_to_mini_roman(152), "clii")
        self.assertEqual(int_to_mini_roman(426), "cdxxvi")

    def test_small_and_boundary_values(self):
        """Check minimum value 1 and important subtractive cases."""
        self.assertEqual(int_to_mini_roman(1),   "i")
        self.assertEqual(int_to_mini_roman(4),   "iv")
        self.assertEqual(int_to_mini_roman(9),   "ix")
        self.assertEqual(int_to_mini_roman(40),  "xl")
        self.assertEqual(int_to_mini_roman(90),  "xc")
        self.assertEqual(int_to_mini_roman(400), "cd")
        self.assertEqual(int_to_mini_roman(900), "cm")
        self.assertEqual(int_to_mini_roman(1000), "m")

    def test_random_composites(self):
        """A few arbitrary composite numbers."""
        self.assertEqual(int_to_mini_roman(73),  "lxxiii")
        self.assertEqual(int_to_mini_roman(289), "cc.lxxx.ix".replace(".", ""))  # cc lxxx ix without dots
        self.assertEqual(int_to_mini_roman(999), "cmxcix")

    def test_repeated_symbol_limits(self):
        """Ensure function never repeats 'i','x','c','m' more than three times."""
        for n in range(1, 1001):
            numeral = int_to_mini_roman(n)
            for sym in ("i", "x", "c", "m"):
                self.assertNotIn(sym * 4, numeral)

    # New Unit tests # 
    def test_subtractive_notation(self):
        subtractive_cases = {
            4: "iv",
            9: "ix",
            40: "xl",
            90: "xc",
            400: "cd",
            900: "cm"
        }
        for num, expected in subtractive_cases.items():
            self.assertEqual(int_to_mini_roman(num), expected)
import signal
class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException("Test took too long!")

class TestPrimeFib(unittest.TestCase):

    def test_first_five(self):
        """Validate the first five prime-Fibonacci numbers from the docstring."""
        expected = [2, 3, 5, 13, 89]
        for i, value in enumerate(expected, start=1):
            self.assertEqual(prime_fib(i), value)

    def test_next_five(self):
        """Check the next five known prime-Fibonacci numbers."""
        expected = [233, 1597, 28657, 514229, 433494437]
        for i, value in enumerate(expected, start=6):
            self.assertEqual(prime_fib(i), value)

    def test_large_index(self):
        """Spot-check the 12-th prime Fibonacci (known value)."""
        # 12th prime Fibonacci is 2971215073
        self.assertEqual(prime_fib(12), 2971215073)

    def test_monotonic_growth(self):
        """Ensure each successive value is strictly larger than the previous one."""
        prev = prime_fib(1)
        for k in range(2, 10):
            current = prime_fib(k)
            self.assertGreater(current, prev)
            prev = current

    # Newly added tests #
    def test_prime_fib_zero_or_negative(self):
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(2) 
        try:
            self.assertEqual(prime_fib(0), False)
            self.assertEqual(prime_fib(-1), False)
        except TimeoutException:
            self.fail("prime_fib() entered an infinite loop on invalid input!")
        finally:
            signal.alarm(0)  

class TestNumericalLetterGrade(unittest.TestCase):

    def test_exact_boundaries(self):
        """Check values that sit exactly on each boundary."""
        gpas = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]
        expected = [
            "A+",   # 4.0
            "A-",   # 3.7  (exactly 3.7 falls into the next lower band)
            "B+",   # 3.3
            "B",    # 3.0
            "B-",   # 2.7
            "C+",   # 2.3
            "C",    # 2.0
            "C-",   # 1.7
            "D+",   # 1.3
            "D",    # 1.0
            "D-",   # 0.7
            "E"     # 0.0
        ]
        self.assertEqual(numerical_letter_grade(gpas), expected)

    def test_in_between_values(self):
        """Typical values strictly between boundaries."""
        gpas = [3.85, 3.5, 2.85, 2.5, 1.85, 0.5]
        expected = ["A", "A-", "B", "B-", "C", "D-"]
        self.assertEqual(numerical_letter_grade(gpas), expected)

    def test_negative_and_overflow(self):
        """GPAs below 0 or above 4 should still map (assume clamp)."""
        gpas = [-0.1, 4.2]
        # spec doesn't cover these, but code treats <0 as E and >4.0 as A+
        expected = ["E", "A+"]
        self.assertEqual(numerical_letter_grade(gpas), expected)

    def test_mixed_list_order_preserved(self):
        """Ensure output order matches input order."""
        gpas = [0.8, 2.95, 3.95, 3.05]
        expected = ["D", "B", "A", "B+"]
        self.assertEqual(numerical_letter_grade(gpas), expected)
    ###self added tests###
    def test_6(self):
        gpas = [3.3]
        expected = ["B+"]
        self.assertEqual(numerical_letter_grade(gpas), expected)
    def test_7(self):
        gpas = [1.3,1.7,1.0]
        expected = ["D+","C-","D"]
        self.assertEqual(numerical_letter_grade(gpas), expected)

class TestClosestInteger(unittest.TestCase):

    # ─── 1. Exact integers ──────────────────────────────────────────────
    def test_exact_integers(self):
        self.assertEqual(closest_integer("0"), 0)
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("-7"), -7)

    # ─── 2. Normal rounding (not a .5 fraction) ─────────────────────────
    def test_standard_rounding(self):
        self.assertEqual(closest_integer("15.3"), 15)   # below midpoint
        self.assertEqual(closest_integer("2.9"), 3)     # above midpoint
        self.assertEqual(closest_integer("-2.9"), -3)   # negative above midpoint
        self.assertEqual(closest_integer("-5.2"), -5)   # negative below midpoint

    # ─── 3. .5 cases must round away from zero ──────────────────────────
    def test_halfway_cases(self):
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("-14.5"), -15)
        self.assertEqual(closest_integer("0.5"), 1)
        self.assertEqual(closest_integer("-0.5"), -1)

    # ─── 4. Large values sanity check ───────────────────────────────────
    def test_large_values(self):
        self.assertEqual(closest_integer("123456.5"), 123457)   # away from zero
        self.assertEqual(closest_integer("-98765.49"), -98765)
    ###self added tests###
    def test_6(self):
        self.assertEqual(closest_integer("-0.1"), 0)  
        self.assertEqual(closest_integer("14.49"), 14)
