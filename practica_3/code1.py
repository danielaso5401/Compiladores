
#test_string = raw_input()
test_string = "25"   
print("la cadena ingesada es: " + str(test_string)) 
  
res = test_string.replace('.', '', 1).isdigit() 
  
print("esta cadena es un float: " + str(res)) 