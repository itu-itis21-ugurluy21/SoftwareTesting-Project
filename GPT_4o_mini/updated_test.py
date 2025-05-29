""""@Authors
Student Names: Muhammed Yunus Doğru
Student IDs: 150210092
"""
from updated_code import *
import unittest



class TestOddCount(unittest.TestCase):

    def test_basic_case(self):
        input_data = ["12345"]
        expected = ["the number of odd elements in the string 3 of the input."]
        self.assertEqual(odd_count(input_data), expected)

    def test_multiple_strings(self):
        input_data = ["135", "246", "7890"]
        expected = [
            "the number of odd elements in the string 3 of the input.",
            "the number of odd elements in the string 0 of the input.",
            "the number of odd elements in the string 2 of the input."
        ]
        self.assertEqual(odd_count(input_data), expected)

    def test_empty_string(self):
        input_data = [""]
        expected = ["the number of odd elements in the string 0 of the input."]
        self.assertEqual(odd_count(input_data), expected)

    def test_large_numbers(self):
        input_data = ["975318642975318642"]
        expected = ["the number of odd elements in the string 9 of the input."]
        self.assertEqual(odd_count(input_data), expected)

    def test_no_digits(self):
        input_data = ["abcdefg"]
        expected = ["the number of odd elements in the string 0 of the input."]
        self.assertEqual(odd_count(input_data), expected)

    #New Unit Test

    def test_mixed_characters(self):
        input_data = ["a1b3c5d7"]
        expected = ["the number of odd elements in the string 4 of the input."]
        self.assertEqual(odd_count(input_data), expected)

    def test_double_digit_count(self):
        input_data = ["1111111111"]
        expected = ["the number of odd elements in the string 10 of the input."]
        self.assertEqual(odd_count(input_data), expected)

class TestMaximum(unittest.TestCase):

    def test_basic_case(self):
        arr = [1, 3, 2, 5, 4]
        k = 3
        expected = [3, 4, 5]
        self.assertEqual(maximum(arr, k), expected)

    def test_k_equals_length(self):
        arr = [10, 20, 30]
        k = 3
        expected = [10, 20, 30]
        self.assertEqual(maximum(arr, k), expected)

    def test_with_duplicates(self):
        arr = [4, 5, 5, 2, 1]
        k = 2
        expected = [5, 5]
        self.assertEqual(maximum(arr, k), expected)

    def test_all_elements_same(self):
        arr = [7, 7, 7, 7]
        k = 2
        expected = [7, 7]
        self.assertEqual(maximum(arr, k), expected)

    def test_negative_numbers(self):
        arr = [-10, -20, -30, -5]
        k = 2
        expected = [-10, -5]
        self.assertEqual(maximum(arr, k), expected)

    # New Unit Test 

    def test_k_zero(self):
        """k = 0 ise sonuç boş liste olmalı."""
        arr = [1, 2, 3]
        k = 0
        expected = []
        self.assertEqual(maximum(arr, k), expected)

    def test_k_exceeds_length(self):
        """k, dizi uzunluğundan büyükse tüm elemanlar artan sırada dönmeli."""
        arr = [8, 3, 6]
        k = 10            # len(arr) = 3
        expected = [3, 6, 8]
        self.assertEqual(maximum(arr, k), expected)

class TestAllPrefixes(unittest.TestCase):

    def test_basic_case(self):
        string = "abc"
        expected = ["a", "ab", "abc"]
        self.assertEqual(all_prefixes(string), expected)

    def test_single_character(self):
        string = "x"
        expected = ["x"]
        self.assertEqual(all_prefixes(string), expected)

    def test_empty_string(self):
        string = ""
        expected = []
        self.assertEqual(all_prefixes(string), expected)

    def test_with_special_characters(self):
        string = "!@#"
        expected = ["!", "!@", "!@#"]
        self.assertEqual(all_prefixes(string), expected)

    def test_longer_string(self):
        string = "prefix"
        expected = ["p", "pr", "pre", "pref", "prefi", "prefix"]
        self.assertEqual(all_prefixes(string), expected)

    # New Unit Tests

    def test_leading_space(self):
        string = " lead"
        expected = [" ", " l", " le", " lea", " lead"]
        self.assertEqual(all_prefixes(string), expected)

    def test_unicode_characters(self):
        string = "αβγ"
        expected = ["α", "αβ", "αβγ"]
        self.assertEqual(all_prefixes(string), expected)



