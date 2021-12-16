import os
import numpy

class FileWorker:

    MAX_SIZE_OF_FILE = 200000
    FIRST_INDEX = 0
    SECOND_INDEX = 1

    def checkFile(self, fileName):
        if os.path.isfile(fileName) == False:
            raise Exception("it is not a file")
        if os.path.exists(fileName) == False:
            raise Exception("there is no file with such name or it can't be opened")
        size = os.stat(fileName).st_size
        if size == 0 or size > self.MAX_SIZE_OF_FILE:
            raise Exception('this file is empty')
    
    def readFile(self, fileName):
        self.checkFile(fileName)
        with open(fileName, 'r') as sourceFile:
            data = sourceFile.readlines()
            sourceFile.close()
        if len(data) == 0:
            raise Exception('there is no data in file')    
        return data
    
    def deleteExtraSymbols(self, lines):
        for i in range(len(lines)):
            if '\n' in lines[i]:
                lines[i] = lines[i].replace('\n', '')
            while '  ' in lines[i]:
                lines[i] = lines[i].replace('  ', ' ')
            if lines[i][self.FIRST_INDEX] == ' ':
                lines[i] = lines[i].strip()
        return lines
    
    def getArrayOfPoints(self, fileName):
        data = self.readFile(fileName)
        data = self.deleteExtraSymbols(data)
        points = []
        for line in data:
            coordinats = line.split(' ')
            point = []
            try: 
                point.append(int(coordinats[self.FIRST_INDEX]))
                point.append(int(coordinats[self.SECOND_INDEX]))
            except: raise Exception('invalid data in file')
            points.append(point)
        return points
                

            

        
        
