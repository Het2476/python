# A list contains some negative and some positive values. Write a recursive function that sanitizes the list by replacing all negative numbers with 0.

def sanitize_list(lst):
    if len(lst) == 0:
        return []
    return [lst[0] if lst[0] >= 0 else 0] + sanitize_list(lst[1:])


lst = [1, -2, 3, -4, 5]
print(sanitize_list(lst))
