class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to list of Anagram
        #defaultdict is imported from python's built in collections module
        #if access or appending a key that does not exsist yet
        #create that key and set its value to an empty list
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
            #dictionary keys must be immutable
            #tuple make it immutable
        return  list(res.values())

