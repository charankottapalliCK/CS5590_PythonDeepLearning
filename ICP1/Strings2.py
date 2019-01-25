a = raw_input("Enter a sentence")

num_count = 0
char_count = 0
space_count = 0
for i in a:
    if(i.isdigit()):
        num_count=num_count+1
    elif(i.isalpha()):
        char_count=char_count+1
    elif(i.isspace()):
        space_count=space_count+1
print "Number of numbers " + str(num_count)
print "Number of charectors "+ str(char_count)
print "Number of spaces "+ str(space_count)

