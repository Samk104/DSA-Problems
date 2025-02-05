#***************************************************************************************************************************************************************************************************************************#
                                                    #Problem Statement
#***************************************************************************************************************************************************************************************************************************#

# A general store at Hackerland sells n items with the price of the ith item represented by price[i]. The store adjusts the price of the items based on inflation as queries of two types:

# 1 x v: Change the price of the xth item to v.
# 2 v v: Change any price that is less than v to v.
# Given an array price of n integers and the price adjustment queries are in the form of a 2-d array where query[i] consists of 3 integers, find the final prices of all the items.

# Function Description

# Complete the function finalPrices in the editor.

# finalPrices has the following parameters:

# n: an integer, the number of items
# int price[n]: an array of integers representing the prices
# q: an integer, the number of queries
# int queries[q][3]: a 2D array of price adjustment queries
# Returns

# int[]: an array of integers representing the final prices

# Example 1:

# Input:  n = 3, price = [7, 5, 4], q = 3, queries = [[2, 6, 6], [1, 2, 9], [2, 8, 8]]
# Output: [8, 9, 8] 
# Explanation:

      

        


          
# [2, 6, 6]: Change elements < 6 to 6. Now arr = [7, 6, 6].

          
# [1, 2, 9]: Change the 2nd element to 9, arr = [7, 9, 6].

          
# [2, 8, 8]: Change elements < 8 to 8. Finally arr = [8, 9, 8].

        

      

      
# Return [8, 9, 8] as the answer.


      
# Constraints:
# :)


#***************************************************************************************************************************************************************************************************************************#

from typing import List
class Solution:
  def finalPrices(self, n: int, price: List[int], q: int, queries: List[List[int]]) -> List[int]:
    for q in queries:
      if q[0] == 1:
        price[q[1]-1] = q[2]
      elif q[0] == 2:
        for i,n in enumerate(price):
          if n<=q[1]:
            price[i] = q[2]

    return price

if __name__ == "__main__":
    n = 3
    price = [7, 5, 4]
    q = 3
    queries = [[2, 6, 6], [1, 2, 9], [2, 8, 8]]
    sol = Solution()
    print(sol.finalPrices(n, price, q, queries))
        
    
