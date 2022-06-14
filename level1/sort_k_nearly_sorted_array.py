import heapq

def sort_k_sorted_array(arr, k):
	N = len(arr)
	h = list()
	sorted_list = list()
	for i in range(min(k+1, N)):
		heapq.heappush(h, arr[i])

	for i in range(min(k + 1, N), N):
		sorted_list.append(heapq.heappop(h))
		heapq.heappush(h, arr[i])
	print(h)
	while len(h)!=0:
		sorted_list.append(heapq.heappop(h))
	return sorted_list

if __name__ == '__main__':
	arr = [2, 3, 1, 4, 6, 7, 5, 8, 9]
	print(sort_k_sorted_array(arr, 6))