import sys
import random

josh_index = int(sys.argv[1])

# This method replaces a word with Josh if the 
# generated random number (1-10) is less than the
# passed-in Josh index. JI of 3 -> 30% Josh
def replace_with_josh(split_text):
    cool_split_text = split_text
    for i in range(len(split_text)):
        if random.randint(1, 10) <= josh_index:
            if "\n" in cool_split_text[i]:
                cool_split_text[i] = "\nJosh"
            else:
                cool_split_text[i] = "Josh"
    return cool_split_text


# This method replaces a word with Josh if the 
# generated random number (1-100) has the passed-in
# Josh index in it.
def replace_with_josh_other_method(split_text):
    num_words = len(split_text)
    num_changed_words = 0
    cool_split_text = split_text
    for i in range(len(split_text)):
        randy = random.randint(1, 100)
        if randy % 10 == josh_index or randy/10 == josh_index:
            cool_split_text[i] = "Josh"
            num_changed_words +=1
    print(str(num_changed_words)+"/"+str(num_words)+" = "+str(num_changed_words/num_words) + " Josh replacement rate")
    return cool_split_text

lame_file = open("LameText.txt", "r")
text = lame_file.read()
lame_file.close()
split_text = text.replace("\n"," \n").split(" ")
cool_split_text = replace_with_josh(split_text)
text = " ".join(cool_split_text)

print(text)

cool_file = open("CoolText.txt","w")
cool_file.write(text)
cool_file.close()

# optional additional functionality. See replace_with_josh_other_method()

#cool_split_text = replace_with_josh_other_method(split_text)
#text = " ".join(cool_split_text)

#sabrina_file = open("OtherCoolText.txt","w")
#sabrina_file.write(text)
#sabrina_file.close()

