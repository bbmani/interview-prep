def isPalindrome(s):
    if len(s) == 1:
         return True
    # Start Index
    start = 0

    # End index
    end = len(s) - 1
    
    while start < end:
        front = s[start]
        rear = s[end]

        if not front.isalnum():
            start += 1
            continue
        if not rear.isalnum():
            end -= 1
            continue
        
        front = front.lower()
        rear = rear.lower()

        if front != rear:
            return False
        
        start += 1
        end -= 1

    return True

def main():
    inputs = ["A man, a plan, a canal: Panama", "race a car", " "]

    for inp in inputs:
        return_value = isPalindrome(inp)
        print(return_value)
if __name__ == "__main__":
    main()
