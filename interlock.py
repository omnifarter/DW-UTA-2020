def interlock(word1,word2,word3):
    #check for edge cases
    if word1 == "" or word2 == ""or word3 == "":
        return False
    if len(word1)!= len(word2):
        return False
    if len(word3)!= len(word1)+len(word2):
        return False

    word1checker = True
    result=""
    for i in range(0,len(word1)):
        result += word1[i] + word2[i]
        
    print(result)
    if result==word3:
        return True
    
    else:
         return False

print("this is the output of test 1: " + str(interlock("shoe","cold","schooled")))
print("this is the output of test 2: " + str(interlock("shoes","cold","schooled")))
print("this is the output of test 3: " + str(interlock("","cold","schooled")))
print("this is the output of test 4: " + str(interlock("shoes","cold","")))
print("this is the output of test 5: " + str(interlock("","","")))
print("this is the output of test 6: " + str(interlock("can","his","chains")))

#extra test cases
print("this is the output of test 1: " + str(interlock("cold","shoe","schooled"))) #checks for starting word

