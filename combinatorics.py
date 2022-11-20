# -*- coding: utf-8 -*-

def get_nel(ndim,nel=None):
	if nel==None:
		nel = ndim
	if not isinstance(ndim,int):
		raise ValueError("The given number of elements to consider is not an integer.")
	if not isinstance(nel,int):
		raise ValueError("The given number of elements to take is not a integer.")
	return nel


def factorial(number):
	"""
	Computes the factorial of a number.
	
	:param number: The number of which the factorial is wanted.
	:return: The factorial of the number.
	"""
	if number<2:
		return 1
	else:
		return number*factorial(number-1)


def binomial(n,m):
	"""
	Computes the binomial coeficient n choose m.
	
	:param n: Top part of the binomial coeficient.
	:param m: Bottom part of the binomial coeficient.
	:return: The binomial coeficient n choose m.
	"""
	k = n-m+1
	num = 1
	while k<=n:
		num *= k
		k += 1
	return num//factorial(m)


def nperm(n,m):
	"""
	Computes the number of permutations of n elements
	taken m by m.

	:param n: Number of elements to consider.
	:param m: Number of elements to take.
	:return: Te number of permutations.
	"""
	p = 1
	k = n-m+1
	while k<=n:
		p *= k
		k += 1
	return p


def combinations_wo_repetition(elements, nelem=None):
	"""
	Gets a generator of all possible subsets of a given size
	of the elements of a list or a tuple (without repetition).
	
	:param elements: A list or a tuple containing the elements of the set.
	:param nelem: Number of elements taken from the set.
	:return: A generator any possible subset.
	"""
	ndim = len(elements)
	nel = get_nel(ndim,nelem)
	if nel<0 or ndim<nel:
		raise ValueError("It's not possible to combine " + str(ndim) + " elemenents " + str(nel) + " by " + str(nel) + ".")
	if nel==0:
		yield []
	else:
		for i in range(ndim-nel+1):
			for combination in combinations_wo_repetition(elements[i+1:ndim],nel-1):
				yield [elements[i]] + combination


def combinations_w_repetition(elements, nelem=None):
	"""
	Gets a generator of all possible combinations of a given
	number of elements from a list or a tuple with repetitions.

	:param elements: A list containing the elements to combine.
	:param nelem: Number of elements taken from the set.
	:return: A generator of all possible combination.
	"""
	ndim = len(elements)
	nel = get_nel(ndim,nelem)
	if nel<0:
		raise ValueError("It's not possible to combine " + str(ndim) + " elemenents " + str(nel) + " by " + str(nel) + ".")
	if nel==0:
		yield []
	else:
		for i in range(ndim):
			for combination in combinations_w_repetition(elements[i:ndim],nel-1):
				yield [elements[i]] + combination


def variations_w_repetition(elements, nel=None):
	"""
	Gets a generator of any possible variation of the elements
	given taken nel by nel (with repetition).

	:param elements: The list of elements to combine.
	:param nel: Number of elements to take in each variation.
	:return: A generator of all possible variation.
	"""
	ndim = len(elements)
	if nel==None:
		nel = 1
	if not isinstance(ndim,int):
		raise ValueError("The given number of elements to consider is not an integer.")
	if not isinstance(nel,int):
		raise ValueError("The given number of elements to take is not a integer.")
	if nel<0:
		raise ValueError("It's not possible to combine " + str(ndim) + " elemenents " + str(nel) + " by " + str(nel) + ".")
	if nel==0:
		yield []
	else:
		for i in range(ndim):
			for variation in variations_w_repetition(elements,nel-1):
				yield [elements[i]] + variation


def variations_wo_repetition(elements, nelem=None):
	"""
	Gets a generator of any possible variation of the elements
	given taken nelem by nelem (without repetition).

	:param elements: The list of elements to combine.
	:param nelem: Number of elements to take in each variation.
	:return: A generator of all possible variation.
	"""
	ndim = len(elements)
	nel = get_nel(ndim,nelem)
	if nel<0 or ndim<nel:
		raise ValueError("It's not possible to combine " + str(ndim) + " elemenents " + str(nel) + " by " + str(nel) + ".")
	if nel==0:
		yield []
	else:
		for i in range(ndim):
			for variation in variations_wo_repetition(elements[0:i]+elements[i+1:ndim],nel-1):
				yield [elements[i]] + variation


def permutations(elements, nelem=None):
	"""
	Gets a generator of all possible permutations of the
	elements of a given list or tuple took nelem by nelem.

	:param elements: The list of elements to permute.
	:param nelem: Number of elements to take in each permutation.
	:return: A generator of all possible permutation.
	"""
	return variations_wo_repetition(elements, nelem)
