open_list = ["[","{","("] 
close_list = ["]","}",")"] 
  
def check(my_Str): 
    stack = [] 
    for i in my_Str: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "False"
    if len(stack) == 0: 
        return "True"
    else: 
        return "False"
  
  
string = "{[]{()}}"
print(string,"-", check(string)) 
  
string = "[{}{})(]"
print(string,"-", check(string)) 
  
string = "((()"
print(string,"-",check(string)) 
      
      
      