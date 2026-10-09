# main_dish = input()
# time_of_day = int(input())
# has_voucher = bool(input())
# is_card_payment = bool(input())

# if main_dish == "paneer tikka":
#     cost = 250
# elif main_dish == "butter chicken":
#     cost = 240
# elif main_dish == "masala dosa":
#     cost = 200
# else: # if main dish is invalid print invalid dish and exit the code.
#     print("Invalid main dish")

# if time_of_day >= 12 and time_of_day <= 15:
#     total_cost = (1 - 0.15) * cost
# else:
#     total_cost = cost

# if has_voucher == True:
#     total_cost = total_cost *(1-0.10)# Apply voucher discount
# else:
#     total_cost = cost    

# if is_card_payment == True:  # service charge for card payments
#     service_charge = 0.05 * total_cost
#     total_cost = total_cost + service_charge
# else:
#     total_cost = total_cost

#print(f"{total_cost:.02f}")

age = 55#int(input("Enter your age : ")) 
height = 5#int(input("Enter your height : ")) 
weight =5 #int(input("Enter your weight : ")) 
print (f"So, you're {age} old, {height} tall and {weight} heavy.")
   



print("So, you're" ,age," year old, " , height, " cm tall and " , weight , " heavy ") 
print("So, you're " + str(age) + " year old, " + str(height)+ "cm tall and" + str(weight) + "heavy ") 
