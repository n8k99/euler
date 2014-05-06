'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''

def find_a(m,n): return n*n - m*m
def find_b(m,n): return 2*n*m
def find_c(m,n): return n*n + m*m
def find_sum(m,n): return sum_threes(find_a(m,n),find_b(m,n),find_c(m,n))
def find_product(m,n): return find_a(m,n)*find_b(m,n)*find_c(m,n)


for i in range(1,55):
	n = i
	m = (500/n)-n
	if find_sum(m,n) == 1000:
		if find_product(m,n) >0:
		 print m, n, find_product(m,n)

print find_a(5,20), find_b(5,20), find_c(5,20)	#gives the sides of the triangle		