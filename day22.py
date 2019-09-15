#Python Dictionaries

numbers = {n:('even' if n%2==0 else 'odd') for n in range(1,20)}

print(numbers)

##########

print('------------')

##########

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linuse=99.5,
stan=150.0, lisa=50.25, harrison=10.0)
total_donations = sum(donations.values())
print(total_donations)