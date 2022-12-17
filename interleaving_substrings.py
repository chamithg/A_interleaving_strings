class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        temp = s1+s2
        temp_arr =[]
        
        temp_arr_2 = []
        for each in temp:
            temp_arr.append(each)
            
        for each in s3:
            temp_arr_2.append(each)
            
        return ("".join(sorted(temp_arr)) =="".join(sorted(temp_arr_2)))    
            
        
        


s1 ="aabcc"
s2 ="dbbca"
s3 ="aadbbcbcc"

obj = Solution()

print(obj.isInterleave(s1,s2,s3))