def close_far(a, b, c):
  if abs(a-b)<=1 and (abs(b-c)>=2 and abs(a-c)>=2):
    return True
    
  if abs(a-c)<=1 and (abs(b-c)>=2 and abs(a-b)>=2):
    return True
  
  else:
    return False


print(close_far(1, 2, 10) )
print(close_far(1, 2, 3) )
print(close_far(4, 1, 3) )