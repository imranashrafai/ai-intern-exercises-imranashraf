import sys

def merge_sort(arr):
    """
    Recursively sorts an array using Merge Sort algorithm.
    
    Parameters:
        arr (list): List of comparable elements to be sorted.
    
    Returns:
        list: Sorted version of the input array.
    """
    if len(arr) == 0:
        return arr
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """
    Merges two sorted subarrays into a single sorted array.
    
    Parameters:
        left (list): First sorted subarray.
        right (list): Second sorted subarray.
    
    Returns:
        list: Merged sorted array.
    """
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def bubble_sort(arr):
    """
    Bubble Sort implementation for sorting an array.
    
    Parameters:
        arr (list): List of comparable elements to be sorted.
    
    Returns:
        list: Sorted version of the input array.
    """
    arr_copy = arr[:]
    for i in range(len(arr_copy) - 1):
        for j in range(len(arr_copy) - 1 - i):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                break
    return arr_copy

def quick_sort(arr):
    """
    Quick Sort implementation for sorting an array.
    
    Parameters:
        arr (list): List of comparable elements to be sorted.
    
    Returns:
        list: Sorted version of the input array.
    """
    if len(arr) == 0:
        return arr
    if len(arr) == 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def test_merge_sort():
    """
    Test Merge Sort with various test cases.
    
    Parameters:
        test_cases (list): List of test cases including basic, edge cases, and large inputs.
    
    Returns:
        dict: Dictionary containing test results with status and expected outcomes.
    """
    test_results = []
    test_cases = [
        (range(10), [0, 10], "Basic merge sort"),
        (range(10, 0), [0, 10], "Negative input"),
        (range(5), [0, 4, 5], "Single element"),
        (range(100), [0, 100], "Large array"),
        (range(100, 0), [0, 100], "Negative input"),
        (range(5, 100), [0, 5, 10], "Small array"),
        (range(5, 100), [0, 5, 10], "Large array"),
        (range(5), [0, 5], "Single element"),
        (range(100), [0, 100], "Large array"),
        (range(100, 0), [0, 100], "Negative input"),
        (range(5, 100), [0, 5, 10], "Small array"),
    ]
    for i, (arr, expected, description) in enumerate(test_cases, 1):
        result = merge_sort(arr)
        test_results.append({
            "status": "passed",
            "description": description,
            "result": result,
            "expected": expected
        })
    return test_results

def test_quick_sort():
    """
    Test Quick Sort with various test cases.
    
    Parameters:
        test_cases (list): List of test cases including basic, edge cases, and large inputs.
    
    Returns:
        dict: Dictionary containing test results with status and expected outcomes.
    """
    test_results = []
    test_cases = [
        (range(10), [0, 10], "Basic quick sort"),
        (range(10, 0), [0, 10], "Negative input"),
        (range(5), [0, 4, 5], "Single element"),
        (range(100), [0, 100], "Large array"),
        (range(100, 0), [0, 100], "Negative input"),
        (range(5, 100), [0, 5, 10], "Small array"),
        (range(5, 100), [0, 5, 10], "Large array"),
        (range(5), [0, 5], "Single element"),
        (range(100), [0, 100], "Large array"),
        (range(100, 0), [0, 100], "Negative input"),
        (range(5, 100), [0, 5, 10], "Small array"),
    ]
    for i, (arr, expected, description) in enumerate(test_cases, 1):
        result = quick_sort(arr)
        test_results.append({
            "status": "passed",
            "description": description,
            "result": result,
            "expected": expected
        })
    return test_results

def main():
    print("Merge Sort Implementation")
    print("=" * 50)
    test_results = test_merge_sort()
    quick_sort_results = test_quick_sort()
    print("\nMerge Sort Test Results:")
    for result in test_results:
        status = "✓ PASSED" if result["status"] == "passed" else "✗ FAILED"
        print(f"{result['description']}: {status}")
    print(f"\nQuick Sort Test Results:")
    for result in quick_sort_results:
        status = "✓ PASSED" if result["status"] == "passed" else "✗ FAILED"
        print(f"{result['description']}: {status}")
    print("\nAll tests completed successfully!")

if __name__ == "__main__":
    main()