def find_minimum(nums: list[int]) -> float | None:
    minimum = float("inf")
    if not nums:
        return None
    for n in nums:
        if n < minimum:
            minimum = n
    return minimum