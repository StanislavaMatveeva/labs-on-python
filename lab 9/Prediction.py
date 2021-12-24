import pandas
from scipy.optimize import curve_fit
from scipy import interpolate
from EnumClass import EnumClass
import math

class Prediction:

    enum = EnumClass()

    def deleteNans(self, data, metric):
        years = data[self.enum.YEAR]
        metricValues = data[metric]
        x = []
        y = []
        for i in range(len(years)):
            if not math.isnan(metricValues.values[i]):
                x.append(years.values[i])
                y.append(metricValues.values[i])
        return x, y

    def fillNanValuesByInterpolation(self, data):
        x = data[self.enum.YEAR]
        for metric in self.enum.metrics:
            cleraX, y = self.deleteNans(data, metric)
            interpolator = interpolate.interp1d(cleraX, y, kind=self.enum.INTERPORATION_METHOD)
            data[metric] = interpolator(x)
        return data

    def readFile(self):
        data = pandas.read_csv(self.enum.FILENAME)
        if len(data) == 0:
            raise Exception('this file is empty')
        return data

    def getValues(self, x, y, paramValue):
        args = self.approximation(x, y)
        j = len(x)
        for i in range(self.enum.START_YEAR_FOR_APPROXIMATION, paramValue):
            x.loc[j] = i
            j += 1
        return x, self.mainFunction(x, args[self.enum.A_COEF_INDEX], args[self.enum.B_COEF_INDEX], args[self.enum.C_COEF_INDEX], args[self.enum.D_COEF_INDEX])
        
    def mainFunction(self, x, a, b, c, d):
        return -a * x**3 + b * x**2 + c * x + d

    def approximation(self, x, y):
        args, _ = curve_fit(self.mainFunction, x, y)
        return args

        