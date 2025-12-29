# Two Sum
# Using Hashmap to track the difference and their indices

# Time Complexity = O(n)

def twoSum(nums, target):
	map = {}

	for idx, num in enumerate(nums):
		diff = target - num
		if diff in map:
			return [map[diff], idx]
		map[num] = idx

def main():
	inputs = [[[2, 7, 11, 15], 9], [[3, 2, 4], 6], [[3, 3], 6]]
	for input in inputs:
		return_value = twoSum(input[0], input[1])
		print(return_value)

if __name__ == "__main__":
	main()
