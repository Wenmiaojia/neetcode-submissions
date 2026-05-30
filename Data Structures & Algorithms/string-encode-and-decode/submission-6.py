from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Fixed: Changed strs(len(s)) to str(len(s))
            res += str(len(s)) + "#" + s
        return res
 
    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        # Loop through the entire encoded string
        while i < len(s):
            j = i
            # Find the delimiter '#' for the current token
            while s[j] != "#":
                j += 1
            
            # Extract the length of the string
            length = int(s[i:j])
            
            # Extract the actual string using the length
            res.append(s[j + 1 : j + 1 + length])
            
            # Move the pointer 'i' to the start of the next encoded block
            i = j + 1 + length
            
        return res