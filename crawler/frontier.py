from collections import deque

class Frontier:
    def __init__(self):
        self.queue = deque()
        self.visited = set()

    def add(self, url):
        if url not in self.visited:
            self.queue.append(url)
            self.visited.add(url)

    def next(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def done(self):
        return len(self.queue) == 0
    
    def __len__(self):
        return len(self.queue)