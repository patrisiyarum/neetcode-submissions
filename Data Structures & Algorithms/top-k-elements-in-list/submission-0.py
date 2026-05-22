import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # i can use a hashmap for this as well
        heap = []
        counts = {}
        for n in nums:
            counts[n] = counts.get(n,0) + 1
        for val, freq in counts.items():
            heapq.heappush(heap,(freq,val))
            if len(heap) > k:
                heapq.heappop(heap)
        return [val for freq,val in heap]