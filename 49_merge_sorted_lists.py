"""Question 49: Merge two sorted lists.

Given two lists of integers sorted in ascending order, return one sorted list
containing all their values.
"""


def merge_sorted(first: list[int], second: list[int]) -> list[int]:
    """Merge the lists in O(n + m) time and O(n + m) result space."""
    merged = []
    left = right = 0

    while left < len(first) and right < len(second):
        if first[left] <= second[right]:
            merged.append(first[left])
            left += 1
        else:
            merged.append(second[right])
            right += 1

    merged.extend(first[left:])
    merged.extend(second[right:])
    return merged


if __name__ == "__main__":
    print(merge_sorted([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
