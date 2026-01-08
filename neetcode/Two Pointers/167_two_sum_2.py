def twoSum(numbers, target):
    start = 0
    end = len(numbers) - 1

    while start < end:
        two_sum = numbers[start] + numbers[end]

        if two_sum > target:
            end -= 1
        elif two_sum < target:
            start += 1
        elif two_sum == target:
            return [start + 1, end + 1]

def main():
    inputs = [[[2,7,11,15], 9], [[2,3,4], 6], [[-1, 0], -1]]

    for inp in inputs:
        return_value = twoSum(inp[0], inp[1])
        print(return_value)

if __name__ == "__main__":
    main()
