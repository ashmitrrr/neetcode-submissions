class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""
        
        for s in strs:
            result += str(len(s)) + "$" + s # will give us ex: "5$Hello5$World"
        return result 

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):

            j = i
            while s[j] != "$":
                j += 1

            l = int(s[i:j]) # will give us len of the coming word by convert to int
            w = s[j+1 : j + 1 + l] # for ex: j+1= H, j + 1 + l = 5, one before is o. 
            result.append(w)
            i = j+1+l
            
        return result 
