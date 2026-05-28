class Solution:
    def generate(self,s,ind,ans,op,close,n):
        if(op>n):
            return
        if (op+close==2*n and op==close):
            ans.append(s)
            return
        self.generate(s+'(',ind+1,ans,op+1,close,n)
        if op>close:
            self.generate(s+')',ind+1,ans,op,close+1,n)
        return ans
    def generateParenthesis(self, n: int) -> List[str]:
        ind=0
        ans=[]
        op=close=0
        return self.generate("",ind,ans,op,close,n)
 