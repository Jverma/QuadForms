# -*- coding: utf-8 -*-
#	Distribution function of quadratic forms in normal variables. 
#	Author - Janu Verma
#	jv367@cornell.edu
#	@januverma


import math
import numpy as np
from scipy.stats import chi2, ncx2


def DistributionFunction(q, lambdaValues, mult=None, delta=None):
	"""
	Implements methods to compute the distribution function of a
	linear combination of quadratic	forms in normal variables. 
	This can be used if e.g. we have a test statistic which has 
	distribution as a mixture of chi square distributions.

	Computes the probability of the distribution function to 
	have a value greater than the given values i.e. the 
	p-value of the distribution.

	We will use the approximation proposed by Liu et al. 
	This approximate method which expresses the distribution 
	function as a standard chi-square distribution function 
	and then computes the p-value accordingly.

	Parameters
	----------
	q : Value at which the distribution function is to be evaluated. 

	lambdaValues : A numpy array of the coefficients of the quadratic forms.
	
	mult : A numpy array of the multiplicities of the lambdaValues. 
			Default is an array of ones. 
	
	delta : A numpy array of non-centrality parameters. 
			Default is an array of zeros.  


	Returns
	-------
	pval : numeric value of the Prob(Q > q).


	Example
	--------
	>>> import numpy as np
	>>> from QuadFormsDistribution.quadforms import DistributionFun
	>>> q = 2
	>>> lambdaValues = np.array([0.5,0.4,0.1])
	>>> mult = np.array([1,2,1])
	>>> delta = np.array([1,0.6,0.8])
	>>> X = DistributionFun(q,lambdaValues, mult, delta)


	References
	----------
	[1] P. Duchesne, P. Lafaye de Micheaux, Computing the distribution of quadratic
	form : Further comparisons between the Liu-Tang-Zhanf approximation and 
	exact methods, Computational Statistics and Data Analysis, Volume 54,(2010), 858-862.

	[2] H.Liu, Y.Tang, H.H. Zhang, A new chi-square approximation to the distribution
	of non-negative definite quadratic forms in non-certral normal variables. 
	Computational Statistics and Data Analysis, Volume 53,(2009), 853-856. 


	"""
	n = len(lambdaValues)
	if (mult == None):
		mult = np.ones(n)

	if (delta == None):
		delta = np.ones(n)

	if (len(mult) != n):
		print "Error : lambdaValues and mult should have same length."

	if (len(delta) != n):
		print "Error : lambdaValues and delta should have same length."

	
	# Compute Liu parameters. 
	param1 = np.sum(lambdaValues.dot(mult)) + np.sum(lambdaValues.dot(delta))
	param2 = np.sum((lambdaValues**2).dot(mult)) + 2*np.sum((lambdaValues**2).dot(delta))
	param3 = np.sum((lambdaValues**3).dot(mult)) + 3*np.sum((lambdaValues**3).dot(delta))
	param4 = np.sum((lambdaValues**4).dot(mult)) + 4*np.sum((lambdaValues**4).dot(delta))

	alpha = param2**(1.5)
	s1 = float(param3)/alpha

	s2 = float(param4)/(param2**2)

	# mean and sd of the distribution. 
	meanQ = param1	
	sigmaQ = math.sqrt(2*param2)


	# t-statistic
	tStar = float(q - meanQ)/sigmaQ


	if ((s1**2) > s2):
		a = 1/float(s1 - math.sqrt(s1**2 - s2))
		delta = s1*(a**3) - (a**2)
		l = (a**2) - 2*delta

	else:
		a = 1/float(s1)
		delta = 0
		l = (param2**3)/(param3**2)


	# mean and sd of the chi-square distribution.
	meanX = l + delta
	sigmaX = math.sqrt(2)*a


	# p-value
	approxChi2 = tStar*sigmaX + meanX
	if (delta != 0):
		pval = 1 - ncx2.cdf(approxChi2,l,delta)
	else:
		pval = 1 - chi2.cdf(approxChi2,l)	


	return pval





















