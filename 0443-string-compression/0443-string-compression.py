class Solution:
    def compress(self, chars: List[str]) -> int:
        s=""
        count=1
        for i in range(1,len(chars)):
            if chars[i]==chars[i-1]:
                count+=1
            else:
                if count>1:
                    s+=chars[i-1]+str(count)
                else:
                    s+=chars[i-1]
                count=1
        if count>1:
            s+=chars[-1]+str(count)
        else:
            s+=chars[-1]
        chars[:len(s)]=list(s)
        return len(s)
