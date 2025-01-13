
print ("This program applies a shift cypher on any phrase!")

print ()


#start a loop that goes through each character in a string, 
#does the shift one at a time and adds it to the answer string

phrase_to_encrypt = input("Enter a phrase to encrypt: ")
shift = int(input("Enter a positive number for the shift: "))
answer = ""


#change to ascii reference number
for x in phrase_to_encrypt:
    converted_piece = ord(x)

#If it's not a letter, leave it alone    
    if converted_piece < 65 or converted_piece > 122 or (converted_piece > 90 and converted_piece < 97):
        answer = answer + chr(converted_piece)
        
        
#If it's an upper case or lower case letter, do the shift    
    else:
        do_the_shift = converted_piece + shift
                
        
#shifts upper case letters not at the end of the alphabet
        if do_the_shift <= 90 and do_the_shift >=65:
            answer = answer + chr(do_the_shift)
            



#shifts lower case letters not at the end of the alphabet
        elif do_the_shift <= 122 and do_the_shift >= 97:
            answer = answer + chr(do_the_shift)
            


#shifts lower case letters at the end of the alphabet
        elif do_the_shift > 122:
            new_location = do_the_shift % 123 + 97
            answer = answer + chr(new_location)
            

#shifts upper case letters at the end of the alphabet
        elif do_the_shift > 90 and do_the_shift < 97:
            new_location = do_the_shift % 91 + 65
            answer = answer + chr(new_location)

#blank space because I hate it when things are crammed
print ()

#print the answer!
print ("Your encoded phrase is: " + answer)
     





