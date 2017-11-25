
def twoSum(nums, target):
    diff_cache = {}
    for i in range(len(nums)):
        x = nums[i]
        if x in diff_cache: return sorted([diff_cache[x], i])
        else: diff_cache[target - x] = i
    assert 0, "no solution"

if __name__ == "__main__":
    nums   = [2, 7, 11, 15]
    target = 9
    sol    = twoSum(nums, target)
    print(sol)
    assert sol == [0, 1]

    target = 17
    sol    = twoSum(nums, target)
    print(sol)
    assert sol == [0, 3]
