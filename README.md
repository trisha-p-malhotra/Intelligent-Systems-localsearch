# Intelligent-Systems-localsearch
Implementation of Hill climb &amp; Simulated Annealing algorithms &amp; their random restart variants.

Tools used:<br>
-Python<br>

Problem Statement:<br>
Here we will experiment with a couple of different local search algorithms. The problem space is a little like hill climbing in real life: you are given a 2-D matrix of elevations and wish to find the 5x5 region within that matrix with the largest variation - that is, the value of a region is the difference between the smallest value and largest value within the region, and we wish to maximize the value. For testing, you can use this file, which contains 500 rows of 400 doubles each (in fact, you can hard-code the file and its size if you like). You should write the following functions (arguments and return types at your discretion):<br>
hillclimb performs a simple hill climb from a random starting location, testing all four one-pixel moves as successor states at each iteration and picking the best one (or stopping when reaching a maximum).<br>
rrhc performs a random restart hill climb 50 times and reports the average and maximum resulting value.<br>
sa performs simulated annealing as follows: start with T=2, choose a random one-pixel move at each iteration, and accept it based on the formula discussed in class (except that we are doing a maximization here, not a minimization). After each iteration, lower the temperature using T *= 0.999. When T reaches 0.1, begin a hill climb from the current state (this will give you better convergence) and return the result of this process.<br>
rrsa performs random-restart simulated annealing similarly to rrhc above.<br>

Report the results of your testing, along with your interpretation of these results - you may wish to try it a few times, and you are welcome to (but not required to) play around with the magic numbers in the simulated annealing.
