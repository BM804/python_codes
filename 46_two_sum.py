"""Question 46: Find two numbers that add up to a target.

Given a list of integers and a target, return the indexes of two different
numbers whose sum equals the target. Assume exactly one answer exists.
"""


def two_sum(numbers: list[int], target: int) -> tuple[int, int]:
    """Return the indexes of a pair that adds up to target.

    Runs in O(n) time using O(n) extra space.
    """
    index_by_value = {}

    for index, number in enumerate(numbers):
        needed = target - number
        if needed in index_by_value:
            return index_by_value[needed], index
        index_by_value[number] = index

    raise ValueError("No pair adds up to the target")


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # (0, 1)
