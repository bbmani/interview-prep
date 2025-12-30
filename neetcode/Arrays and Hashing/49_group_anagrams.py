from collections import Counter

def groupAnagrams(strs):
	if len(strs) == 1:
		return [strs]

	fo_dict = {}
	for input in strs:
		counter_input = [0] * 26
		for char in input:
			counter_input[int(ord(char) - ord('a'))] += 1
		
		counter_input = tuple(counter_input)
		if counter_input in fo_dict:
			fo_dict[counter_input].append(input)
		else:
			fo_dict[counter_input] = [input]
	return [value for value in fo_dict.values()]
def main():
	inputs = [["eat","tea","tan","ate","nat","bat"], [""], ["a"]]
	for input in inputs:
		return_value = groupAnagrams(input)
		print(return_value)

if __name__ == "__main__":
	main()
