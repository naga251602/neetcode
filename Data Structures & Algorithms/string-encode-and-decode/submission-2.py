class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        res = []

        for i in strs:
            if len(i) == 0: res.append('ç')
            else: res.append(i)

        return 'Ω'.join(res)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0: return []
        return s.strip('ç').split('Ω')
