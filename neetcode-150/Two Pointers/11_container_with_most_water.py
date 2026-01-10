def maxArea(heights: list[int]) -> int:
    l = 0
    r = len(heights) - 1

    res = -1

    while l < r:
        volume = min(heights[l], heights[r]) * (r - l)
        print(f"Volume: {volume} R: {r} L: {l}")
        res = max(res, volume)

        if l <= r:
            l +=1 
        else: 
            r += 1

    return res

def main():
    inputs = [[1,8,6,2,5,4,8,3,7], [1, 1]]

    for idx in inputs:
        return_value = maxArea(idx)
        print(return_value)

if __name__ == "__main__":
    main()
