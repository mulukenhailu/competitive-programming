class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
         #  ["900 google.mail.com", 
         # lst=[900, google.mail.com]
         # lst2=[google, mail,com]
         # "google.mail.com":900
         # "mail":900
         # "com":900
         # "50 yahoo.com", 
         # lst1=[50,yahoo.com]
         # "yahoo.com":50
         # ".com":901
         # "1 intel.mail.com", 
         # "5 wiki.org"]
        dic={}
        ans=[]
        for cp in cpdomains:
            
            lst1=cp.split(" ")
            dic[lst1[1]]=dic.get(lst1[1], 0)+int(lst1[0])
            
            lst2=lst1[1].split(".")
            # print(lst2)
            if len(lst2)==3:
                lst3=[lst2[1]+"."+lst2[2], lst2[2]]
            else:
                lst3=[lst2[1]]
            # print(lst3)
            
            for l in lst3:
                dic[l]=dic.get(l, 0)+int(lst1[0])
            
        print(dic)
        
        for k, v in dic.items():
            ans.append(str(v)+" "+k)
            
        return ans
                

        