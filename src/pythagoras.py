'''
	Project Euler Problem 9 

	A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

				a**2 + b**2 = c**2

	For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
	Find the product abc.


	Link : https://projecteuler.net/problem=9

'''

from operator import mul


class Pythagoras(object): 

	def __init__(self, sides=[]):
		self.sides = sides


	def get_sides_from_sum(self, psum=0):
		if psum <= 0 : 
			print "Error: Pythagorean sum cannot be less than  0"
			return None

		for b in range(int(psum/5), int(psum/2)):

			a = ((((psum**2)/2) - (psum * b)))/(psum - b)
			c = psum - a - b

			if c < 0 :
				continue

			print a, b, c

			if ((a**2) + (b**2)) == (c**2):
				self.sides = [a, b, c]
				print self.sides
				return self.sides

		return None


	def get_product(self, sides=[]):
		
		if self.sides == [] and sides:
			self.sides = sides

		product = reduce(mul, self.sides)

		return product


def main():

	pythagoras = Pythagoras()

	print "Special Pythagorean Triplets"

	if pythagoras.get_sides_from_sum(1000):
		print "Product is ", pythagoras.get_product()


if __name__ == "__main__":
	main()