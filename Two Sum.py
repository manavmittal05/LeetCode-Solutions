def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = [[], 0]
            
        for i in range(0 ,len(nums)):
            d[nums[i]][0].append(i)
            d[nums[i]][1] += 1
        
        for i in d.keys():
            d[i][1] -= 1
            temp = d[i][0].pop(0)
            if target-i in d.keys() and d[target-i][1] != 0:
                return [temp, d[target-i][0][0]]
