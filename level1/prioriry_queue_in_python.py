import heapq

# min heap sort
class Heap:
	def __init__(self):
		self.min_heap = list()
		self.max_heap = list()

	def min_heap_push(self, priority, str1):
		heapq.heappush(self.min_heap, (priority, str1))

	def max_heap_push(self, priority, str1):
		heapq.heappush(self.max_heap, ( (-1) * priority, str1))

	def print_min_heap(self):
		while len(self.min_heap):
			print(heapq.heappop(self.min_heap))

	def print_max_heap(self):
		while len(self.max_heap):
			score, value= heapq.heappop(self.max_heap)
			print((-1 * score, value))

if __name__ == '__main__':
	h = Heap()

	# min heap
	h.min_heap_push(1, "ANZO")
	h.min_heap_push(2, "Ashmita")
	h.min_heap_push(2, "Arun")
	h.min_heap_push(1, "Ashok")
	h.min_heap_push(1, "SUNITA")
	h.print_min_heap()

	# max heap
	h.max_heap_push(1, "ANZO")
	h.max_heap_push(2, "Ashmita")
	h.max_heap_push(2, "Arun")
	h.max_heap_push(1, "Ashok")
	h.max_heap_push(1, "SUNITA")
	h.print_max_heap()
