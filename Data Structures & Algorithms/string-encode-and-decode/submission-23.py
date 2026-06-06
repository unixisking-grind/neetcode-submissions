# https://neetcode.io/problems/string-encode-and-decode

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            tmp = ""
            for ch in s:
                tmp += ch
            result += chr(0) + tmp
        return result + chr(0)

    def decode(self, s: str) -> List[str]:
        if s == 2*chr(0):
            return [""]
        result = []
        tmp = ""
        for i, ch in enumerate(s):
            if ch == chr(0):
                if tmp != "":
                    result.append(tmp)
                elif i == 1:
                    result.append("")
                tmp = ""
                continue
            tmp += ch
        return result