def string_splosion(str):
  
  result = ""
  
  for i in range(len(str)):
    result = result + str[:i+1]
  return result

print(string_splosion("python"))


# Given a non-empty string like "Code" return a string like "CCoCodCode".