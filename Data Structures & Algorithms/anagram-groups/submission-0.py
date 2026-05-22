class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #i can use hashmaps here too
        groups = {}
        for string in strs:
            key = "".join(sorted(string)) # "aet"
            if key not in groups:
                groups[key] = [string]
            else:
                groups[key].append(string)
        return list(groups.values())