

berth_types = ["UB","MB","LB", "SU","SL", None]


def analyze_bookings(bookings, task):
    """
    Analyze the railway ticket bookings based on the given task.
    
    Args:
        bookings (dict): Dictionary with PNR as key and booking details as value.
        task (str): The analysis task to perform.
    
    Returns:
        dict: The result of the requested task.
    """
    if task == "ticket_prices":
        for i in bookings:
            return i 
                                                                                                                                
    











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


analyze_bookings(a, "ticket_prices")
