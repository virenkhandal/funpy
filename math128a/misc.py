coeffs = [1, 22, 7, 42, 33, 4, 40]
total = 0
stringy = ""

for i in range(0, 7):
    curr_str = str(coeffs[i]) + "(1/60)^" + str(i) + "+ "
    stringy += curr_str
    curr_exp = ((1/60) ** i)
    curr = curr_exp * coeffs[i]
    total += curr

print(stringy)
print(total)