"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = set()
        for i in range(n):
            if i == 0:
                s.add("()")
            else:
                new_set = set()
                for element in s:
                    parentheses = []
                    for i in range(len(element) + 1):
                        new_str = element[:i] + "()" + element[i:]
                        parentheses.append(new_str)
                    new_set.update(parentheses)
                s = new_set 
        return list(s) 

n = 2
solution = Solution()
print(solution.generateParenthesis(n))

