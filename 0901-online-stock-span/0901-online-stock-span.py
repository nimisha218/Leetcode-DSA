from collections import deque
from collections import defaultdict

class StockSpanner:

    def __init__(self):
        self.q = deque()
        self.d = defaultdict()
        self.counter = 0

    def next(self, price: int) -> int:
        
        if not self.q:
            self.q.appendleft(price)
            self.d[self.counter] = 1
            self.counter += 1
            return 1
        else:
            if price < self.q[0]:
                self.q.appendleft(price)
                self.d[self.counter] = 1
                self.counter += 1
                return 1
            else:
                res = 1
                count = 1
                while self.q and price >= self.q[0]:
                    res += self.d[self.counter - count]
                    count += self.d[self.counter - count]
                    self.q.popleft()
                self.d[self.counter] = res
                self.q.appendleft(price)
                self.counter += 1
                
                return res
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)