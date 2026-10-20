"""Question 50: Remove duplicates from a sorted list.

Given a sorted list, return a new list containing each value only once.
Keep the original order.
"""


def remove_duplicates(numbers: list[int]) -> list[int]:
    """Return the unique values in O(n) time."""
    unique = []

    for number in numbers:
        if not unique or number != unique[-1]:
            unique.append(number)

    return unique


if __name__ == "__main__":
    print(remove_duplicates([1, 1, 2, 2, 2, 3, 4, 4]))  # [1, 2, 3, 4]
