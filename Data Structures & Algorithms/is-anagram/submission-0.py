class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #for this i can also use a hashmap to see if the counts of the letters match
        lettersInS = {}
        lettersInT = {}
        count = 0
        count2 = 0

        for let in s:
            if let in lettersInS:
                lettersInS[let] = lettersInS[let] + 1
            else:
                lettersInS[let] = 1
            
        
        for let in t:
            if let in lettersInT:
                lettersInT[let] = lettersInT[let] + 1
            else:
                lettersInT[let] = 1
            

        return lettersInS == lettersInT
        