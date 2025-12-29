def containsDuplicate(input):
    duplicate_array = {}

    for number in input:
        if number in duplicate_array:
            return True
        else:
            duplicate_array[number] = 1

    return False


def main():
    inputs = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]

    for input in inputs:
        return_value = containsDuplicate(input)
        print(return_value)

if __name__ == "__main__":
    main()
