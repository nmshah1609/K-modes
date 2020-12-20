# K-modes
Implementation of k-modes algorithm from scratch


Code outline:
Algorithm: k-modes(dataset, numOfClusters)
Input: Data, k
Output: Cj where 1 <= j <= k

-Step 1: Randomly select the K initial cluster centers such that Cj, j = 1,2,...,K
-Step 2: Find the matching dissimilarity between the each K initial cluster modes and each data objects using the minizing cost function TD(C,m)
-Step 3: Evaluate the fitness using the dissimilarity distance function (Hamming distance)
-Step 4: Find the minimum mode values in each data object i.e. finding the objects nearest to the initial cluster modes.
-Step 5: Assign the data objects to the nearest cluster modes.
-Step 6: Update the modes by applying the frequency based method on newly formed clusters
-Step 7: Recalculate the similarity between the objects and the updated modes 
-Step 8: Repeat step 4 - 5 until no changes in the cluster ship of the objects

Psuedocode:

key:
k = numOfClusters
X = data

Algorithm: get_distance(x, c)
Input: numOfClusters, sizeOfDataset
Output: distance
```
dist <- 0
IF x is not equal to c do
	dist += 1
```


Algorithm: kmodes(dataset, numOfClusters)
Input: X, k
Output: Cj where 1 <= j <= k
```
C1 <- empty array
Randomly select k cluster centres from X with n objects
C <- random k clusters
FOR i from 0 to range of n do  
	minDist <- intialize with some large value
    FOR j from 0 to k do
	    Calculate the distance between ith data point and jth mode vector using dissimilarity distance function and assign that data point to appropriate cluster whose cluster mode vector is closer to it and update mode vector of corresponding cluster and also find the
		distribution of mode categories between clusters
		dist <- get_distance(C[row index, features], X[row index, features])
        IF dist < minDist do
            minDist <- dist
            clustNum <- j
            X[i,d] <- clustNum
            C[j,d] <- clustNum
        ENDIF
    ENDFOR
    FOR j from 0 to k do
    	result <- indexes where X[:d] == j
        mode_info <- array of modal values
        C[j] <-  reshape modal array
    ENDFOR
ENDFOR
WHILE c1 is not equal to c do
	c1 <- c
	FOR i from 0 to range of n do  
	minDist <- intialize with some large value
	    FOR j from 0 to k do
		    Calculate the distance between ith data point and jth mode vector using dissimilarity distance function (6) and assign that data point to appropriate cluster whose cluster mode vector is closer to it and update mode vector of corresponding cluster and also find the distribution of mode categories between clusters 
			dist <- get_distance(C[row index, features], X[row index, features])
	        IF dist < minDist do
	            minDist <- dist
	            clustNum <- j
	            X[i,d] <- clustNum
	            C[j,d] <- clustNum
	        ENDIF
    	ENDFOR
    	FOR j from 0 to k do
	    	result <- indexes where X[:d] == j
	        mode_info <- array of modal values
	        C[j] <-  reshape modal array
    	ENDFOR
	ENDFOR
	IF old_modes is equal to new_modes
	 	then break the loop
 	ENDIF
ENDWHILE
```
