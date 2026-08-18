TASKS = [
    {
        "id": 1, "difficulty": "easy", "function_name": "is_palindrome",
        "prompt": "def is_palindrome(s: str) -> bool:\n"
                  "    Return True if s is a palindrome, ignoring case and non-alphanumeric characters.",
        "test_code": """
def test_solution():
    from solution import is_palindrome
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert is_palindrome("No 'x' in Nixon") == True
    assert is_palindrome("a") == True
""",
    },
    {
        "id": 2, "difficulty": "easy", "function_name": "flatten",
        "prompt": "def flatten(nested: list) -> list:\n"
                  "    Flatten an arbitrarily nested list into a single flat list, preserving order.",
        "test_code": """
def test_solution():
    from solution import flatten
    assert flatten([1, [2, [3, 4], 5], 6]) == [1, 2, 3, 4, 5, 6]
    assert flatten([]) == []
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten([[[[1]]]]) == [1]
    assert flatten([1, [], [2, []], 3]) == [1, 2, 3]
""",
    },
    {
        "id": 3, "difficulty": "easy", "function_name": "most_frequent",
        "prompt": "def most_frequent(items: list):\n"
                  "    Return the most frequent element. On a tie, return the smallest tied element (by <).",
        "test_code": """
def test_solution():
    from solution import most_frequent
    assert most_frequent([1, 2, 2, 3, 3]) == 2
    assert most_frequent([5]) == 5
    assert most_frequent([1, 1, 2, 2, 3]) == 1
    assert most_frequent(["b", "a", "a", "b"]) == "a"
""",
    },
    {
        "id": 4, "difficulty": "easy", "function_name": "caesar_cipher",
        "prompt": "def caesar_cipher(s: str, shift: int) -> str:\n"
                  "    Shift each letter by shift positions (wrapping a-z / A-Z), preserve case,\n"
                  "    leave non-letters unchanged. shift may be negative or > 26.",
        "test_code": """
def test_solution():
    from solution import caesar_cipher
    assert caesar_cipher("Zebra-9", 3) == "Cheud-9"
    assert caesar_cipher("abc", 0) == "abc"
    assert caesar_cipher("xyz", 3) == "abc"
    assert caesar_cipher("abc", -1) == "zab"
    assert caesar_cipher("ABC", 29) == "DEF"
""",
    },
    {
        "id": 5, "difficulty": "medium", "function_name": "merge_intervals",
        "prompt": "def merge_intervals(intervals: list) -> list:\n"
                  "    Given a list of (start, end) tuples, merge overlapping or touching intervals.\n"
                  "    Return the merged list sorted by start.",
        "test_code": """
def test_solution():
    from solution import merge_intervals
    assert merge_intervals([(1,3),(2,6),(8,10),(15,18)]) == [(1,6),(8,10),(15,18)]
    assert merge_intervals([]) == []
    assert merge_intervals([(1,4),(4,5)]) == [(1,5)]
    assert merge_intervals([(1,4)]) == [(1,4)]
    assert merge_intervals([(5,6),(1,2)]) == [(1,2),(5,6)]
""",
    },
    {
        "id": 6, "difficulty": "medium", "function_name": "is_valid_parens",
        "prompt": "def is_valid_parens(s: str) -> bool:\n"
                  "    s contains only (){}[]. Return True if brackets are properly nested and closed.",
        "test_code": """
def test_solution():
    from solution import is_valid_parens
    assert is_valid_parens("{[()()]}") == True
    assert is_valid_parens("{[(])}") == False
    assert is_valid_parens("") == True
    assert is_valid_parens("(") == False
    assert is_valid_parens("()[]{}") == True
    assert is_valid_parens("(]") == False
""",
    },
    {
        "id": 7, "difficulty": "medium", "function_name": "group_anagrams",
        "prompt": "def group_anagrams(words: list) -> list:\n"
                  "    Group words that are anagrams of each other. Return a list of groups.\n"
                  "    Order of groups and order within a group does not matter.",
        "test_code": """
def test_solution():
    from solution import group_anagrams
    result = group_anagrams(["eat","tea","tan","ate","nat","bat"])
    normalized = sorted(sorted(g) for g in result)
    expected = sorted(sorted(g) for g in [["eat","tea","ate"],["tan","nat"],["bat"]])
    assert normalized == expected
    assert group_anagrams([]) == []
    assert sorted(sorted(g) for g in group_anagrams(["a"])) == [["a"]]
""",
    },
    {
        "id": 8, "difficulty": "hard", "function_name": "longest_increasing_subsequence_length",
        "prompt": "def longest_increasing_subsequence_length(nums: list) -> int:\n"
                  "    Return the length of the longest strictly increasing subsequence (not\n"
                  "    necessarily contiguous).",
        "test_code": """
def test_solution():
    from solution import longest_increasing_subsequence_length as f
    assert f([10,9,2,5,3,7,101,18]) == 4
    assert f([]) == 0
    assert f([5]) == 1
    assert f([1,2,3,4]) == 4
    assert f([4,3,2,1]) == 1
""",
    },
    {
        "id": 9, "difficulty": "hard", "function_name": "min_edit_distance",
        "prompt": "def min_edit_distance(a: str, b: str) -> int:\n"
                  "    Levenshtein distance: minimum insert/delete/substitute operations (cost 1 each)\n"
                  "    to turn a into b.",
        "test_code": """
def test_solution():
    from solution import min_edit_distance
    assert min_edit_distance("horse", "ros") == 3
    assert min_edit_distance("", "") == 0
    assert min_edit_distance("abc", "") == 3
    assert min_edit_distance("intention", "execution") == 5
    assert min_edit_distance("same", "same") == 0
""",
    },
    {
        "id": 10, "difficulty": "hard", "function_name": "topological_sort",
        "prompt": "def topological_sort(graph: dict) -> list:\n"
                  "    graph maps node -> list of nodes it points to. Return a valid topological\n"
                  "    ordering of the DAG. Raise ValueError if a cycle exists.",
        "test_code": """
import pytest

def test_solution():
    from solution import topological_sort
    g = {"a": ["b"], "b": ["c"], "c": []}
    order = topological_sort(g)
    pos = {n: i for i, n in enumerate(order)}
    assert set(order) == {"a", "b", "c"}
    for node, deps in g.items():
        for d in deps:
            assert pos[node] < pos[d]

    with pytest.raises(ValueError):
        topological_sort({"a": ["b"], "b": ["a"]})
""",
    },
    {
        "id": 11, "difficulty": "easy", "function_name": "run_length_encode",
        "prompt": "def run_length_encode(s: str) -> str:\n"
                  "    Encode consecutive runs as count+char, e.g. 'aaabbc' -> '3a2b1c'.\n"
                  "    Empty string returns empty string.",
        "test_code": """
def test_solution():
    from solution import run_length_encode
    assert run_length_encode("aaabbc") == "3a2b1c"
    assert run_length_encode("") == ""
    assert run_length_encode("a") == "1a"
    assert run_length_encode("abc") == "1a1b1c"
""",
    },
    {
        "id": 12, "difficulty": "easy", "function_name": "run_length_decode",
        "prompt": "def run_length_decode(s: str) -> str:\n"
                  "    Reverse of run-length encoding, e.g. '3a2b1c' -> 'aaabbc'.",
        "test_code": """
def test_solution():
    from solution import run_length_decode
    assert run_length_decode("3a2b1c") == "aaabbc"
    assert run_length_decode("") == ""
    assert run_length_decode("1a1b1c") == "abc"
    assert run_length_decode("10a") == "a" * 10
""",
    },
    {
        "id": 13, "difficulty": "easy", "function_name": "matrix_transpose",
        "prompt": "def matrix_transpose(matrix: list) -> list:\n"
                  "    Return the transpose of a 2D list (rows/columns swapped).",
        "test_code": """
def test_solution():
    from solution import matrix_transpose
    assert matrix_transpose([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]]
    assert matrix_transpose([[1]]) == [[1]]
    assert matrix_transpose([[1,2],[3,4]]) == [[1,3],[2,4]]
""",
    },
    {
        "id": 14, "difficulty": "medium", "function_name": "matrix_multiply",
        "prompt": "def matrix_multiply(a: list, b: list) -> list:\n"
                  "    Multiply two 2D matrices (lists of lists). Raise ValueError if the inner\n"
                  "    dimensions don't match.",
        "test_code": """
import pytest

def test_solution():
    from solution import matrix_multiply
    assert matrix_multiply([[1,2],[3,4]], [[5,6],[7,8]]) == [[19,22],[43,50]]
    assert matrix_multiply([[1,2,3]], [[1],[1],[1]]) == [[6]]
    with pytest.raises(ValueError):
        matrix_multiply([[1,2]], [[1,2]])
""",
    },
    {
        "id": 15, "difficulty": "easy", "function_name": "binary_search_insert_position",
        "prompt": "def binary_search_insert_position(nums: list, target: int) -> int:\n"
                  "    nums is sorted ascending. Return the index where target should be inserted\n"
                  "    to keep it sorted (leftmost valid position if target already present).",
        "test_code": """
def test_solution():
    from solution import binary_search_insert_position as f
    assert f([1,3,5,6], 5) == 2
    assert f([1,3,5,6], 2) == 1
    assert f([1,3,5,6], 7) == 4
    assert f([], 3) == 0
    assert f([1,1,1], 1) == 0
""",
    },
    {
        "id": 16, "difficulty": "medium", "function_name": "quicksort",
        "prompt": "def quicksort(nums: list) -> list:\n"
                  "    Return a new sorted list (ascending). Do not mutate the input.",
        "test_code": """
def test_solution():
    from solution import quicksort
    original = [5,3,8,1,9,2]
    result = quicksort(original)
    assert result == [1,2,3,5,8,9]
    assert original == [5,3,8,1,9,2]
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
    assert quicksort([2,2,1,1]) == [1,1,2,2]
""",
    },
    {
        "id": 17, "difficulty": "hard", "function_name": "word_break",
        "prompt": "def word_break(s: str, word_dict: list) -> bool:\n"
                  "    Return True if s can be segmented into a space-separated sequence of one or\n"
                  "    more words from word_dict. Words may be reused.",
        "test_code": """
def test_solution():
    from solution import word_break
    assert word_break("leetcode", ["leet","code"]) == True
    assert word_break("applepenapple", ["apple","pen"]) == True
    assert word_break("catsandog", ["cats","dog","sand","and","cat"]) == False
    assert word_break("", ["a"]) == True
    assert word_break("a", []) == False
""",
    },
    {
        "id": 18, "difficulty": "hard", "function_name": "coin_change_min",
        "prompt": "def coin_change_min(coins: list, amount: int) -> int:\n"
                  "    Return the minimum number of coins needed to make amount, or -1 if\n"
                  "    impossible. amount=0 returns 0.",
        "test_code": """
def test_solution():
    from solution import coin_change_min
    assert coin_change_min([1,2,5], 11) == 3
    assert coin_change_min([2], 3) == -1
    assert coin_change_min([1], 0) == 0
    assert coin_change_min([1,3,4], 6) == 2
""",
    },
    {
        "id": 19, "difficulty": "hard", "function_name": "sliding_window_max",
        "prompt": "def sliding_window_max(nums: list, k: int) -> list:\n"
                  "    Return the max of every contiguous window of size k, in order.",
        "test_code": """
def test_solution():
    from solution import sliding_window_max
    assert sliding_window_max([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert sliding_window_max([1], 1) == [1]
    assert sliding_window_max([9,8,7,6], 2) == [9,8,7]
""",
    },
    {
        "id": 20, "difficulty": "hard", "function_name": "dijkstra_shortest_path",
        "prompt": "def dijkstra_shortest_path(graph: dict, start, end) -> int:\n"
                  "    graph maps node -> dict of neighbor -> non-negative edge weight.\n"
                  "    Return the shortest path distance from start to end, or -1 if unreachable.",
        "test_code": """
def test_solution():
    from solution import dijkstra_shortest_path as f
    g = {
        "a": {"b": 1, "c": 4},
        "b": {"c": 2, "d": 5},
        "c": {"d": 1},
        "d": {},
    }
    assert f(g, "a", "d") == 4
    assert f(g, "a", "a") == 0
    assert f({"a": {}, "b": {}}, "a", "b") == -1
""",
    },
    {
        "id": 21, "difficulty": "hard", "function_name": "is_valid_bst_preorder",
        "prompt": "def is_valid_bst_preorder(preorder: list) -> bool:\n"
                  "    Given a list of unique integers, return True if it could be the preorder\n"
                  "    traversal of a valid binary search tree.",
        "test_code": """
def test_solution():
    from solution import is_valid_bst_preorder as f
    assert f([5,2,1,3,6]) == True
    assert f([5,2,6,1,3]) == False
    assert f([]) == True
    assert f([1]) == True
    assert f([2,1,3]) == True
""",
    },
    {
        "id": 22, "difficulty": "medium", "function_name": "rotate_matrix_90",
        "prompt": "def rotate_matrix_90(matrix: list) -> list:\n"
                  "    Return a new NxN matrix rotated 90 degrees clockwise. Do not mutate input.",
        "test_code": """
def test_solution():
    from solution import rotate_matrix_90
    m = [[1,2],[3,4]]
    result = rotate_matrix_90(m)
    assert result == [[3,1],[4,2]]
    assert m == [[1,2],[3,4]]
    assert rotate_matrix_90([[1]]) == [[1]]
    assert rotate_matrix_90([[1,2,3],[4,5,6],[7,8,9]]) == [[7,4,1],[8,5,2],[9,6,3]]
""",
    },
    {
        "id": 23, "difficulty": "hard", "function_name": "longest_common_subsequence",
        "prompt": "def longest_common_subsequence(a: str, b: str) -> str:\n"
                  "    Return the longest common subsequence of a and b. If multiple subsequences\n"
                  "    share the max length, any one of them is accepted.",
        "test_code": """
def test_solution():
    from solution import longest_common_subsequence as f

    def is_subsequence(sub, s):
        it = iter(s)
        return all(c in it for c in sub)

    result = f("abcde", "ace")
    assert len(result) == 3
    assert is_subsequence(result, "abcde") and is_subsequence(result, "ace")

    result2 = f("abc", "abc")
    assert result2 == "abc"

    result3 = f("abc", "def")
    assert result3 == ""
""",
    },
    {
        "id": 24, "difficulty": "medium", "function_name": "permutations_unique",
        "prompt": "def permutations_unique(nums: list) -> list:\n"
                  "    Return all unique permutations of nums (which may contain duplicates).\n"
                  "    Order of the outer list does not matter.",
        "test_code": """
def test_solution():
    from solution import permutations_unique as f
    result = {tuple(p) for p in f([1,1,2])}
    expected = {(1,1,2),(1,2,1),(2,1,1)}
    assert result == expected
    assert {tuple(p) for p in f([1])} == {(1,)}
    assert len(f([1,2,3])) == 6
""",
    },
    {
        "id": 25, "difficulty": "easy", "function_name": "is_prime",
        "prompt": "def is_prime(n: int) -> bool:\n"
                  "    Return True if n is a prime number. n may be negative, 0, or 1.",
        "test_code": """
def test_solution():
    from solution import is_prime
    assert is_prime(2) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-7) == False
    assert is_prime(97) == True
    assert is_prime(100) == False
""",
    },
    {
        "id": 26, "difficulty": "easy", "function_name": "gcd_of_list",
        "prompt": "def gcd_of_list(nums: list) -> int:\n"
                  "    Return the greatest common divisor of all numbers in the list.",
        "test_code": """
def test_solution():
    from solution import gcd_of_list
    assert gcd_of_list([12, 18, 24]) == 6
    assert gcd_of_list([7]) == 7
    assert gcd_of_list([5, 10, 15, 25]) == 5
    assert gcd_of_list([1, 2, 3]) == 1
""",
    },
    {
        "id": 27, "difficulty": "medium", "function_name": "deep_equal",
        "prompt": "def deep_equal(a, b) -> bool:\n"
                  "    Recursively compare two values (which may be nested lists/tuples/dicts/\n"
                  "    scalars) for structural equality. Lists and tuples are NOT interchangeable.",
        "test_code": """
def test_solution():
    from solution import deep_equal
    assert deep_equal([1, [2, 3]], [1, [2, 3]]) == True
    assert deep_equal([1, [2, 3]], [1, [2, 4]]) == False
    assert deep_equal({"a": [1, 2]}, {"a": [1, 2]}) == True
    assert deep_equal((1, 2), [1, 2]) == False
    assert deep_equal({"a": 1, "b": 2}, {"b": 2, "a": 1}) == True
""",
    },
    {
        "id": 28, "difficulty": "easy", "function_name": "find_missing_number",
        "prompt": "def find_missing_number(nums: list) -> int:\n"
                  "    nums contains n distinct numbers from the range 0..n with exactly one\n"
                  "    missing. Return the missing number.",
        "test_code": """
def test_solution():
    from solution import find_missing_number
    assert find_missing_number([3,0,1]) == 2
    assert find_missing_number([0,1]) == 2
    assert find_missing_number([9,6,4,2,3,5,7,0,1]) == 8
    assert find_missing_number([1]) == 0
""",
    },
    {
        "id": 29, "difficulty": "hard", "function_name": "text_justify",
        "prompt": "def text_justify(words: list, max_width: int) -> list:\n"
                  "    Format words into lines of exactly max_width characters, fully justified\n"
                  "    (extra spaces distributed as evenly as possible, leftmost gaps get more).\n"
                  "    The last line is left-justified with a single space between words and\n"
                  "    padded with trailing spaces to max_width.",
        "test_code": """
def test_solution():
    from solution import text_justify
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    result = text_justify(words, 16)
    assert all(len(line) == 16 for line in result)
    last_words = result[-1].rstrip("\\n").rstrip().split(" ")
    assert " ".join(last_words) == result[-1].rstrip()
    assert "  " not in result[-1].rstrip()
    all_words_in_order = []
    for line in result:
        all_words_in_order.extend(w for w in line.strip().split(" ") if w)
    assert all_words_in_order == words
""",
    },
    {
        "id": 30, "difficulty": "easy", "function_name": "roman_to_int",
        "prompt": "def roman_to_int(s: str) -> int:\n"
                  "    Convert a Roman numeral string to an integer. Input is a valid Roman\n"
                  "    numeral between 1 and 3999.",
        "test_code": """
def test_solution():
    from solution import roman_to_int
    assert roman_to_int("III") == 3
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994
""",
    },
]
