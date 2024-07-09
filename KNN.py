import numpy as np
from collections import Counter
from distances import euclidean_distance

class KNN:
    def __init__(self, k = 3, max_k=10):
        self.k =  k-1 if (k % 2 == 0) else k
        self.k_range = np.arange(max_k)
        # self.k_values = [k if k%2 != 0 else k+1 for k in max_k]
        
    def fit(self, x, y):
        self.X_train = x
        self.y_train = y
    
    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return predictions
        
    def _predict(self, x) -> int:
        # X is a 2d numpy where each row is a data point and each column is a feature.
        # compute the distance
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
    
        # get the closest k
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        # majority vote
        most_common = Counter(k_nearest_labels).most_common()
        return most_common[0][0]