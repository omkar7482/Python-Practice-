new_word = word  # don’t remove this line

if new_word[-3:] == "ing":
    new_word = new_word[:-3]

if continuous_tense:
    new_word=new_word+"ing"
    
if age < 18 :
    age_group = "Child"
else:
    age_group = "Adult"    
    
if is_member:
    application_type = age_group +" "+ "Menmber"
else : 
    application_type = age_group+" "+"Non-member"

if color_code == "R":
    color = "red"
elif color_code == "G":
    color = "green"
elif color_code == "B":
    color = "blue"
else :
    color = "black"
    
is_time_valid = 0<int(time[:2])<=12

time_in_hrs = int(time[:2])%2 + (time[-2:]== "PM") * 12

if not is_time_valid:
    time_of_day = "Invalid"
elif 0 <= time_in_hrs<6 :
    time_of_day = "Night"
elif 6 <= time_in_hrs <12 :
    time_of_day = "Morning"
elif 12<= time_in_hrs <18 :
    time_of_day = "Afternoon"
elif 18<= time_in_hrs <24:
    time_of_day = "Evening"
    