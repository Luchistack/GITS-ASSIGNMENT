#PSEUDOCODE
#calculate the total investment of a user which is 7% of %1000
#of what the user invested
#then see how much return the user gets after ten years, 20 years and 30 years of
#investing.

#a = p(1+r)n

p = 1000
r = 0.07
#n = 10 or 20 or 30
#a= expected return

ten = p * (1 + r) ** 10

print("Ten years years investment return = ", ten)

twenty = p * (1 + r) ** 20

print("Twenty  years investment return = ", twenty)

thirty = p * (1 + r) ** 30

print("Thirty years investment return = ", thirty)