class TestDoAlgebra(unittest.TestCase):

    def test_basic_operations(self):
        operators = ["+", "*", "-"]
        operands = [2, 3, 4, 5]
        expected = 9  # 2 + 3 * 4 - 5 = 9
        self.assertEqual(do_algebra(operators, operands), expected)

    def test_single_operand(self):
        operators = []
        operands = [42]
        expected = 42
        self.assertEqual(do_algebra(operators, operands), expected)

    def test_division(self):
        operators = ["/", "+"]
        operands = [20, 4, 2]
        expected = 20 / 4 + 2  # 5 + 2 = 7
        self.assertEqual(do_algebra(operators, operands), expected)

    def test_parentheses_effect(self):
        operators = ["+", "*"]
        operands = [1, 2, 3]
        expected = 1 + 2 * 3  # 1 + 6 = 7, not (1+2)*3 = 9
        self.assertEqual(do_algebra(operators, operands), expected)

    def test_negative_numbers(self):
        operators = ["-", "*"]
        operands = [10, 3, -2]
        expected = 10 - 3 * -2  # 10 - (-6) = 16
        self.assertEqual(do_algebra(operators, operands), expected)
    
    # New Unit Tests

    def test_zero_division(self):
        operators = ["/"]
        operands  = [10, 0]
        with self.assertRaises(ZeroDivisionError):
            do_algebra(operators, operands)

    def test_operator_operand_mismatch(self):
        operators = ["+", "*"]
        operands  = [2, 3, 4, 5]      # son '5' işleme girmez
        expected  = 2 + 3 * 4         # 14
        self.assertEqual(do_algebra(operators, operands), expected)



class TestLargestDivisor(unittest.TestCase):

    def test_even_number(self):
        self.assertEqual(largest_divisor(10), 5)

    def test_odd_number(self):
        self.assertEqual(largest_divisor(15), 5)

    def test_prime_number(self):
        self.assertEqual(largest_divisor(13), 1)  # 13 is prime

    def test_power_of_two(self):
        self.assertEqual(largest_divisor(16), 8)

    def test_smallest_valid_input(self):
        self.assertEqual(largest_divisor(2), 1)  # Only possible divisor less than 2

    # New Unit Tests

    def test_square_of_prime(self):
        self.assertEqual(largest_divisor(49), 7)

    def test_input_one_returns_none(self):
        self.assertIsNone(largest_divisor(1))



class TestChangeBase(unittest.TestCase):

    def test_base_binary(self):
        self.assertEqual(change_base(10, 2), '1010')  # 10 in base 2 is 1010

    def test_base_decimal(self):
        self.assertEqual(change_base(255, 10), '255')  # No change expected

    def test_base_3(self):
        self.assertEqual(change_base(5, 3), '12')  # 5 in base 3 is 12

    def test_zero_input(self):
        self.assertEqual(change_base(0, 2), '0')  # Special case

    def test_large_number(self):
        self.assertEqual(change_base(1024, 2), '10000000000')  # 2^10
    
    # New Unit Tests

    def test_base_octal(self):
        self.assertEqual(change_base(64, 8), '100')   # 64₁₀ = 100₈

    def test_base_hexadecimal(self):
        self.assertEqual(change_base(255, 16), 'ff')  # Beklenen 255₁₀ = ff₁₆



class TestMedian(unittest.TestCase):

    def test_odd_number_of_elements(self):
        l = [3, 1, 4]
        expected = 3
        self.assertEqual(median(l), expected)

    def test_even_number_of_elements(self):
        l = [1, 2, 3, 4]
        expected = 2.5
        self.assertEqual(median(l), expected)

    def test_sorted_input(self):
        l = [10, 20, 30, 40, 50]
        expected = 30
        self.assertEqual(median(l), expected)

    def test_unsorted_with_negatives(self):
        l = [-1, -5, -3]
        expected = -3
        self.assertEqual(median(l), expected)

    def test_floating_point_result(self):
        l = [1, 99]
        expected = 50.0
        self.assertEqual(median(l), expected)

    # New Unit Tests

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            median([])

    def test_all_elements_equal(self):
        l = [7, 7, 7, 7]
        expected = 7
        self.assertEqual(median(l), expected)



class TestCircularShift(unittest.TestCase):

    def test_basic_shift(self):
        self.assertEqual(circular_shift(12345, 2), '45123')

    def test_shift_zero(self):
        self.assertEqual(circular_shift(9876, 0), '9876')

    def test_shift_equal_length(self):
        self.assertEqual(circular_shift(1234, 4), '1234')  # full cycle returns original

    def test_shift_greater_than_length(self):
        self.assertEqual(circular_shift(321, 5), '123')  # reverse of '321' is '123'

    def test_single_digit(self):
        self.assertEqual(circular_shift(7, 3), '7')  # no matter the shift, result is same

    # New Unit Tests

    def test_shift_length_minus_one(self):
        self.assertEqual(circular_shift(12345, 4), '23451')

    def test_negative_shift(self):
        with self.assertRaises(ValueError):
            circular_shift(12345, -1)


