from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomDict = Counter(ransomNote)
        magDict = Counter(magazine)
        for key in ransomDict:
            if key not in magDict:
                return False
            if ransomDict[key] > magDict[key]:
                return False
        return True