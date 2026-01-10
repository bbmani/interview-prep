def heightChecker(heights):
    counter_array = [0] * 100

    for h in heights:
        counter_array[h-1] += 1

    print(counter_array)

    expected = []

    for idx, counter in enumerate(counter_array):
        if counter != 0:
            expected += [idx+1] * counter

    count = 0

    for h, a_h in zip(heights, expected):
        if h != a_h:
            count += 1
    
    return count

def main():
    inputs = [[1,1,4,2,1,3], [5,1,2,3,4], [1,2,3,4,5]]

    for inp in inputs:
        return_value = heightChecker(inp)
        print(return_value)

if __name__ == "__main__":
    main()
