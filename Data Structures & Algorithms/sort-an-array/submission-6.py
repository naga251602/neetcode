class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            j = i - 1
            key = arr[i]

            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j+1] = key
        return arr