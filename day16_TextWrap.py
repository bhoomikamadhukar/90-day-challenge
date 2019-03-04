import textwrap 
  
value = input("enter text")
   
wrapper = textwrap.TextWrapper(width=4) 
  
string = wrapper.fill(text=value) 
  
print (string) 