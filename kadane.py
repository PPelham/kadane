# Find the maximum subarray's sum using the Kadane's Algorithm
# ie. [1, -3, 2, 1, -1] => [-3], [2, 1], [1, -3, 2, 1, -1]

def kadane(A):
	max_current = max_global = A[0]
	for i in range(1, len(A)):
		max_current = max(A[i], max_current + A[i])
		if max_current > max_global:
			max_global = max_current
	return max_global

A = [-2, 3, 2, -1]
print(kadane(A))
