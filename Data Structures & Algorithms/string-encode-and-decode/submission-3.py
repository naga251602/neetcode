class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        res = []
        for i in range(len(strs)):
            if len(strs[i]) == 0: res.append('≈')
            else: res.append(strs[i])
        print(res)
        return 'Ω'.join(res)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0: return []
        s = s.replace('≈', '')
        return s.split('Ω')
