def words(n):
    w = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    if 0 <= n < 20:
        return w[n]
    else:
        return "Number out of range"
w = int(input("Enter a number between 0 and 19: "))
for i in range(20):
    if i == w:
        print(words(i))