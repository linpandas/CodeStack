#
# @lc app=leetcode.cn id=347 lang=python3
# @lcpr version=30204
#
# [347] 前 K 个高频元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        hashmap = Counter(nums)
        result = []
        for num, freq in hashmap.items():
            heapq.heappush(result, (freq, num))
            if len(result) > k:
                heapq.heappop(result)
        
        return [x[1] for x in result]
# @lc code=end



#
# @lcpr case=start
# [1,1,1,2,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

