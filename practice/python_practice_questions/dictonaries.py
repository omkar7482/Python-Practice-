a = {
    "PNR112": {
        "coach_type": "3AC",
        "ticket_rate": 900,
        "passengers": [("Rahul", "UB"), ("Baskar", None)]
    },
    "PNR123": {
        "coach_type": "2AC",
        "ticket_rate": 1500,
        "passengers": [("Amit", "LB"), ("Ravi", "UB")]
    },
    "PNR456": {
        "coach_type": "3AC",
        "ticket_rate": 800,
        "passengers": [("Priya", "MB"), ("Neha", None)]
    },
    "PNR789": {
        "coach_type": "SL",
        "ticket_rate": 500,
        "passengers": [("Vikram", "UB"), ("Kiran", "MB"), ("Surya", "SU")]
    },
}
returning_dict = {}
for i in a : 
    inside_pnr = a[i]
    amount = inside_pnr["ticket_rate"]
    no_of_passenger = len(inside_pnr["passengers"])
    total_amount = amount*no_of_passenger
    returning_dict[i] = total_amount

        
#print(returning_dict)

value = list(returning_dict.values())
total_amount = 0    
for i in value:
    total_amount += i
print(total_amount)




