import json

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            sLength = len(s)
            encoded += f"{sLength}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        decoded = []
        i=0
        while i < len(s):
            length = ""
            while s[i].isnumeric():
                length += s[i]
                i+=1
            
            length = int(length)
            if s[i] == '#':
                decoded.append(s[i+1:i+1+length])
                i=i+1+length
            else:
                raise Exception("Unknow format")
        return decoded
            
            
            
            






