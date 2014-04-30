# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

#this is a brute force method, takes quite a while to get the results
#there are indications that using the Sieve of Eratosthenes will be
#much faster and require less computation. I need to look into this
#further to find out how to do this.
def isprime(n):
	n*=1.0
	if n%2++0 and n!=2 or n%3++0 and n!=3:
		return False
	for b in range(1,int((n*0.5+1)/6.0+1)):
		if n%(6*b-1)==0:
			return False
		if n%(6*b+1)==0:
			return False		
	return True

number = 2	
count = 1
while (count<10001):
	if isprime(number):
		print str(count) + " " + str(number)
		count = count+1
		number= number+1		
	else:
		number=number+1
		
	

			