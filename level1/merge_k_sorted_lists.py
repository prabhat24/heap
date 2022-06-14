# merge k sorted lists
import heapq

def merge_lists(arr2d):
	h = list()
	result = list()
	for each_list in arr2d:
		heapq.heappush(h, (each_list[0], each_list, 0))

	while len(h) != 0:
		value, lst, ind = heapq.heappop(h)
		result.append(value)
		if ind + 1 < len(lst):
			heapq.heappush(h, (lst[ind+1], lst, ind + 1))
	return result

if __name__ == '__main__':
	arr2d = [
		[10, 20, 30, 40, 50], 
		[5, 7, 9, 11, 19, 55, 57],
		[1, 2, 3],
		[32, 39]
	]

	print(merge_lists(arr2d))
