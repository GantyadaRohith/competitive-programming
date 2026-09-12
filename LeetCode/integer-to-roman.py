class Solution:
    def intToRoman(self, num: int) -> str:
        dit = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        s=''
        x = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        i=0
        while num and i<=len(x):
            if num >= x[i] :
                s+=dit[x[i]]
                num -= x[i]
            else:
                i+=1
        return s
