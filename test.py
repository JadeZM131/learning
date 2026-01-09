def minOperations(nums, x: int) -> int:
    left = s_w = max_win = 0
    s = sum(nums)
    l = len(nums)

    for r, n in enumerate(nums):
        s_w += n
        if s_w < s - x:
            continue

        if s_w == s - x:
            max_win = max(max_win, r - left + 1)

        while s_w > s - x:
            s_w -= nums[left]
            left += 1

    return l - max_win


nums = [1, 1, 4, 2, 3]
print(minOperations(nums, 3))
