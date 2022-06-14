import heapq

def kth_largest_element(arr, k):
	h = list()
	for ele in arr:
		if len(h) < k:
			heapq.heappush(h, ele)
		else:
			if ele > h[0]:
				heapq.heappop(h)
				heapq.heappush(h, ele)
	print(h[0])

if __name__ == '__main__':
	# only works if it contains all distinct elements
	arr = [5, 6, 2, 8, 9, 3, 10, 21, 31]
	kth_largest_element(arr, 1)