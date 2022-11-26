#Time_Complexity: O(n)
#Space_Complexity: O(n)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #using the resultant array
        result=[-1] * len(nums)
        #a monotonic stack
        mstack=[]
        
        
        #iterate through the nums
        for i in range(2*len(nums)):
            #unitl the stack is empty
            while len(mstack)!=0 and nums[mstack[-1]]<nums[i%len(nums)]:
                #adding it to the resultant array
                result[mstack[-1]]=nums[i%len(nums)]
                #pop the index from the stack
                mstack.pop()
            #append the index to stack everytime u iterate 
            if i<len(nums):
                mstack.append(i)
                #return the result array
        return result
        
        
