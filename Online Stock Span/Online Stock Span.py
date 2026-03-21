class StockSpanner:

    def __init__(self):
        self.past = list()

    def next(self, price: int) -> int:
        out = 1

        while self.past and self.past[-1][0] <= price:
            out += self.past[-1][1]
            self.past.pop()

        self.past.append((price,out))

        return out


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)