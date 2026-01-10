def productExceptSelf(nums):
    res = [1] * len(nums)

    # Prefix calculation
    prefix = 1
    for idx in range(len(nums)):
        res[idx] = prefix
        prefix = prefix * nums[idx]
        
        print(f"Nums Array: {nums}")
        print(f"Result after {idx + 1}th round in prefix: {res}")
        print(f"Prefix after iteration: {prefix}")
        print("\n")

    # Postfix calculation
    postfix = 1

    # Iterate backwards until the index 0 (inclusive)
    for idx in range(len(nums) - 1, -1, -1):
        # Multiply with the result array so that we dont overwrite the value
        res[idx] = res[idx] * postfix
        postfix = postfix * nums[idx]
        
        print(f"Nums Array: {nums}")
        print(f"Result after {idx + 1}th round in postfix: {res}")
        print(f"Postfix value: {postfix}")
        print(f"\n")

    return res


def main():
    inputs = [[1,2,3,4], [-1, 1, 0, -3, 3]]

    for inp in inputs:
        return_value = productExceptSelf(inp)
        print(return_value)
        print("\n\n")

if __name__ == "__main__":
    main()
