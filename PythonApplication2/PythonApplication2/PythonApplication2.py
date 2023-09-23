from concurrent.futures.process import _ResultItem


def twoSum(nums, target):
    result = []
    for v , i in enumerate(nums):
        while v < len(nums)-1:
            if nums[i]+ nums[i+1] == target:
                result.append(v)
                result.append(v+1)
                return result
            else:
                continue
    
# Example usage
nums = [11, 7, 2, 15]
target = 9
result = twoSum(nums, target)
if result:
    print("Pair found:", result)
else:
    print("No pair found.")
