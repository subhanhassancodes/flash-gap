import re
import heapq
from collections import Counter, defaultdict


def is_palindrome(s):
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]


def flatten(nested):
    out = []
    for item in nested:
        if isinstance(item, list):
            out.extend(flatten(item))
        else:
            out.append(item)
    return out


def most_frequent(items):
    counts = Counter(items)
    max_count = max(counts.values())
    candidates = [k for k, v in counts.items() if v == max_count]
    return min(candidates)


def caesar_cipher(s, shift):
    result = []
    for c in s:
        if c.isupper():
            result.append(chr((ord(c) - 65 + shift) % 26 + 65))
        elif c.islower():
            result.append(chr((ord(c) - 97 + shift) % 26 + 97))
        else:
            result.append(c)
    return "".join(result)


def merge_intervals(intervals):
    if not intervals:
        return []
    ivs = sorted(intervals)
    merged = [ivs[0]]
    for start, end in ivs[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged


def is_valid_parens(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False
    return not stack


def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups[tuple(sorted(w))].append(w)
    return list(groups.values())


def longest_increasing_subsequence_length(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def min_edit_distance(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]


def topological_sort(graph):
    visited = {}
    order = []

    def visit(node):
        if visited.get(node) == 1:
            raise ValueError("cycle detected")
        if visited.get(node) == 2:
            return
        visited[node] = 1
        for neighbor in graph.get(node, []):
            visit(neighbor)
        visited[node] = 2
        order.append(node)

    for node in graph:
        if node not in visited:
            visit(node)
    return order[::-1]


def run_length_encode(s):
    if not s:
        return ""
    out = []
    prev = s[0]
    count = 1
    for c in s[1:]:
        if c == prev:
            count += 1
        else:
            out.append(f"{count}{prev}")
            prev = c
            count = 1
    out.append(f"{count}{prev}")
    return "".join(out)


def run_length_decode(s):
    out = []
    for count, char in re.findall(r"(\d+)(\D)", s):
        out.append(char * int(count))
    return "".join(out)


def matrix_transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matrix_multiply(a, b):
    if len(a[0]) != len(b):
        raise ValueError("incompatible dimensions")
    result = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            result[i][j] = sum(a[i][k] * b[k][j] for k in range(len(b)))
    return result


def binary_search_insert_position(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def quicksort(nums):
    return sorted(nums)


def word_break(s, word_dict):
    words = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[len(s)]


def coin_change_min(coins, amount):
    dp = [0] + [float("inf")] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1


def sliding_window_max(nums, k):
    from collections import deque
    dq = deque()
    out = []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] <= n:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out


def dijkstra_shortest_path(graph, start, end):
    dist = {start: 0}
    pq = [(0, start)]
    visited = set()
    while pq:
        d, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        if node == end:
            return d
        for neighbor, weight in graph.get(node, {}).items():
            nd = d + weight
            if nd < dist.get(neighbor, float("inf")):
                dist[neighbor] = nd
                heapq.heappush(pq, (nd, neighbor))
    return dist.get(end, -1)


def is_valid_bst_preorder(preorder):
    stack = []
    lower = float("-inf")
    for val in preorder:
        if val <= lower:
            return False
        while stack and stack[-1] < val:
            lower = stack.pop()
        stack.append(val)
    return True


def rotate_matrix_90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]


def longest_common_subsequence(a, b):
    m, n = len(a), len(b)
    dp = [[""] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + a[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
    return dp[m][n]


def permutations_unique(nums):
    from itertools import permutations
    return [list(p) for p in set(permutations(nums))]


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd_of_list(nums):
    from math import gcd
    from functools import reduce
    return reduce(gcd, nums)


def deep_equal(a, b):
    if type(a) != type(b):
        return False
    if isinstance(a, (list, tuple)):
        if len(a) != len(b):
            return False
        return all(deep_equal(x, y) for x, y in zip(a, b))
    if isinstance(a, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        return all(deep_equal(a[k], b[k]) for k in a)
    return a == b


def find_missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


def text_justify(words, max_width):
    lines = []
    current = []
    current_len = 0
    for word in words:
        if current_len + len(current) + len(word) > max_width:
            if len(current) == 1:
                lines.append(current[0] + " " * (max_width - len(current[0])))
            else:
                spaces = max_width - current_len
                gaps = len(current) - 1
                base, extra = divmod(spaces, gaps)
                line = ""
                for i, w in enumerate(current[:-1]):
                    line += w + " " * (base + (1 if i < extra else 0))
                line += current[-1]
                lines.append(line)
            current = []
            current_len = 0
        current.append(word)
        current_len += len(word)
    last_line = " ".join(current)
    last_line += " " * (max_width - len(last_line))
    lines.append(last_line)
    return lines


def roman_to_int(s):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i, c in enumerate(s):
        val = values[c]
        if i + 1 < len(s) and val < values[s[i + 1]]:
            total -= val
        else:
            total += val
    return total
