from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            # sort characters to create a unique key
            key = "".join(sorted(word))
            anagram_map[key].append(word)
        
        return list(anagram_map.values())
