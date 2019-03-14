# iForest

The goal of this project is to implement the original Isolation Forest algorithm by Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou. (Read the paper for more detail) 
There are two general approaches to anomaly detection:
1) model what normal looks like and then look for nonnormal observations
2) focus on the anomalies, which are few and different. This is the interesting and relatively-new approach taken by the authors of isolation forests.

One of the known weaknesses of the original isolation forest is that it can't handle lots of irrelevant or noisy features (columns). We have a number of options for trying to improve the algorithm and one of them is when we split at decision nodes. Think about how we might decide whether one candidate (column and split value) is better than another. I tried to split smartly at the root node to avoid any noisy features ( check fit_improved ).








