f = open("The_Ashes_of_Tomorrow_Part1.txt","r")
c = ",. !@#$%^&*(_-=+)~\\/?><\"[]1234567890:;——\n"
d = []




a = f.read()



for char in a :
    if char not in c:
        d.append(char) 





joint_without_any_special_char = "".join(d)
lower_joint_without_any_special_char = joint_without_any_special_char.lower()

g = open("story_without_any_special_char.txt","w")
g.write(lower_joint_without_any_special_char)
f.close()
g.close()

        
