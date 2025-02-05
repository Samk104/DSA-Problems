#***************************************************************************************************************************************************************************************************************************#
                                                    #Problem Statement
#***************************************************************************************************************************************************************************************************************************#

# Amazon shoppers often refer to user reviews to help them decide whether to purchase an item. They can focus their efforts using a keyword search, but typographical errors are common in reviews. To help mitigate this problem, Amazon's algorithm will include reviews that contain a word that is similar to the search term. A string, s, is similar to another string, t, if it is possible to swap two adjacent characters at most once in s to turn it into t. Given a keyword string named keyword, find how many substrings of review are similar to keyword.

# Note: A substring is a contiguous sequence of characters within a string. Two substrings are considered distinct if they begin at different positions.

# Example 1:

# Input:  key = "moon", text = "monomon"
# Output: 2 
# Explanation:


# Consider the first four characters in text, i.e "mono". Swap the last two characters to match the keyword "moon".
# The last four characters in the text are "onom". Swap the first two characters to match the keyword.
# Thus, there are 2 substrings of "monom" that are similar to "moon". Note, that no other substring is similar to the given key.
  
      
# Example 2:

# Input:  key = "aaa", text = "aaaa"
# Output: 2 
# Explanation:


# There are 2 substrings of "aaaa" that are similar to "aaa" are:

# aaaa

# aaaa
 
      
# Constraints:
# key and text will consist solely of lowercase English letters.
# 1 ≤ |key| ≤ |text| ≤ 50, where |s| denotes the length of a string s.
#***************************************************************************************************************************************************************************************************************************#


class Solution:
    def similarTextSubstringCount(self, key: str, text: str) -> int:
        res = 0
        key_len = len(key)
        
        for l in range(len(text) - key_len + 1):
            word = text[l:l+key_len]

            if key == word:
                res += 1
                continue

            # Swap
            word_list = list(word)
            for i in range(key_len - 1):
                word_list[i], word_list[i+1] = word_list[i+1], word_list[i]
                if ''.join(word_list) == key:
                    res += 1
                    break
                word_list[i], word_list[i+1] = word_list[i+1], word_list[i]

        return res

if __name__ == "__main__":
    key = "moon"
    text = "monomon"
    sol = Solution()
    print(sol.similarTextSubstringCount(key, text))
    print(sol.similarTextSubstringCount("aaa", "aaaaa"))
