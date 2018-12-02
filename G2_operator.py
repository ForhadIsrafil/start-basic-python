# ======= Operators of python ============== # 

x = 5
y = 6

# now i show the different types of arithmetic operator and there operations
sum = x + y
min = x - y
mult = x * y
dev = x / y

print(sum)
print(min)
print(mult)
print(dev)

# when we need the reminder (vag sas) using modulous(%) operator
rmnd = y % x
print(rmnd)

# without float result / floor devision(//)
flrdvsn = 10//3
print(flrdvsn)

# power operator power (**) exponential
pwr = x**y
print(pwr)
# 2nd way of exponential(power)

k = 2
res = pow (k,3)
print(res)

a = 75 
a = -75
print(a)
print(abs(a))# here we can see that, negative value change into positive value

# print devision value and reminder both // in this case we use (divmod) function
s = 75
p = 10
r = divmod(s,p)
print(r)