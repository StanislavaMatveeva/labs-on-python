from numpy import greater
from FileWorker import FileWorker
from Clustering import Clustering
from Presentation import ClustersPresentation
import matplotlib.pyplot as graphic

FILENAME = 'source.txt'

fileWorker = FileWorker()
points = fileWorker.getArrayOfPoints(FILENAME)
clustering = Clustering(points)
graphics = ClustersPresentation(clustering)
graphics.drawAllGraphics(points)
