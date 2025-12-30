def topKFrequent(nums, k):
	count = {}
	
	for num in nums:
		if num in count:
			count[num] += 1
		else:
			count[num] = 1
	
		
	frequency = [[] for idx in range(len(nums) + 1)]
	
	for num, cnt in count.items():
		frequency[cnt].append(num)
	
	result = []
	
	for idx in range(len(frequency) - 1, 0, -1):
		for res in frequency[idx]:
			result.append(res)
			if len(result) == k:
				return result
				


def main():
	inputs = [[[1,1,1,2,2,3], 2], [[1], 1], [[1,2,1,2,1,2,3,1,3,2], 2]]
	for input in inputs:
		return_value = topKFrequent(input[0], input[1])
		print(return_value)

if __name__ == "__main__":
	main()
