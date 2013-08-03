def minCuts(s):
  leng = len(s)
  isPal = [[False for i in range(leng)] for j in range(leng)]
  dp = [leng - 1 - i for i in range(leng + 1)]
  for i in range(leng - 2, -1, -1):
    for j in range(i, leng):
      if (s[i] == s[j] and (j <= i + 2 or isPal[i + 1][j - 1])):
        isPal[i][j] = True
        dp[i] = min(dp[i], dp[j + 1] + 1)
  return dp[0]

s = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
print s, minCuts(s)