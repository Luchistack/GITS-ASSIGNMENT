#declare a float point table: a ,b, pow(a, b)
#under a add 1, 2, 3, 4, 5, or =
#under b add 2, 3, 4, 5,6
#under pow add 1, 8, 81, 1024, 15625
#display all in a table format


# add values to variable, a and b
a = (1, 2, 3, 4, 5)
b = (2, 3, 4, 5, 6)

#print the top of the table with the names, header
print(f"{'a' :<5}  {'b':<5}  {'pow(a/b)':<10}")
print("....................")


#calculate a raised to the power of b
   

table = []
#loop a and b together, side by side
for a, b in zip(a, b):
    table.append ([a, b, a**b])

#print each row in its columns

print(f"{a :<5}  {b:<5}  {a**b:<10}")

print(tabulation(table, headers, tablefmt="grid"))

