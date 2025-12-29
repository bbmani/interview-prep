def isAnagram(s, t):
	if len(s) != len(t): return False
		
	char_s, char_t = {}, {}

	for char in s:
		if char in char_s:
			char_s[char] += 1
		else:
			char_s[char] = 1
	
	for char in t:
		if char in char_t:
			char_t[char] += 1
		else:
			char_t[char] = 1
		
	return char_s == char_t

def main():
	inputs = [["anagram", "nagaram"],["rat", "car"]]
	for input in inputs:
		return_value = isAnagram(input[0], input[1])
		print(return_value)

if __name__ == "__main__":
	main()