class TestPluck(unittest.TestCase):

    def test_basic_case(self):
        arr = [5, 8, 2, 3, 4]
        expected = [2, 2]  # 2 is smallest even, index 2
        self.assertEqual(pluck(arr), expected)

    def test_no_even_numbers(self):
        arr = [1, 3, 5, 7]
        expected = []
        self.assertEqual(pluck(arr), expected)

    def test_first_element_even(self):
        arr = [2, 9, 4, 6]
        expected = [2, 0]
        self.assertEqual(pluck(arr), expected)

    def test_multiple_same_min_evens(self):
        arr = [8, 2, 2, 10]
        expected = [2, 1]  # first occurrence of min even
        self.assertEqual(pluck(arr), expected)

    def test_negative_numbers(self):
        arr = [-4, -2, -6, 3]
        expected = [-6, 2]  # smallest even among negatives
        self.assertEqual(pluck(arr), expected)

    # New Unit Test

    def test_contains_zero(self):
        arr = [7, 0, 4, 2]
        expected = [0, 1]          # 0 en küçük çift, indeks 1
        self.assertEqual(pluck(arr), expected)

    def test_empty_array(self):
        self.assertEqual(pluck([]), [])




class TestEncode(unittest.TestCase):

    def test_basic_vowels_and_consonants(self):
        self.assertEqual(encode("Hello"), "hGLLQ")  # e→g (swap G), o→q (swap Q), others swap

    def test_all_vowels(self):
        self.assertEqual(encode("aeiouAEIOU"), "CGKQWCgkqw")  # all vowels shifted+swapcase

    def test_all_consonants(self):
        self.assertEqual(encode("bcdfg"), "BCDFG")  # just swapcase

    def test_mixed_case_and_nonalpha(self):
        self.assertEqual(encode("PyTh0n!"), "pYtH0N!")  # only letters are affected

    def test_empty_string(self):
        self.assertEqual(encode(""), "")  # edge case
    
    # New Unit Tests

    def test_sentence_with_spaces(self):
        src = "This is, in fact, a Test."
        expected = "tHKS KS, KN FCKT, C tGST."
        self.assertEqual(encode(src), expected)

    def test_vowel_u_wrapping(self):
        src = "Uu"
        expected = "wW"
        self.assertEqual(encode(src), expected)


class TestValidDate(unittest.TestCase):

    def test_valid_31_day_month(self):
        self.assertTrue(valid_date("01-31-2023"))  # Ocak, 31 gün

    def test_valid_30_day_month(self):
        self.assertTrue(valid_date("04-30-2023"))  # Nisan, 30 gün

    def test_invalid_day_in_month(self):
        self.assertFalse(valid_date("04-31-2023"))  # Nisan'da 31 gün yok

    def test_february_limit(self):
        self.assertTrue(valid_date("02-29-2023"))  # Şubat, leap year kontrolü yapılmadığından 29 geçerli

    def test_february_invalid_day(self):
        self.assertFalse(valid_date("02-30-2023"))  # Şubat'ta 30 gün olmaz

    def test_invalid_month(self):
        self.assertFalse(valid_date("13-01-2023"))  # 13. ay yok

    def test_non_digit_input(self):
        self.assertFalse(valid_date("ab-cd-efgh"))  # tüm parçalar harf

    def test_malformed_date(self):
        self.assertFalse(valid_date("01/01/2023"))  # yanlış ayraç

    def test_empty_string(self):
        self.assertFalse(valid_date(""))  # boş giriş

    def test_incorrect_length(self):
        self.assertFalse(valid_date("1-1-2023"))  # uzunluk != 10

    # New Unit Tests

    def test_zero_day(self):
        self.assertFalse(valid_date("05-00-2023"))  # Mayıs 0. gün geçersiz

    def test_zero_month(self):
        self.assertFalse(valid_date("00-15-2023"))  # 0. ay yok


