class Solution:
    
    # Function 1: Sort 0s, 1s, and 2s
    def sort012(self, arr):
        low = 0
        mid = 0
        high = len(arr) - 1

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1

            elif arr[mid] == 1:
                mid += 1

            else:  # arr[mid] == 2
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1


    # Function 2: Binary search (first occurrence)
    def binarysearch(self, arr, k):
        left = 0
        right = len(arr) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == k:
                result = mid
                right = mid - 1   # keep searching left

            elif arr[mid] < k:
                left = mid + 1

            else:
                right = mid - 1

        return result