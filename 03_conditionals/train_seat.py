# Build a train seat information system
# =====================================================================
"""
You're building a ticket info system for a railway app.
Based on seat type, show it's features.
Task:
    - Input: "sleeper", "AC", "general", "luxury"
    - Match using match-case
    - Unknown -> show: "Invalid seat type"
"""
# =====================================================================

seat_type = input("Enter seat type (sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("sleeper - No AC, beds available")
    case "ac":
        print("AC - Air conditioned, comfy ride")
    case "general":
        print("General - cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:
        print("Invalid seat type")