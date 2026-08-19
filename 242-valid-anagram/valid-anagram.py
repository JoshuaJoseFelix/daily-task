class Solution(object):
    def isAnagram(self, s, t):
        hashmap = defaultdict(int)

        for char in s:
            hashmap[char] += 1

        for char in t:
            hashmap[char] -=1

        for count in hashmap.values():
            if count !=0:
                return False
        return True  