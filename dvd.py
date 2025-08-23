def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    
    mid = len(arr) // 2
    l_max = find_max(arr[:mid])
    r_max = find_max(arr[mid:])
    
    return max(l_max, r_max)

# Example usage
numbers = [3, 8, 2, 5, 10, 7, 6, 12]
print("Maximum number is:", find_max(numbers))
