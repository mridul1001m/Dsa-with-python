def find_max(arr, low, high):
    # Base case: only one element
    if low == high:
        return arr[low]
    
    # Divide
    mid = (low + high)//2

    # Conquer
    left_max = find_max(arr, low, mid)
    right_max = find_max(arr, mid + 1, high)

    # Combine
    return max(left_max, right_max)

# Example usage
numbers = [0,55,6,7,33,4,55,1]
result = find_max(numbers, 0, len(numbers) - 1)
print("Maximum number is:", result)