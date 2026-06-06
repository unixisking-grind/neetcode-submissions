import json

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            sLength = len(s)
            encoded.append(f"{sLength}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        decoded = []
        i=0
        while i < len(s):
            length_str = ""
            while i < len(s) and s[i].isnumeric():
                length_str += s[i]
                i+=1
            
            length = int(length_str)
            if i < len(s) and s[i] == '#':
                i += 1
                decoded.append(s[i:i+length])
                i=i+length
            else:
                raise Exception("Unknow format")
        return decoded
