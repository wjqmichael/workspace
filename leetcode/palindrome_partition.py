def partition(string):
  if len(string) == 0:
    return [[]]
  result = []
  for i in range(1, len(string) + 1):
    prefix = string[:i]
    if isPalindrome(prefix):
      right = partition(string[i:])
      for lst in right:
        lst.insert(0, prefix)
        result.append(lst)
  return result      
    
def isPalindrome(string):
  left = 0
  right = len(string) - 1
  while right > left: 
    if (string[left] != string[right]):
      return False
    left += 1
    right -= 1
  return True

print partition("abbab")