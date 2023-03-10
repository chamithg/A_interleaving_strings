class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1)+ len(s2) != len(s3):
            return False
        r1 = 0
        r2 = 0
        r3 =0
        duplicates =""
        d = 0
        
        while r3 < len(s3):
            if r1 < len(s1) and s1[r1] == s3[r3] and r2 < len(s2) and s2[r2] == s3[r3]:
                duplicates += s1[r1]
                r1+=1
                r2+=1
            elif r1 < len(s1) and s1[r1] == s3[r3]:
                r1+=1
            elif r2 < len(s2) and s2[r2] == s3[r3]:
                r2 +=1
            elif d < len(duplicates) and duplicates[d] == s3[r3]:
                d+=1
            else:
                return False
            r3+=1
            
        return True

s1 ="dbbca"
s2 ="aabcc"
s3 ="aadbbcbcaa"

obj = Solution()

print(obj.isInterleave(s1,s2,s3))