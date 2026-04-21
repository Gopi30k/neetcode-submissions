class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        print(buckets)
        topkF=[]
        # for index, num in enumerate(nums):
        #     count = nums.count(num)
        #     buckets[count].append(num)
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        print(counter)
        for num, count in counter.items():
            buckets[count].append(num)
        print(buckets)
        for i in range(len(buckets) -1 , 0 , -1):
            # print(buckets[i])
            # if len(buckets[i]) !=0 and k !=0:
            #     topkF.append(set(buckets[i]))
            #     k -= 1
            for num in buckets[i]:
                topkF.append(num)
                k -= 1
                if k == 0:
                    return topkF
