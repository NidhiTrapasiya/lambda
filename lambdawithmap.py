# Take a list of numbers.  
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ] 
  
# use anonymous function to filter and comparing  
# if divisible or not 
result = list(map(lambda x=1 : x>50, my_list))  
# printing the result 
print(result)  

