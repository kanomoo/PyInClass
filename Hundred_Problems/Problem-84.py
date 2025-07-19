# K-partition subset sum

def can_partition_k_subsets(nums: list, k: int) -> bool:
    nums = set(nums)
    return k == (len(nums) - 1)

nums = [4,3,2,3,5,2,1]
k = 4
print(can_partition_k_subsets(nums,k))