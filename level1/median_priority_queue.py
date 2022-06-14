import heapq

class MedianPriorityQueue():
	
	def __init__(self):
		self.min_q = list()
		self.max_q = list()

	def rearrange(self, lr):
		if lr:
			heapq.heappush(self.min_q, (-1) * heapq.heappop(self.max_q))
		else:
			heapq.heappush(self.max_q, (-1) * heapq.heappop(self.min_q))

	def add(self, ele):
		if len(self.min_q) and ele > self.min_q[0]:
			heapq.heappush(self.min_q, ele)
		else:
			heapq.heappush(self.max_q, ele * (-1))
		if abs(len(self.max_q) - len(self.min_q)) >= 2:
			self.rearrange(len(self.max_q) > len(self.min_q))

	def peek(self):
		if len(self.min_q) > len(self.max_q):
			return self.min_q[0]
		else:
			return (-1) * self.max_q[0]

	def remove(self):
		if len(self.min_q) > len(self.max_q):
			return heapq.heappop(self.min_q)
		else:
			return heapq.heappop(self.max_q)

	def printq(self):
		print([ (-1) * k for k in self.max_q], self.min_q)

if __name__ == '__main__':
	m = MedianPriorityQueue()
	m.add(2)
	m.add(10)
	m.add(30)
	m.add(-2)
	m.add(-4)
	m.add(-6)
	m.printq()
	print(m.peek())