import heapq

class MedianFinder:

    def __init__(self):
        # Two heaps
        # small = max-heap (left half) — remember Python negates for max-heap
        # large = min-heap (right half)
        self.small = []  # max-heap
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        # Step 1: Push to correct heap
        # If small is empty OR num <= top of small → push to small
        # Remember: small is a max-heap, so negate on push
        # Otherwise → push to large
        if len(self.small) == 0 or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        # Step 2: Rebalance
        # If small has 2 more than large →
        #     pop from small, push to large
        # If large has 2 more than small →
        #     pop from large, push to small
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If sizes equal → average of both tops
        # If small larger → small top is median
        # If large larger → large top is median
        # Remember: small top is negated — undo it
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]