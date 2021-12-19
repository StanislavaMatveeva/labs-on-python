from re import T
import numpy
from numpy.lib.function_base import percentile
from sklearn import cluster
from sklearn import datasets
from sklearn.cluster import KMeans, AffinityPropagation, MeanShift, AgglomerativeClustering, DBSCAN
from sklearn.datasets import make_blobs
import time

class Clustering:

    AMOUNT_OF_CLUSTERS = 15
    FIRST_INDEX = 0
    SECOND_INDEX = 1
    MAIN_DATASET = 0
    KMEANS = 1
    AFFINITY_PROPAGATION = 2
    MEAN_SHIFT = 3
    AGGLOMERATIVE_CLUSTERING = 4
    DBSCAN = 5
    RANDOM_KMEANS = 5
    RANDOM_AFFINITY_PROPAGATION = 6
    RANDOM_MEAN_SHIFT = 7
    AMOUNT_OF_METHODS = 5
    PREFERENCE = -890000000
    DAMPING = 0.96
    CONVERGENCE_ITER = 5
    BIN_SEEDING = True
    MIN_BIN_FREQ = 15
    BANDWIDTH = 50000
    LINKAGE = 'ward'
    EPS = 21000
    MIN_SAMPLES = 5

    def __init__(self, points):
        if len(points) == 0:
            raise Exception('empty array of points')
        self.points = points

    def getClusters(self, points, methodNumber):
        if len(points) == 0:
            raise Exception('empty array of points')
        if methodNumber == self.KMEANS:
            clusters = KMeans(n_clusters=self.AMOUNT_OF_CLUSTERS)
        elif methodNumber == self.AFFINITY_PROPAGATION:
            clusters = AffinityPropagation(damping=self.DAMPING, convergence_iter=self.CONVERGENCE_ITER, preference=self.PREFERENCE)
        elif methodNumber == self.MEAN_SHIFT:
            clusters = MeanShift(bin_seeding=self.BIN_SEEDING, min_bin_freq=self.MIN_BIN_FREQ, bandwidth=self.BANDWIDTH)
        elif methodNumber == self.AGGLOMERATIVE_CLUSTERING:
            clusters = AgglomerativeClustering(n_clusters=self.AMOUNT_OF_CLUSTERS, linkage=self.LINKAGE)
        elif methodNumber == self.DBSCAN:
            clusters = DBSCAN(eps=self.EPS, min_samples=self.MIN_SAMPLES)
        startTime = time.time()
        clusters.fit(points)
        endTime = time.time() - startTime
        return clusters, round(endTime, 3)


    
