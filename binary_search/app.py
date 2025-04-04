# Function to perform Binary Search
def binary_search(arr, target):
    # Initial low and high indices
    low = 0
    high = len(arr) - 1
    
    # While loop runs until low and high pointers cross
    while low <= high:
        mid = (low + high) // 2  # Finding middle index
        
        # If the target is found at mid index, return the index
        if arr[mid] == target:
            return mid
        # If the target is greater than the mid value, search in the right half
        elif arr[mid] < target:
            low = mid + 1
        # If the target is smaller than the mid value, search in the left half
        else:
            high = mid - 1
    
    # If the target is not found, return -1
    return -1

# Driver code to test the binary search
if __name__ == "__main__":
    # Sorted array for binary search
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    
    # Target element to search
    target = int(input("Enter the number you want to search: "))
    
    # Calling the binary_search function
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in the list.")
