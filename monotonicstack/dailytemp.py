#TC:0(n)
#SC:0(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #creating a monotonoc stack
        mstack=[]
        #resultant array
        result=[0] * len(temperatures)
        
        #irtarate through the temperatures
        for i in range(len(temperatures)):
            #while stack is empth and lesser than the new temp
            while mstack and temperatures[mstack[-1]]<temperatures[i]:
                #nextwarmer day stores index
                nextwarmer=i-mstack[-1]
                #then adding it to the result array
                result[mstack[-1]] = nextwarmer
                #now pop it from the array
                mstack.pop()
                #at each stage append the index to stack
            mstack.append(i)
            #return teh resultant array
        return result