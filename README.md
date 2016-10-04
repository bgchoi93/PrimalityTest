# PrimalityTest
Algorithm for Primality Test from scratch (for a number < 1,000,000,000)

I have tried this problem under an assumption that this algorithm is not a one-time-use algorithm, 
i.e. we use it multiple times under the same assumptions.
If one-time or few times use, we have to trade-off between: correctness or time 
If fast evaluation is more important than accuracy, (2) is suitable
If correctness is required, (1) is suitable. 

(1) Initially, I started from a scratch: divide N by every number from 2 to N-1, which will take O(n) time.
Next, to reduce unnecessary operations, divde N by every number from 2 to sqrt(N). 
Then, by removing even numbers, the algorithm performs division with only odd numbers. 
This algorithm has an O(1/2n^(1/2)) = O(n^(1/2)) time complexity.

(2) Since that method was not enough, I recalled Fermat’s Little theorem from algebra and analysis class:
for any a : n mod a = 0, if p is prime, then a*(p-1) is congruent with 1 (mod p),
i.e. a^(p-1) mod p = 1.
By using this theorem, the algorithm time complexity could be reduced down to O(1) time. 
However, this theorem only holds for prime numbers. If a number is not prime, there was no guarantee that the number can be checked correctly => we have to change the base a for such numbers.
I thought that using randomly chosen a or iteratively using Fermat’s little theorem for k time could give a true answer with very high probability and the time complexity would be O(k) time where k is the number of trials. 
But then I found out that no matter what base we have, there are certain numbers that could be not determined correctly as non prime numbers. (I can manually maintain a list of these integers but it might be not what you are looking for from me, and also there are many bases possible, so if we want to make it completely accurate, I’d rather choose another method)

(3) Thus, I came back to the first method.  
I recalled that every positive integer greater than 3 is a product of prime numbers. 
Also, assuming that this algorithm is not one-time-use only, and we are given an assumption that N < 1,000,000,000, I decided to improve the method I started with. 
The common trial division has a problem: We have to check unnecessary cases - even numbers except 2 and non prime numbers (it is a result of the fact that every integer greater than 3 is a product of prime numbers)
Thus to avoid unnecessary iteration, having a list of prime numbers less than sqrt(N) would let us check only prime numbers less than sqrt(N).
Although this heuristic method is more expensive than the trial division method, it turns out much more efficient than the trial division method as we use this method more than certain amount of time. 
Also, please note that we have to keep this list for future multiple time use.

From now, the max{N} is denoted as N, and the number we want to test is denoted as n. 
For getListOfPrime(n) function, I approached with an idea of the sieve of Eratosthenes: we set a list from 2 to N-1, and delete multiples of each number we encounter in the list. 
But the problems of this approach is that 
	1	we need too much unnecessary space to save all the numbers from 2 to N-1.
	2	traversing the whole list to flag(prime or not) each numbers takes O(n^2) time.
	3	we have to re traverse the list to build a list of primes. 
Thus, I combined it with the first method I came up:
	1	start with a list containing 2 and 3.
	2	start iterating from i = 5 to sqrt(N) with step size of 2 (excluding even numbers)
	3	check i is prime or not by checking if there is any divisor of i in the list of prime numbers so far. (we only need to check the list until the prime number p < sqrt(i))
	4	As we find a prime divisor of i: p < sqrt(i), break then move on the the next i = i + 2.  
	5	if there is no prime divisor: < sqrt(i) in the list, we append the i. 


By these steps, we only need a space for prime numbers < sqrt(N), and the number of iteration is O(1/2N^(1/2)) * O((1/2N^(1/2))^(1/2)) = O(N^(3/4)). 
But in fact it is much faster than O(N^(3/4)) since the number of primes < N^(1/2) is much less than N^(1/2). 
In other word, the time complexity of this algorithm is O(k*N^(1/2)) where k is the number of the primes < sqrt(N).
Again, it is much faster than O(k*N^(1/2)) since we are only checking the case that the prime divisor of the numbers only when the prime divisor is less than sqrt(i).

Then now, finally, we can use the heuristic: a list of prime numbers such that p in prime numbers’ list is less than sqrt(N) for all p.
Using that heuristic, I again try trial division, but this time with only prime numbers less than sqrt(n). 
This will take O(k) where k is the number of prime numbers < sqrt(n).
Under assumption that n < 1,000,000,000, the maximum number of iteration is 3401. 
(And as I tested by writing randomized simulation code, after 300~400 simulations it became more efficient then the trial division, 
and heuristic method’s number of iteration(including iteration performed by getListOfPrime) was larger than the one of trial division until approximately 300 simulations, 
But it is reduced down to approximately 23 percent of the trial division method(1) since after more than 2000 simulations.

Correctness of this algorithm:
It can be mathematically proven.
Test is written but it takes too much time to test for all the numbers < 1,000,000,000

Running Performance Test:
>>> measurePerformance(50000)
Naive Method: 0:00:11.088528
Heuristic Method: 0:00:02.473345
My Algorithm takes 22.31 % of time compared to the naive method with 50000 tests.
