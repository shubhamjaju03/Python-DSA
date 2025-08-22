keys = {"1":"","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

def return_all_words(input):
    if input == '':
        return ['']   # base case should return [''] for combination building
    
    small = input[1:]
    ans_for_small = return_all_words(small)
    key_letters = keys[input[0]]
    
    ans = []
    for char in key_letters:
        for word in ans_for_small:
            ans.append(char + word)
    
    return ans

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        return return_all_words(digits)
