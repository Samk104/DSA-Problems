#***************************************************************************************************************************************************************************************************************************#
                                                    #Problem Statement
#***************************************************************************************************************************************************************************************************************************#

# You are in the Amazon's Cloud Infrastructure Team, and you are working on a project to optimize how data flows through its network of storage servers.

# You are given with n storage servers, and the throughput capacity of each server is given in an integer array named throughput.

# There are pipelineCount data pipelines that need to be connected to two storage servers, one as the primary connection and the other as the backup. Each data pipeline must choose a unique pair of servers for its connections.

# The transferRate for each data pipeline is defined as the sum of the throughput of its primary and backup servers.

# Given an integer array throughput and an integer pipelineCount, find the maximum total transferRate that can be obtained by optimally choosing unique pairs of connections for each data pipeline.

# Note:

# A pair of servers (x, y) is said to be unique if no other pipeline has selected the same pair. However, the pairs (y, x) and (x, y) are treated as different connections.
# It is also possible to select the same server for primary and backup connections, which means that (x, x) is a valid pair for the connection.
# Function Description

# Complete the function maxTransferRate in the editor.

# maxTransferRate has the following parameters:

# 1. int throughput[n]: array of throughput provided by each server instance.
# 2. int pipelineCount: the number of data pipelines that need to be connected.
# Returns

# long: the maximum total transfer rate.

# Example 1:

# Input:  throughput = [4, 2, 5], pipelineCount = 4
# Output: 36 
# Explanation:

# The data pipelines can select their connection among the following 9 possible server pairs:

# [1, 1], [1, 2], [1, 3], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]
# (Assuming 1-based indexing of throughput array).

# However, each data pipeline must select a unique pair of servers.

# To achieve the maximum total transferRate, the data pipelines can optimally choose the pairs [3, 3], [1, 3], [3, 1], [1, 1] to obtain the maximum sum of transferRate = (5 + 5) + (5 + 4) + (4 + 5) + (4 + 4) = 36.

#***************************************************************************************************************************************************************************************************************************#



from typing import List

class Solution:
  def maxTransferRate(self, throughput: List[int], pipelineCount: int) -> int:
    tLen = len(throughput)
    throughput.sort()

    res = 0
    pair = set()
    pCount = 0

    for i in range(tLen - 1, 0, -1):
      if pCount == pipelineCount:
        return res
      
      if pCount < pipelineCount:
        pair.add((i, i))
        res += 2 * throughput[i] 
        pCount += 1

      if pCount < pipelineCount and (i, i-1) not in pair:
        pair.add((i, i-1))
        res += throughput[i] + throughput[i-1]
        pCount += 1

      if pCount < pipelineCount and (i-1, i) not in pair:
        pair.add((i-1, i))
        res += throughput[i-1] + throughput[i]
        pCount += 1

    return res

if __name__ == "__main__":
  throughput = [4, 2, 5]
  pipelineCount = 4
  sol = Solution()
  output = sol.maxTransferRate(throughput, pipelineCount)
  print(output) 
