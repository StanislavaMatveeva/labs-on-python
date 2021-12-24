import numpy
import matplotlib.pyplot as graphic
import tkinter
from tkinter.ttk import Combobox
from tkinter import messagebox
import pandas
from Prediction import Prediction
from sklearn.linear_model import LinearRegression
from EnumClass import EnumClass

class Presentation:

    approx = Prediction()
    enum = EnumClass()

    def __init__(self):
        self.window = tkinter.Tk()
        self.regionNameLabel = tkinter.Label(self.window, bg=self.enum.WIDGETS_COLOR, text=self.enum.labels[0], font=(self.enum.FONT, self.enum.FONT_SIZE))
        self.comboBox = Combobox(self.window, state=self.enum.COMBOBOX_STATE, font=(self.enum.FONT, self.enum.FONT_SIZE), width=self.enum.WIDTH)
        self.paramLabel = tkinter.Label(self.window, bg=self.enum.WIDGETS_COLOR, text=self.enum.labels[1], font=(self.enum.FONT, self.enum.FONT_SIZE), width=self.enum.WIDTH)
        self.paramText = tkinter.Entry(self.window, bg=self.enum.WIDGETS_COLOR, font=(self.enum.FONT, self.enum.FONT_SIZE), width=self.enum.PARAMETR_TEXT_WIDTH)
        self.buttonCreate = tkinter.Button(self.window, bg=self.enum.HEADERS_COLOR, text=self.enum.labels[2], font=(self.enum.FONT, self.enum.FONT_SIZE), command=self.buttonClicked, width=self.enum.BUTTON_WIDTH)
        self.metricsLabel = tkinter.Label(self.window, bg=self.enum.HEADERS_COLOR, text=self.enum.labels[3], font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
        self.approximationPredictionsLabel = tkinter.Label(self.window, bg=self.enum.HEADERS_COLOR, text=self.enum.labels[4], font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
        self.regressionPredictionsLabel = tkinter.Label(self.window, bg=self.enum.HEADERS_COLOR, text=self.enum.labels[5], font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
        self.npgValueLabel = tkinter.Label(self.window, bg=self.enum.WIDGETS_COLOR, text=self.enum.labels[6], font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
        self.birthRateLabel = tkinter.Label(self.window, bg=self.enum.WIDGETS_COLOR, text=self.enum.labels[7], font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
        self.deathRateLabel = tkinter.Label(self.window, bg=self.enum.WIDGETS_COLOR, text=self.enum.labels[8], font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
        self.gdwLabel = tkinter.Label(self.window, bg=self.enum.WIDGETS_COLOR, text=self.enum.labels[9], font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
        self.urbanizationLabel = tkinter.Label(self.window, bg=self.enum.WIDGETS_COLOR, text=self.enum.labels[10], font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
        self.npgByApproximation = tkinter.Label(self.window, bg=self.enum.WIDGETS_COLOR, font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
        self.birthRateByApproximation = tkinter.Label(self.window, bg=self.enum.WIDGETS_COLOR, font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
        self.deathRateByApproximation = tkinter.Label(self.window, bg=self.enum.WIDGETS_COLOR, font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
        self.gdwByApproximation = tkinter.Label(self.window, bg=self.enum.WIDGETS_COLOR, font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
        self.urbanizationByApproximation = tkinter.Label(self.window, bg=self.enum.WIDGETS_COLOR, font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
        self.npgByRegression = tkinter.Label(self.window, bg=self.enum.WIDGETS_COLOR, font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
        self.birthRateByRegression = tkinter.Label(self.window, bg=self.enum.WIDGETS_COLOR, font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
        self.deathRateByRegression = tkinter.Label(self.window, bg=self.enum.WIDGETS_COLOR, font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
        self.gdwByRegression = tkinter.Label(self.window, bg=self.enum.WIDGETS_COLOR, font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
        self.urbanizationByRegression = tkinter.Label(self.window, bg=self.enum.WIDGETS_COLOR, font=(self.enum.FONT, self.enum.FONT_SIZE), relief= self.enum.RELIEF, width=self.enum.WIDTH)
    
    def drawGraphicsForOneMetric(self, paramValue, regionData, metricIndex, method):
        regionData = self.approx.fillNanValuesByInterpolation(regionData)
        x = regionData[self.enum.YEAR]
        y = regionData[self.enum.metrics[metricIndex]]
        graphic.figure(method)
        mainPlot = graphic.subplot(self.enum.ROWS_COUNT, self.enum.COLUMNS_COUNT, metricIndex + 1)
        mainPlot.clear()
        mainPlot.set_title(f'{self.enum.metricsNames[metricIndex]}')
        mainPlot.scatter(x, y, s=3)
        if method == self.enum.APPROXIMATION:
            x, prediction = self.approx.getValues(x, y, paramValue)
            color = self.enum.APPROXIMATION_COLOR
            self.showApproximationPrediction(self.enum.metrics[metricIndex], numpy.array(prediction))
        elif method == self.enum.REGRESSION:
            regression = LinearRegression().fit(numpy.array(x).reshape((-1, 1)), numpy.array(y))
            x = numpy.arange(self.enum.START_YEAR_FOR_REGRESSION, paramValue).reshape((-1, 1))
            prediction = regression.predict(x)
            color = self.enum.REGRESSION_COLOR
            self.showRegressionPrediction(self.enum.metrics[metricIndex], prediction)
        predictionPlot = graphic.subplot(self.enum.ROWS_COUNT, self.enum.COLUMNS_COUNT, metricIndex + 6)
        predictionPlot.clear()
        predictionPlot.plot(x, prediction, color=color)

    def showApproximationPrediction(self, paramName, prediction):
        resultValue = round(prediction[len(prediction) - 1], 3)
        if paramName == self.enum.metrics[0]:
            self.npgByApproximation.configure(text=str(resultValue))
        elif paramName == self.enum.metrics[1]:
            self.birthRateByApproximation.configure(text=str(resultValue))
        elif paramName == self.enum.metrics[2]:
            self.deathRateByApproximation.configure(text=str(resultValue))
        elif paramName == self.enum.metrics[3]:
            self.gdwByApproximation.configure(text=str(resultValue))
        elif paramName == self.enum.metrics[4]:
            self.urbanizationByApproximation.configure(text=str(resultValue))
    
    def showRegressionPrediction(self, paramName, prediction):
        resultValue = round(prediction[len(prediction) - 1], 3)
        if paramName == self.enum.metrics[0]:
            self.npgByRegression.configure(text=str(resultValue))
        elif paramName == self.enum.metrics[1]:
            self.birthRateByRegression.configure(text=str(resultValue))
        elif paramName == self.enum.metrics[2]:
            self.deathRateByRegression.configure(text=str(resultValue))
        elif paramName == self.enum.metrics[3]:
            self.gdwByRegression.configure(text=str(resultValue))
        elif paramName == self.enum.metrics[4]:
            self.urbanizationByRegression.configure(text=str(resultValue))
    
    def buttonClicked(self):
        region = self.comboBox.get()
        if region == '':
            messagebox.showerror(self.enum.errors[0], self.enum.errors[1])
        try:
            year = int(self.paramText.get())
        except:
            messagebox.showerror(self.enum.errors[2], self.enum.errors[3])
        if year < self.enum.START_YEAR_FOR_APPROXIMATION:
            messagebox.showerror(self.enum.errors[4], self.enum.errors[5])
        else:
            self.drawGraphics(region, year)
    
    def drawGraphics(self, regionName, paramValue):
        data = self.approx.readFile()
        regionData = data[data.region == regionName]
        for i in range(len(self.enum.metrics)):
            self.drawGraphicsForOneMetric(paramValue, regionData, i, self.enum.APPROXIMATION)
            self.drawGraphicsForOneMetric(paramValue, regionData, i, self.enum.REGRESSION)
        graphic.show()
        
    def createWindow(self):
        data = self.approx.readFile()
        self.window.title(self.enum.titles[3])
        self.window.geometry(self.enum.WINDOW_GEOMETRY)
        self.window['bg'] =  self.enum.WIDGETS_COLOR
        self.regionNameLabel.grid(column=0, row=0)
        self.comboBox['values'] = list(numpy.unique(data[self.enum.REGION]))
        self.comboBox.grid(column=1, row=0)
        self.paramLabel.grid(column=0, row=1)
        self.paramText.grid(column=1, row=1)
        self.buttonCreate.grid(column=2, row=0)
        self.metricsLabel.grid(column=0, row=2)
        self.approximationPredictionsLabel.grid(column=1, row=2)
        self.regressionPredictionsLabel.grid(column=2, row=2)
        self.npgValueLabel.grid(column=0, row=3)
        self.birthRateLabel.grid(column=0, row=4)
        self.deathRateLabel.grid(column=0, row=5)
        self.gdwLabel.grid(column=0, row=6)
        self.urbanizationLabel.grid(column=0, row=7)
        self.npgByApproximation.grid(column=1, row=3)
        self.birthRateByApproximation.grid(column=1, row=4)
        self.deathRateByApproximation.grid(column=1, row=5)
        self.gdwByApproximation.grid(column=1, row=6)
        self.urbanizationByApproximation.grid(column=1, row=7)
        self.npgByRegression.grid(column=2, row=3)
        self.birthRateByRegression.grid(column=2, row=4)
        self.deathRateByRegression.grid(column=2, row=5)
        self.gdwByRegression.grid(column=2, row=6)
        self.urbanizationByRegression.grid(column=2, row=7)
        self.window.mainloop()