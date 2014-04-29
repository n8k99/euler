prime = 1
number = 2

def isprime(startnumber):
	startnumber*=1.0
	for divisor in range(2,int(startnumber**0.5)+1):
		if startnumber/divisor==int(startnumber/divisor):
			return False
	return True

while prime < 10001:
	is_it = isprime(number)
	if is_it == True:
		number+1
		prime+1
	else:
		number+1		

print number
	
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
			