class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary to store numbers and their indices
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement
            if complement in hashmap:  # Check if complement is already in the hash map
                return [hashmap[complement], i]  # Return the indices
            hashmap[num] = i  # Add the current number and its index to the hash map
