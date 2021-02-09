def Solution(s):
    i=0;j=1
    for _ in range(len(s)-1):
        if s[i] != s[j]:
            j += 1
        elif s[i]==s[j]:
            i=j
            j+=1
        else:


s = 'abcab'
Solution(s)