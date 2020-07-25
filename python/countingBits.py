'''
Question: 

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]


Follow up:
1) It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
3) Space complexity should be O(n).
'''

def countBitsDynmaic(self, num: int) -> List[int]:
        po = 0
        dp=[0]
        for i in range(1,num+1):
            if i&(i-1)==0:
                dp.append(1)
                po+=1
            else:
                dp.append(dp[i-(1<<po)]+1)
        return(dp)
                
def countBitsBruteForce(self, num: int) -> List[int]:
    def count1(num):
      count = 0
      if num == 1 or num==2:
         return 1
      if num ==0:
        return 0
      while num!=0:
        num = num&num-1
        count+=1
        return count
        
   ret = []
   for i in range(num+1):
    ret.append(count1(i))
   return ret
          
  


                
        