class TestIsPrime(unittest.TestCase):

    def test_negative_numbers(self):
        self.assertFalse(is_prime(-7))  # negatifler asal olamaz

    def test_small_primes(self):
        self.assertTrue(is_prime(2))  # en küçük asal
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))

    def test_small_non_primes(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))

    def test_large_prime(self):
        self.assertTrue(is_prime(101))  # büyük asal sayı

    def test_large_composite(self):
        self.assertFalse(is_prime(100))  # 100 = 10 * 10

    def test_even_number_greater_than_2(self):
        self.assertFalse(is_prime(28))  # çift sayı, asal değil

    def test_prime_square_root_check(self):
        self.assertFalse(is_prime(49))  # 7*7 → tam kare asal çarpan

    # New Unit Tests

    def test_carmichael_number(self):
        self.assertFalse(is_prime(561))

    def test_medium_large_prime(self):
        self.assertTrue(is_prime(7919))



class TestMinPath(unittest.TestCase):

    def test_single_cell_grid(self):
        grid = [[7]]
        self.assertEqual(minPath(grid, 1), [7])  # tek hücre, tek adım

    def test_two_by_two_grid(self):
        grid = [
            [5, 2],
            [9, 1]
        ]
        result = minPath(grid, 2)
        self.assertIn(result, [[1, 2], [1, 5], [1, 9], [2, 1], [2, 5], [2, 9], [5, 1], [5, 2], [5, 9], [9, 1], [9, 2], [9, 5]])
        # En küçük leksikografik yol 1->2 veya 1->5 gibi olabilir

    def test_minimum_path_is_sorted(self):
        grid = [
            [7, 6],
            [5, 4]
        ]
        result = minPath(grid, 3)
        self.assertEqual(result, [4, 5, 6])  # en küçük yol sözlüksel sırayla [4,5,6]

    def test_three_by_three_with_duplicates(self):
        grid = [
            [1, 2, 3],
            [4, 1, 6],
            [7, 8, 1]
        ]
        result = minPath(grid, 2)
        self.assertEqual(result, [1, 1])  # en küçük değer tekrarlanan 1'lerden oluşur

    def test_large_k(self):
        grid = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
        result = minPath(grid, 4)
        self.assertEqual(result, [1, 2, 3, 4])  # 1’den başlayan en küçük yol büyüyerek gider

    # New Unit Tests

    def test_k_zero_returns_empty(self):
        grid = [[1, 2],
                [3, 4]]
        self.assertEqual(minPath(grid, 0), [])

    def test_k_equals_cell_count(self):
        grid = [[4, 9],
                [1, 6]]
        # Grid’de 4 hücre var → k = 4
        self.assertEqual(minPath(grid, 4), [1, 4, 6, 9])




class TestIsNested(unittest.TestCase):

    def test_no_brackets(self):
        self.assertFalse(is_nested("abc def"))  # parantez yok

    def test_single_pair(self):
        self.assertFalse(is_nested("[abc]"))  # tek parantez çifti, iç içe değil

    def test_nested_brackets(self):
        self.assertTrue(is_nested("[[abc]]"))  # iç içe parantez

    def test_multiple_non_nested(self):
        self.assertFalse(is_nested("[a][b][c]"))  # çoklu ama iç içe değil

    def test_deeply_nested(self):
        self.assertTrue(is_nested("[a[b[c[d]]]]"))  # çok katmanlı iç içe

    def test_unbalanced_brackets(self):
        self.assertFalse(is_nested("[abc][def]]"))  # hatalı ama nested değil

    def test_open_brackets_only(self):
        self.assertFalse(is_nested("[[[[["))  # açılmış ama kapanmamış — nested gibi görünse de `depth > 1` olduğu için True olabilir
        self.assertTrue(is_nested("[[["))    # burada kesin nested

    def test_closing_before_opening(self):
        self.assertFalse(is_nested("]a[b]"))  # açılmadan kapanma, yine nested değil

    # New Unit Tests

    def test_nested_after_separate_block(self):
        self.assertTrue(is_nested("[x][[y]]"))

    def test_extra_closing_bracket_without_nesting(self):
        self.assertFalse(is_nested("[]][]["))


class TestFixSpaces(unittest.TestCase):

    def test_single_spaces(self):
        self.assertEqual(fix_spaces("a b c"), "a_b_c")  # tek boşluklar

    def test_double_spaces(self):
        self.assertEqual(fix_spaces("a  b"), "a_b")  # iki boşluk da _ olur

    def test_triple_spaces(self):
        self.assertEqual(fix_spaces("a   b"), "a-b")  # üç boşluk → tire

    def test_mixed_spaces(self):
        self.assertEqual(fix_spaces("a    b  c d"), "a-b_c_d")  # karma durum

    def test_no_spaces(self):
        self.assertEqual(fix_spaces("abc"), "abc")  # boşluk yoksa değişiklik yok

    def test_only_spaces(self):
        self.assertEqual(fix_spaces("     "), "-_")  # 5 boşluk: 3→‘-’, 2→‘_’

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(fix_spaces("  a   b "), "_a-b_")  # baştaki/sondaki boşluklar da işlenmeli

    # New Unit Tests

    def test_long_space_run(self):
        self.assertEqual(fix_spaces("foo          bar"), "foo-bar")

    def test_leading_triple_spaces(self):
        self.assertEqual(fix_spaces("   hello"), "-hello")


