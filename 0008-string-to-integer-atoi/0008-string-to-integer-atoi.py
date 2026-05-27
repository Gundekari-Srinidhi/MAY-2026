class Solution:
    def myAtoi(self, s: str) -> int:
        temp=s.strip()
        sign=1
        i=0
        if len(temp)==0:
            return 0
        if temp[0]=='-':
            sign=-1
            i+=1
        if temp[0]=='+':
            i+=1
        num=0
        while i<len(temp) and temp[i].isdigit():
            num=num * 10 + int(temp[i])
            i+=1
        num=num*sign
        min1=-2**31
        max1=2**31-1
        if num<min1:
            return min1
        if num>max1:
            return max1
        return num

        