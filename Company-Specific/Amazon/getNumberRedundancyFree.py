#***************************************************************************************************************************************************************************************************************************#
                                                    #Problem Statement
#***************************************************************************************************************************************************************************************************************************#

# Your team at AMZ is developing a new algorithm for suggesting passwords when a user sets up a NEW account :)

# A string of lowercase English characters is said to be redundancy-free if each character occurs at most once in the string. In order to ensure minimum redundancy, the developers suggest a password that has the minimum number of redundancy-free segments it can be divided into.

# Given a string, password, find the minimum number of redundancy-free segments we can divide it into.

# Function Description

# Complete the function getNumberRedundancyFree in the editor.

# getNumberRedundancyFree has the following parameter:

# string password: the given password
# Returns

# int: the number of segments we can divide the string into

# Example 1:

# Input:  password = "aabcdea"
# Output: 3 
# Explanation:
# https://www.fastprep.io/_next/static/media/getNumberRedundancyFree.36cfbc8b.png




# The password can be partitioned into a minimum of 3 valid segments. Return 3.

# Example 2:

# Input:  password = "alabama"
# Output: 4 
# Explanation:


# The minimum partitions are "al", "ab", "a", "ma".

# Example 3:

# Input:  password = "zebra"
# Output: 1 
# Explanation:

# Constraints:
# 1 ≤ length of password ≤ 10^5
# All characters in password are lowercase English letters.

#***************************************************************************************************************************************************************************************************************************#

class Solution:
  def getNumberRedundancyFree(self, password: str) -> int:
    dup = set()
    res = 1

    for s in password:
      if s in dup:
        res += 1
        dup.clear()
      dup.add(s)

    return res
        

if __name__ == "__main__":
    password = "alabama"
    sol = Solution()
    output = sol.getNumberRedundancyFree(password)
    print(output) 
