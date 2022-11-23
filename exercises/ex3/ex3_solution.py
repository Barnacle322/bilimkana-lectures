# Развернутое решение
def same_first_last(nums: list) -> bool:
    if nums[0] == nums[-1]:
        return True
    else:
        return False


print(same_first_last([1, 2, 3, 1]))  # True

# Короткое решение
def same_first_last(nums: list) -> bool:
    return nums[0] == nums[-1]


print(same_first_last([1, 2, 3, 4]))  # False

# Еще короче решение
func = lambda nums: nums[0] == nums[-1]
print(func([1, 2, 3, 1]))  # True
