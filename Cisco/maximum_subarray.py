def maxSubArray(nums):
    max_current = max_global = nums[0]
    nums_final = nums[1:]
    for x in nums_final:
        max_current = max(x, x+max_current)
        max_global = max(max_current, max_global)
    
    return max_global

if __name__ == "__main__":
    nums = [5,4,-1,7,8]
    return_value = maxSubArray(nums)
    
    print(return_value)