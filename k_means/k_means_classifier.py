import random 

print("Hello")

class k_means :
    
    def __init__(self,max_iteration = 100,n_clusters = 2 ):
        self.cluster = n_clusters
        self.max_iteration = max_iteration
        self.centroid = None
        
    def fit_predict(self,x_train):
        index = random.sample((0,x_train.shape[0]),x_train.shape[0])
        print("Index")