# heap implementation using self.heapays

class Heap():

	def __init__(self):
		self.heap = list()

	@staticmethod
	def get_parent_ind(ci):
		return (ci -1)//2

	@staticmethod
	def get_child_indices(pi):
		return  (2 * pi + 1), (2 * pi + 2)


	def heap_push(self, ele):
		self.heap.append(ele)
		ind = len(self.heap) - 1
		parent_ind = self.get_parent_ind(ind)

		while parent_ind >= 0 and self.heap[parent_ind] > ele:
			temp = self.heap[parent_ind]
			self.heap[parent_ind] = ele
			self.heap[ind] = temp
			ind = self.get_parent_ind(ind)
			parent_ind = self.get_parent_ind(ind) 

	def heap_pop(self):
		# swap peak node and end node
		temp = self.heap[0]
		self.heap[0] = self.heap[len(self.heap)-1]
		self.heap[len(self.heap)-1] = temp

		# remove the end of the heap
		self.heap.pop(len(self.heap) - 1)

		# down heapify
		ind = 0
		c1, c2 = self.get_child_indices(ind)
		while True:
			if c2 < len(self.heap) and min(self.heap[c1], self.heap[c2]) < self.heap[ind]:
				if self.heap[c1] < self.heap[c2]:
					self.heap[c1], self.heap[ind] =  self.heap[ind], self.heap[c1]
					ind = c1
				else:
					self.heap[c2], self.heap[ind] = self.heap[ind], self.heap[c2]
					ind = c2
			elif c1 < len(self.heap) and self.heap[c1] < self.heap[ind]:
				self.heap[c1], self.heap[ind] = self.heap[ind], self.heap[c1]
				ind = c1
			else:
				break
			c1, c2 = self.get_child_indices(ind)



	def __str__(self):
		return str(self.heap)

if __name__ == '__main__':
	h = Heap()
	h.heap_push(3)
	h.heap_push(10)
	h.heap_push(5)
	h.heap_push(9)
	h.heap_push(7)
	h.heap_push(21)
	h.heap_push(24)
	h.heap_push(2)
	h.heap_push(1)
	h.heap_push(11)
	h.heap_pop()
	print(h)
