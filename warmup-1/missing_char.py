def missing_char(str, n):
  front = str[0:n]
  back = str[n+1:]
  return front+back


print(missing_char("hello",2))



# Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
# The value of n will be a valid index of a char in the original string 
# (i.e. n will be in the range 0..len(str)-1 inclusive).