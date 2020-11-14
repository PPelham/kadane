# Find the maximum subarray sum
# Using the Kadane's Algorithm
# ie. [1, -3, 2, 1, -1] => [-3], [2, 1], [1, -3, 2, 1, -1]
# Brute force would take O(n^2)
# Kadane's Algorithm takes O(n)
# Big O is Time Complexity

def kadane(A):
	max_current = max_global = A[0]
	for i in range(1, len(A)):
		max_current = max(A[i], max_current + A[i])
		if max_current > max_global:
			max_global = max_current
	return max_global

A = [-2, 3, 2, -1]
print(kadane(A))
