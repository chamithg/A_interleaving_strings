class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        
        # this recursive function completely works but not efficient in time complexity, this can be solved by memoization.
        
        if len(s1)+ len(s2) != len(s3):
            return False
        
        l1,l2,l3 = len(s1),len(s2),len(s3)
        
        # memoization part
        # here create a dictionary to hold the already found values
        already_found ={}

        def find(p1,p2,p3):
            
            
            if p1 ==l1 and p2 ==l2 and p3 == l3:
                return True
            
            ## each function call create a unique key with the parameter values.
            key = str(p1) +str(p2)+ str(p3)
            
            # if the key is already in the dictionary , return the value without going any further.
            if key in already_found:
                return already_found[key]
            
            path1,path2 = False,False
            
            if p1<l1 and p3< l3 and s1[p1] == s3[p3]:
                path1 = find(p1+1,p2,p3+1)
            if p2<l2 and p3<l3 and s2[p2] ==s3[p3]:
                path2 = find(p1,p2+1,p3+1)
            
            ## before return any value add the result to the already found dict with unique key.
            already_found[key] = path1 or path2
            return path1 or path2
        
        return find(0,0,0)


s1 ="dbbca"
s2 ="aabcc"
s3 ="aadbbcbcaa"

obj = Solution()

print(obj.isInterleave(s1,s2,s3))