class TestFileNameCheck(unittest.TestCase):

    def test_valid_cases(self):
        self.assertEqual(file_name_check("file1.txt"), "Yes")
        self.assertEqual(file_name_check("a23.exe"), "Yes")
        self.assertEqual(file_name_check("start99.dll"), "Yes")

    def test_too_many_digits(self):
        self.assertEqual(file_name_check("abc1234.txt"), "No")  # 4 rakam

    def test_multiple_dots(self):
        self.assertEqual(file_name_check("my.file.txt"), "No")  # 2 nokta

    def test_no_dot(self):
        self.assertEqual(file_name_check("filetxt"), "No")  # nokta yok

    def test_invalid_extension(self):
        self.assertEqual(file_name_check("app.pdf"), "No")  # pdf geçerli değil

    def test_empty_name(self):
        self.assertEqual(file_name_check(".exe"), "No")  # ad yok

    def test_nonalpha_start(self):
        self.assertEqual(file_name_check("1file.txt"), "No")  # sayı ile başlıyor

    def test_edge_case_exactly_three_digits(self):
        self.assertEqual(file_name_check("x12a3.dll"), "Yes")  # tam 3 rakam

    def test_extension_case_sensitivity(self):
        self.assertEqual(file_name_check("file.TXT"), "No")  # büyük harfli uzantı geçersiz

    def test_starting_with_underscore(self):
        self.assertEqual(file_name_check("_file1.txt"), "No")  # harfle başlamıyor

    # New Unit Tests

    def test_trailing_dot_without_extension(self):
        self.assertEqual(file_name_check("file."), "No")

    def test_valid_name_with_symbols(self):
        self.assertEqual(file_name_check("my-file_2.txt"), "Yes")



class TestIntToMiniRoman(unittest.TestCase):

    def test_basic_values(self):
        self.assertEqual(int_to_mini_roman(1), "i")
        self.assertEqual(int_to_mini_roman(4), "iv")
        self.assertEqual(int_to_mini_roman(9), "ix")
        self.assertEqual(int_to_mini_roman(40), "xl")
        self.assertEqual(int_to_mini_roman(90), "xc")

    def test_typical_numbers(self):
        self.assertEqual(int_to_mini_roman(58), "lviii")      # l = 50, v = 5, iii = 3
        self.assertEqual(int_to_mini_roman(1994), "mcmxciv")  # 1000 + (100 less 1000) + (10 less 100) + (1 less 5)

    def test_max_value(self):
        self.assertEqual(int_to_mini_roman(3999), "mmmcmxcix")  # en büyük geçerli değer

    def test_middle_value(self):
        self.assertEqual(int_to_mini_roman(1000), "m")
        self.assertEqual(int_to_mini_roman(1444), "mcdxliv")

    def test_min_value(self):
        self.assertEqual(int_to_mini_roman(1), "i")  # minimum geçerli giriş

    # New Unit Tests

    def test_zero_value(self):
        self.assertEqual(int_to_mini_roman(0), "")

    def test_many_repetitions(self):
        self.assertEqual(int_to_mini_roman(3888), "mmmdccclxxxviii")

class TestPrimeFib(unittest.TestCase):

    def test_first_few(self):
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 5)
        self.assertEqual(prime_fib(4), 13)
        self.assertEqual(prime_fib(5), 89)

    def test_mid_range(self):
        self.assertEqual(prime_fib(6), 233)
        self.assertEqual(prime_fib(7), 1597)

    def test_higher_index(self):
        self.assertEqual(prime_fib(8), 28657)
        self.assertEqual(prime_fib(9), 514229)

    def test_edge_case(self):
        # Sanity check: n = 10 (should be known value)
        self.assertEqual(prime_fib(10), 433494437)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            prime_fib("3")  # string yerine int bekleniyor

    # New Unit Tests

    def test_returned_value_is_prime(self):
        for i in range(1, 10):          # ilk 9 asal Fibonacci sayısı
            self.assertTrue(is_prime(prime_fib(i)))

    def test_eleventh_prime_fibonacci(self):
        self.assertEqual(prime_fib(11), 2971215073)


