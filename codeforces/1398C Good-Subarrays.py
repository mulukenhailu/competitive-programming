t = int(input())
for _ in range(t):
    n = int(input())
    lst = input()

    # cursum=j-i+1
    # i=cursum-j-1
    # i(target)= cursum-j-1
    # or 
    # j=cursum+i-1
        
    dic = {0 : 1}
    cur = 0
    ans = 0
    for j in range(n):
        cur+=int(lst[j])
        ans += dic.get((cur - j - 1), 0)
        dic[cur - (j + 1)] = dic.get((cur - j - 1), 0) + 1

    print(ans)
        