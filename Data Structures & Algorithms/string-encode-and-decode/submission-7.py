class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        res = []
        for i in range(len(strs)):
            if len(strs[i]) != 0:
                res.append(strs[i])
            else:
                res.append('≈')
        return 'Ω'.join(res)



    def decode(self, s: str) -> List[str]:
        if len(s) == 0: return []
        res = []

        for i in s.split('Ω'):
            if i == '≈': res.append("")
            else: res.append(i)

        return res