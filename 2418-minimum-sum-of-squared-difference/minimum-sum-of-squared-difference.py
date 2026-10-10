class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        """d={}
        for i in range(len(nums1)):
            key=abs(nums1[i]-nums2[i])
            if key  in d:
                d[key]+=1
            else:
                d[key]=1
        print(d)"""
        """d = {}
        for a, b in zip(nums1, nums2):
            diff = abs(a - b)
            if diff > 0:
                d[diff] = d.get(diff, 0) + 1
        print(d)
        k=k1+k2"""
        """ans=0
        if k>0:
            item=sum(j for j in d.values())
            if item<k:
                return 0
            while(k>0):
                maxi=max(d)
                mimi=min(d)
                if(d[maxi]>1):
                    d[maxi]-=1
                    d[mimi]+=1
                elif(d[maxi]==1):
                    del d[maxi]
                    d[mimi]+=1
                k-=1
        ans=sum(i**2*j for i,j in d.items())
        return ans"""
        """k = k1 + k2
        totalsum = sum(val * freq for val, freq in d.items())
        if totalsum <= k:
            return 0
        max_heap = [(-val, freq) for val, freq in d.items()]
        heapq.heapify(max_heap)
        print(max_heap)
        while k > 0 and max_heap:
            neg_val, freq = heapq.heappop(max_heap)
            val = -neg_val
            can_reduce = min(k, freq)
            k -= can_reduce
            new_val = val - 1
            if new_val > 0:
                heapq.heappush(max_heap, (-new_val, can_reduce))
            if freq > can_reduce:
                heapq.heappush(max_heap, (-val, freq - can_reduce))
        ans = 0
        for neg_val, freq in max_heap:
            val = -neg_val
            ans += freq * (val ** 2)
            
        return ans"""
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        total_k = k1 + k2
        if sum(diffs) <= total_k:
            return 0
        left, right = 0, max(diffs)
        best = right
        while left <= right:
            mid = (left + right) // 2
            ops = sum(max(0, d - mid) for d in diffs)
            if ops <= total_k:
                best = mid
                right = mid - 1
            else:
                left = mid + 1  
        remaining_k = total_k
        new_diffs = []
        for d in diffs:
            if d > best:
                remaining_k -= (d - best)
                new_diffs.append(best)
            else:
                new_diffs.append(d)
        for i in range(len(new_diffs)):
            if remaining_k > 0 and new_diffs[i] == best:
                new_diffs[i] -= 1
                remaining_k -= 1
        return sum(d * d for d in new_diffs)