class TestNumericalLetterGrade(unittest.TestCase):

    def test_perfect_gpa(self):
        self.assertEqual(numerical_letter_grade([4.0]), ['A+'])

    def test_boundary_grades(self):
        self.assertEqual(numerical_letter_grade([3.8, 3.4, 3.1]), ['A', 'A-', 'B+'])
        self.assertEqual(numerical_letter_grade([2.8, 2.4, 2.1]), ['B', 'B-', 'C+'])
        self.assertEqual(numerical_letter_grade([1.8, 1.4, 1.1]), ['C', 'C-', 'D+'])

    def test_low_grades(self):
        self.assertEqual(numerical_letter_grade([0.8, 0.1, 0.0]), ['D', 'D-', 'E'])

    def test_mixed_input(self):
        grades = [4.0, 3.75, 3.5, 3.2, 2.95, 2.5, 1.9, 1.0, 0.6, 0.0]
        expected = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C', 'D+', 'D-', 'E']
        self.assertEqual(numerical_letter_grade(grades), expected)

    def test_empty_list(self):
        self.assertEqual(numerical_letter_grade([]), [])
        
    # New Unit Tests

    def test_boundary_values(self):
        gpas = [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]
        expected = ['A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
        self.assertEqual(numerical_letter_grade(gpas), expected)

    def test_out_of_range_values(self):
        self.assertEqual(numerical_letter_grade([-0.5, 4.5]), ['E', 'A'])

class TestClosestInteger(unittest.TestCase):

    def test_positive_half(self):
        self.assertEqual(closest_integer(2.5), 3)
        self.assertEqual(closest_integer(0.5), 1)
        self.assertEqual(closest_integer(3.4999), 3)

    def test_negative_half(self):
        self.assertEqual(closest_integer(-2.5), -3)
        self.assertEqual(closest_integer(-0.5), -1)
        self.assertEqual(closest_integer(-3.4999), -3)

    def test_exact_integers(self):
        self.assertEqual(closest_integer(0.0), 0)
        self.assertEqual(closest_integer(-2.0), -2)
        self.assertEqual(closest_integer(7.0), 7)

    def test_near_boundaries(self):
        self.assertEqual(closest_integer(1.49), 1)
        self.assertEqual(closest_integer(1.51), 2)
        self.assertEqual(closest_integer(-1.49), -1)
        self.assertEqual(closest_integer(-1.51), -2)

    def test_string_input(self):
        self.assertEqual(closest_integer("2.5"), 3)
        self.assertEqual(closest_integer("-3.5"), -4)

    # New Unit Tests

    def test_sub_half_magnitudes(self):
        self.assertEqual(closest_integer(0.4999), 0)
        self.assertEqual(closest_integer(-0.4999), 0)

    def test_invalid_non_numeric_string(self):
        with self.assertRaises(ValueError):
            closest_integer("not-a-number")

class TestByLength(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(by_length([1, 2, 3]), ['Three', 'Two', 'One'])

    def test_unsorted_with_invalids(self):
        self.assertEqual(by_length([5, 3, 11, -1, 7, 0]), ['Seven', 'Five', 'Three'])

    def test_all_valid_sorted(self):
        self.assertEqual(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]), [
            'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One'
        ])

    def test_all_invalid(self):
        self.assertEqual(by_length([0, 10, -3, 15]), [])

    def test_duplicates(self):
        self.assertEqual(by_length([2, 2, 9, 1, 9]), ['Nine', 'Nine', 'Two', 'Two', 'One'])

    def test_empty_input(self):
        self.assertEqual(by_length([]), [])

    # New Unit Tests

    def test_already_descending(self):
        self.assertEqual(by_length([9, 8, 7]), ['Nine', 'Eight', 'Seven'])

    def test_min_max_duplicates(self):
        self.assertEqual(by_length([1, 9, 1, 9, 1]), ['Nine', 'Nine', 'One', 'One', 'One'])


