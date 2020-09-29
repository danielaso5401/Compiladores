import re 
regex = '^[A-Za-z][A-Za-z0-9_]*'
def check(string):  
    if(re.search(regex, string)):  
        print("Valid Identifier")      
    else:  
        print("Invalid Identifier")  
      
if __name__ == '__main__' :  

    string =raw_input()
    check(string) 
  