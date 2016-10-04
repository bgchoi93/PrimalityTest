import math
import datetime
import random

# O(n^(3/4))
# n = maximum number we can take by assumption
# this list should be kept for later uses. 
def getListOfPrimes(n):
	sqrtn = int(math.sqrt(n))
	primes = [2,3]
	for i in range(5, sqrtn, 2):
		isItPrime = True
		for prime in primes:
			if (prime <= math.sqrt(i)):
				if(i % prime == 0):
					isItPrime = False
					break
			else: 
					break
		if isItPrime == True:
			primes.append(i)
	return primes

# O(k) where k = number of prime numbers < sqrt(n), k << sqrt(n) < n
# x = the number we want to test
# primes = the list of prime numbers we obtained from getListOfPrime(n)
def isPrime(x, primes):
	if x == 1:
		return False
	sqrtx = math.sqrt(x)
	for prime in primes:
		if (prime <= sqrtx):
			if (x == prime):
				return True
			elif (x % prime == 0):
				return False
		else: 
			break
	return True

def isPrimeNaive(x):
	if x == 1:
		return False
	for i in range(2, int(math.sqrt(x))+1):
		if (x % i == 0):
			return False
	return True

def measurePerformance(numberOfTests):
	listOfParameters = random.sample(range(1, 1000000000), numberOfTests)
	# test naive method
	startTime = datetime.datetime.now()
	testNaivePerformance(listOfParameters)
	endTime = datetime.datetime.now()
	naivePerformance = endTime - startTime
	# test heuristic method
	startTime = datetime.datetime.now()
	primes = getListOfPrimes(1000000000)
	testHeuristicMethodPerformance(listOfParameters, primes)
	endTime = datetime.datetime.now()
	heuristicPerformance = endTime - startTime
	# print performance
	print("Naive Method: " + str(naivePerformance))
	print("Heuristic Method: " + str(heuristicPerformance))
	# analyze performance
	print("My Algorithm takes " + format(heuristicPerformance.total_seconds()/naivePerformance.total_seconds()*100, '.2f') + " % of time compared to the naive method with " + str(numberOfTests) + " tests.")

def testCorrectness(primes):
	listOfParameters = range(1,(1000000000))
	naiveResult = testNaivePerformance(listOfParameters)
	heuristicResult = testHeuristicMethodPerformance(listOfParameters, primes)
	if (len(naiveResult) != len(heuristicResult)):
		print("The Algorithm is incorrect.")
		print(len(naiveResult))
		print(len(heuristicResult))
	for i in range(0, len(naiveResult)):
		if (naiveResult[i] != heuristicResult[i]):
			print("The Algorithm is incorrect.")
			print("Naive: " + naiveResult[i])
			print("Heuristic: " + heuristicResult[i])
			return False
	print("The Algorithm is correct")
	return True

	
def testNaivePerformance(numbers):
	results = []
	for i in numbers:
		if (isPrimeNaive(i)):
			results.append(i)
	return results

def testHeuristicMethodPerformance(numbers, primes):
	results = []
	for i in numbers:
		if (isPrime(i, primes)):
			results.append(i)
	return results

if __name__ == "__main__":
	primes = getListOfPrimes(1000000000)
	# testing correctness takes too much time
	# correctness = testCorrectness(primes)
	# if (!correctness):
	#	print("Not Correct")
	# else:
	# 	print("Correct")
	measurePerformance(50000)

