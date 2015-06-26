# QuadForms
Distribution function of a linear combination of quadratic forms in normal variables. 


If we have a statistics which has a distribution as a linear combination of chi-square distributions. This method computes the probability of the distribution function to have a value greater than the given values i.e. the p-value of the distribution.
We will use the approximation proposed by Liu et al. This approximate method which expresses the distribution function as a standard chi-square distribution function and then computes the p-value accordingly.

**Input:**

    lambdaValues : A numpy array of the coefficients of the quadratic forms.

**Usage**

    import numpy as np
	from QuadFormsDistribution.quadforms import DistributionFun
	  
	q = 2
    lambdaValues = np.array([0.5,0.4,0.1])
	mult = np.array([1,2,1])
	delta = np.array([1,0.6,0.8])
	X = DistributionFun(q,lambdaValues, mult, delta)



**References**


	[1] P. Duchesne, P. Lafaye de Micheaux, Computing the distribution of quadratic
	form : Further comparisons between the Liu-Tang-Zhanf approximation and 
	exact methods, Computational Statistics and Data Analysis, Volume 54,(2010), 858-862.

	[2] H.Liu, Y.Tang, H.H. Zhang, A new chi-square approximation to the distribution
	of non-negative definite quadratic forms in non-certral normal variables. 
	Computational Statistics and Data Analysis, Volume 53,(2009), 853-856. 



