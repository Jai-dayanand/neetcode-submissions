
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l1 = dict()

        for i in strs:
            key = tuple(sorted(i))

            if key in l1:
                l1[key].append(i)
            else:
                l1[key] = [i]

        return list(l1.values())
