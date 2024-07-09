import numpy as np

class Node:
    def __init__(self, feature=None, threshold=None, right=None, left=None,*,value=None):
        self.feature = feature
        self.threshold = threshold
        self.right = right
        self.left = left
        self.value = None
        
    def is_left_node(self) -> bool:
        return self.value is not None
        
        
    
class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=150, num_features=None):
        self.min_samples_split = min_samples_split
        self.max_depth =max_depth
        # add some randomness so that not all features are used but a subset of them
        self.num_features = num_features 
        self.root = None
    
    def fit(self, x, y):
        self.num_features = x.shape[1] if not self.num_features else min(x.shape[1], self.num_features)
        self.root = self._grow_tree(x,y)
        
    def _grow_tree(self, x, y):
        # check the stopping criteria
        
        # find the best split
        
        
        # create the child nodes
    
    def predict():
        pass
        
    