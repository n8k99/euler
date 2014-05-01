'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''

def square(x):
	x=x*x
	return x

a = 3
b = 4
a= square(a)
b=b*b
c=a+b
print c
print a+b+c
print a*b*c


