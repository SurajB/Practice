
#This is Pig Latin translator

def translate(eng):
    if type(eng)==str:
        l=len(eng)
        '''temp=eng[l-1]
        eng[l-1]=eng[0]
        eng[0]=temp'''
        pig_lat=eng[l-1] + eng[1:l-1] + eng[0] + "ay"
        return(pig_lat)
    
print "This is Pig Latin translator"
eng=raw_input("Enter the English word: ")
pig_lat=translate(eng)    
print "The Pig Latin word is " + pig_lat