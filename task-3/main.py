# Check List Order
# Objective: Write a function `check` that takes a list and determines whether it is strictly increasing,
# strictly decreasing, or neither.
# Parameters:
# - list: A list of integers with a minimum length of 2.
# Returns:
# - A string: "increasing" if the list is strictly increasing, "decreasing" if the list is strictly decreasing, or "neither" otherwise.
# Notes:
# - A list is strictly increasing if each element is greater than the preceding one.
# - A list is strictly decreasing if each element is less than the preceding one.
# - If any two consecutive elements are equal, the list is considered "neither".

def check(list):
    if len(list) < 2:
        return "neither"
    
    is_increasing = True
    is_decreasing = True
    
    for i in range(1, len(list)):
        if list[i] > list[i - 1]:
            is_decreasing = False
        elif list[i] < list[i - 1]:
            is_increasing = False
        else:
            return "neither"
        
    if is_increasing:
        return "increasing"
    elif is_decreasing:
        return "decreasing"
    else:
        return "neither"

# Examples:
print(check([1, 2, 3]))  # Expected: "increasing"
print(check([3, 2, 1]))  # Expected: "decreasing"
print(check([1, 2, 1]))  # Expected: "neither"
print(check([1, 1, 2]))  # Expected: "neither"
