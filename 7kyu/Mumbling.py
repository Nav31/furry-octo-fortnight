def accum(s):
    # your code
    s = s.lower()
    ans = ""
    i = 0
    for x in range(len(s)): 
      while i < x+1:
        if(i == 0):
          ans += s[x].upper()
          i += 1
        else:
          ans += s[x]
          i += 1
      ans += "-"
      i = 0
    return ans[0:-1]