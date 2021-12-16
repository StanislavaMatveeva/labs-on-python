from itertools import cycle
from matplotlib import axes
from matplotlib import markers
from matplotlib.colors import Colormap
from matplotlib.figure import Figure
from matplotlib.markers import MarkerStyle
import matplotlib.pyplot as graphic
import numpy
from numpy.core.fromnumeric import size
import scipy
import seaborn
from seaborn.matrix import dendrogram
from seaborn.palettes import color_palette

class ClustersPresentation:

    AMOUNT_OF_CLUSTERS = 15
    AMOUNT_OF_METHODS = 10
    FIRST_INDEX = 0
    SECOND_INDEX = 1
    KMEANS = 0
    AFFINITY = 1
    PLOT_ROWS_COUNT = 3
    PLOT_COLUMNS_COUNT = 2
    names = ['Main Dataset', 'K-means', 'Affinity Propagation', 'Mean Shift', 'Agglomerative Clustering', 'DBSCAN']

    def __init__(self, clustering):
        self.clustering = clustering

    def getColumns(self, points):
        if len(points) == 0:
            raise Exception('empty array of points')
        XYArray = []
        xValues = []
        yValues = []
        for i in range(len(points)):
            xValues.append(points[i][self.FIRST_INDEX])
            yValues.append(points[i][self.SECOND_INDEX])
        XYArray.append(xValues)
        XYArray.append(yValues)
        return XYArray

    def drawOneGraphic(self, points, methodNumber):
        newPlot = graphic.subplot(self.PLOT_ROWS_COUNT, self.PLOT_COLUMNS_COUNT, methodNumber + 1)
        newPlot.set_title(self.names[methodNumber])
        if methodNumber != self.clustering.MAIN_DATASET:
            clusters, timeOfWork = self.clustering.getClusters(points, methodNumber)
            points = self.getColumns(points)
            newPlot.scatter(points[self.FIRST_INDEX], points[self.SECOND_INDEX], s=3, c=clusters.labels_)
            if methodNumber == self.clustering.KMEANS:
                centers = self.getColumns(clusters.cluster_centers_)
                newPlot.scatter(centers[self.FIRST_INDEX], centers[self.SECOND_INDEX], s=5, c='black')
            newPlot.text(2, 7, f'{timeOfWork}s')
        else:
            points = self.getColumns(points)
            newPlot.scatter(points[self.FIRST_INDEX], points[self.SECOND_INDEX], s=3) 
        graphic.xticks(())
        graphic.yticks(())

    def drawAllGraphics(self, points):
        if len(points) == 0:
            raise Exception('empty array of points')
        palette = seaborn.color_palette(palette='tab20c', as_cmap=True)
        graphic.set_cmap(palette)
        for i in range(self.clustering.AMOUNT_OF_METHODS + 1):
            self.drawOneGraphic(points, i)
        graphic.show()