class TestGetClosestVowel(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(get_closest_vowel("apple"), "e")  # 'e' has consonants on both sides

    def test_multiple_vowels(self):
        self.assertEqual(get_closest_vowel("strength"), "e")  # 'e' between r and n

    def test_no_vowel(self):
        self.assertEqual(get_closest_vowel("try"), "")  # no vowel in the middle

    def test_vowels_at_ends_only(self):
        self.assertEqual(get_closest_vowel("arena"), "")  # middle vowels are adjacent to vowels

    def test_uppercase_mixed(self):
        self.assertEqual(get_closest_vowel("HElLo"), "E")  # uppercase vowel with consonants around

    def test_short_words(self):
        self.assertEqual(get_closest_vowel("hi"), "")  # too short to have a middle vowel

    def test_vowel_with_adjacent_vowels(self):
        self.assertEqual(get_closest_vowel("quiet"), "")  # 'u' and 'i' are adjacent

    # New Unit Tests

    def test_multiple_candidates_returns_rightmost(self):

        self.assertEqual(get_closest_vowel("catapults"), "u")

    def test_word_without_standard_vowels(self):
        self.assertEqual(get_closest_vowel("rhythm"), "")


    

class TestAddElements(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(add_elements([10, 20, 30, 40], 3), 60)  # 10+20+30

    def test_with_invalid_elements(self):
        self.assertEqual(add_elements([100, 20, -150, 50], 4), 70)  # Only 20 and 50 are valid

    def test_k_exceeds_length(self):
        self.assertEqual(add_elements([10, 20], 5), 30)  # still valid, no IndexError

    def test_all_invalid(self):
        self.assertEqual(add_elements([150, 200, -150], 3), 0)

    def test_negative_and_positive_mix(self):
        self.assertEqual(add_elements([-99, 0, 99, -100], 4), 0)  # sum of first 3 only = 0

    def test_empty_list(self):
        self.assertEqual(add_elements([], 3), 0)

    # New Unit Tests

    def test_k_zero(self):
        self.assertEqual(add_elements([1, 2, 3], 0), 0)

    def test_negative_k_slice(self):
        self.assertEqual(add_elements([10, 20, 30, 40], -2), 30)  # 10+20

class TestSumSquares(unittest.TestCase):

    def test_basic_positive(self):
        self.assertEqual(sum_squares([1.1, 2.5]), 13)  # 2² + 3² = 4 + 9

    def test_all_integers(self):
        self.assertEqual(sum_squares([1.0, 2.0, 3.0]), 14)  # 1² + 2² + 3² = 14

    def test_mixed_values(self):
        self.assertEqual(sum_squares([0.1, 1.9, 2.0, 3.7]), 1 + 4 + 4 + 16)  # = 25

    def test_negatives(self):
        self.assertEqual(sum_squares([-1.1, -2.5]), 1 + 4)  # ceil(-1.1) = -1 → 1, ceil(-2.5) = -2 → 4

    def test_large_numbers(self):
        self.assertEqual(sum_squares([99.9, 100.1]), 100**2 + 101**2)  # 10000 + 10201 = 20201

    def test_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

    # New Unit Tests

    def test_small_fractional_and_near_zero(self):
        self.assertEqual(sum_squares([0.3, -0.3]), 1)

    def test_infinite_value_raises(self):
        with self.assertRaises(OverflowError):
            sum_squares([float('inf')])

class TestSpecialFilter(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(specialFilter([15, 31, 53, 22, 8]), 3)

    def test_all_below_10(self):
        self.assertEqual(specialFilter([1, 3, 9, 7]), 0)

    def test_no_matching_digits(self):
        self.assertEqual(specialFilter([20, 42, 68]), 0)  # all first/last digits are even

    def test_edge_digits(self):
        self.assertEqual(specialFilter([19, 91, 11, 33, 77]), 5)  # all digits valid

    def test_mixed_case(self):
        self.assertEqual(specialFilter([5, 13, 20, 37, 49, 99]), 3)  # 13, 37, 99

    def test_empty_list(self):
        self.assertEqual(specialFilter([]), 0)

    # New Unit Tests

    def test_boundary_at_ten(self):
        self.assertEqual(specialFilter([10, 11]), 1)

    def test_large_multi_digit_numbers(self):
        self.assertEqual(specialFilter([101, 30305, 13579, 24681]), 3)


class TestCommon(unittest.TestCase):

    def test_integers_with_common(self):
        self.assertEqual(common([1, 2, 3], [2, 3, 4]), [2, 3])

    def test_strings_with_common(self):
        self.assertEqual(common(['apple', 'banana'], ['banana', 'cherry']), ['banana'])

    def test_no_common_elements(self):
        self.assertEqual(common([1, 2, 3], [4, 5, 6]), [])

    def test_duplicates_in_lists(self):
        self.assertEqual(common([1, 2, 2, 3], [2, 2, 3, 3]), [2, 3])  # set removes duplicates

    def test_empty_lists(self):
        self.assertEqual(common([], []), [])

    def test_one_empty_list(self):
        self.assertEqual(common([1, 2, 3], []), [])

    def test_unsorted_input(self):
        self.assertEqual(common([5, 1, 3], [3, 5]), [3, 5])  # output is sorted

    # New Unit Tests

    def test_int_and_float_equality(self):
        self.assertEqual(common([2, 2.0, 3.0], [2.0, 2]), [2])

    def test_unhashable_elements_raise(self):
        with self.assertRaises(TypeError):
            common([[1, 2], [3]], [[1, 2]])

class TestTriangleArea(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.0)

    def test_equilateral_triangle(self):
        self.assertAlmostEqual(triangle_area(5, 5, 5), 10.83)

    def test_invalid_triangle(self):
        self.assertEqual(triangle_area(1, 2, 3), -1)  # 1 + 2 == 3 → geçersiz

    def test_decimal_sides(self):
        self.assertAlmostEqual(triangle_area(3.5, 4.2, 5.1), 7.29)

    def test_large_triangle(self):
        self.assertAlmostEqual(triangle_area(3000, 4000, 5000), 6000000.0)

    def test_zero_or_negative_sides(self):
        self.assertEqual(triangle_area(0, 5, 7), -1)
        self.assertEqual(triangle_area(-3, 4, 5), -1)

    # New Unit Tests

    def test_isosceles_triangle(self):
        self.assertAlmostEqual(triangle_area(10, 10, 12), 48.0)

    def test_very_small_triangle(self):
        self.assertAlmostEqual(triangle_area(0.3, 0.4, 0.5), 0.06)

class TestIsMultiplyPrime(unittest.TestCase):

    def test_three_distinct_primes(self):
        self.assertTrue(is_multiply_prime(30))  # 2 * 3 * 5

    def test_repeating_prime_factors(self):
        self.assertTrue(is_multiply_prime(8))   # 2 * 2 * 2

    def test_not_enough_prime_factors(self):
        self.assertFalse(is_multiply_prime(7))  # Tek asal

    def test_non_prime_factors(self):
        self.assertFalse(is_multiply_prime(60))  # 2*2*3*5 → 4 asal → False

    def test_large_composite(self):
        self.assertFalse(is_multiply_prime(1001))  # 7*11*13 → 3 asal ama > 100

    def test_small_number(self):
        self.assertFalse(is_multiply_prime(1))  # Geçersiz

    def test_prime_number_input(self):
        self.assertFalse(is_multiply_prime(17))  # Tek asal

    # New Unit Tests

    def test_same_prime_cubed(self):
        self.assertTrue(is_multiply_prime(13 ** 3))      # 2197

    def test_prime_factor_above_limit(self):
        self.assertFalse(is_multiply_prime(2 * 3 * 101))  # 606

class TestEncrypt(unittest.TestCase):

    def test_simple_shift(self):
        self.assertEqual(encrypt("abcd"), "efgh")

    def test_wrap_around(self):
        self.assertEqual(encrypt("wxyz"), "abcd")

    def test_mixed_case_and_symbols(self):
        self.assertEqual(encrypt("abc XYZ!"), "efg XYZ!")

    def test_no_letters(self):
        self.assertEqual(encrypt("123!@#"), "123!@#")  # değişmemeli

    def test_empty_string(self):
        self.assertEqual(encrypt(""), "")

    def test_full_alphabet(self):
        self.assertEqual(encrypt("abcdefghijklmnopqrstuvwxyz"), "efghijklmnopqrstuvwxyzabcd")

    # New Unit Tests

    def test_repeated_pattern_and_whitespace(self):
        self.assertEqual(encrypt("zz zz"), "dd dd")

    def test_non_ascii_characters_unchanged(self):
        self.assertEqual(encrypt("çağrı"), "çağrı")   # ç, ğ, ı değişmez


class TestCheckDictCase(unittest.TestCase):

    def test_all_lowercase_keys(self):
        self.assertTrue(check_dict_case({'a': 1, 'b': 2, 'z': 3}))

    def test_all_uppercase_keys(self):
        self.assertTrue(check_dict_case({'A': 1, 'B': 2, 'Z': 3}))

    def test_mixed_case_keys(self):
        self.assertFalse(check_dict_case({'A': 1, 'b': 2}))

    def test_empty_dict(self):
        self.assertFalse(check_dict_case({}))

    def test_non_string_keys(self):
        self.assertFalse(check_dict_case({1: 'one', 2: 'two'}))

    def test_string_and_non_string_mixed_keys(self):
        self.assertFalse(check_dict_case({'a': 1, 2: 'two'}))

    # New Unit Tests

    def test_empty_string_key(self):
        self.assertFalse(check_dict_case({'': 1, 'a': 2}))

    def test_uppercase_with_digits(self):
        self.assertTrue(check_dict_case({'ABC123': 1, 'XYZ99': 2}))
