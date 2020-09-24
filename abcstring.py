# mergesort and merge functions copied from some mergesort python example, can't remember which one

def mergeSort(arr, temp_arr, left, right):

    inversionCount = 0
  
    if left < right: 

        mid = (left + right)//2
        inversionCount += mergeSort(arr, temp_arr, left, mid) 
        inversionCount += mergeSort(arr, temp_arr, mid + 1, right) 
        inversionCount += merge(arr, temp_arr, left, mid, right) 

    return inversionCount 
  
def merge(arr, temp_arr, left, mid, right): 
	i = left   
	j = mid + 1  
	k = left   
	inversionCount = 0

	while i <= mid and j <= right: 
		if arr[i] <= arr[j]: 
				temp_arr[k] = arr[i] 
				k += 1
				i += 1
		else: 
				temp_arr[k] = arr[j] 
				inversionCount += (mid-i + 1) 
				k += 1
				j += 1

	while i <= mid: 
			temp_arr[k] = arr[i] 
			k += 1
			i += 1

	while j <= right: 
			temp_arr[k] = arr[j] 
			k += 1
			j += 1

	for loop_var in range(left, right + 1): 
			arr[loop_var] = temp_arr[loop_var] 
				
	return inversionCount 

def solve(s):
	arr = list(s)
	n = len(arr) 
	helperArray = [0]*n

	return mergeSort(arr, helperArray, 0, n-1)

if __name__ == "__main__":
    print(solve("CCAABB")) # 4
    print(solve("CBACBA")) # 3
    print(solve("AAAA")) # 0