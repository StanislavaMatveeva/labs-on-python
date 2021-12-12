import random

class FileWorker:

    def outputFiles(self, args):
        with open(args.source, 'r') as sourceFile:
            text = sourceFile.read()
            sourceFile.close()
        print(f'\nText in first file:\n{text}\n')
        with open(args.result, 'r') as resultFile:
            text = resultFile.read()
            resultFile.close()
        print(f'Text in second file:\n{text}\n')

    def writeDataInFile(self, args):
        file = open(args.source, 'r')
        lines = file.readlines()
        lines = self.deleteLinesDiveders(lines)
        file.close()
        self.writeLinesInFile(args.result, lines)   
    
    def swapStrings(self, array, ind_1, ind_2):
        tmp = array[ind_1]
        array[ind_1] = array[ind_2]
        array[ind_2] = tmp
        return array

    def deleteLinesDiveders(self, lines):
        for i in range(len(lines)):
            if '\n' in lines[i]:
                lines[i] = lines[i].replace('\n', '')
        return lines

    def writeLinesInFile(self, fileName, array):
        file = open(fileName, 'w')
        for line in array:
            file.write(line + '\n')
        file.close()

    def sortLinesByLengthInAscendingOrder(self, args):
        file = open(args.source, 'r')
        lines = file.readlines()
        lines = self.deleteLinesDiveders(lines)
        file.close()
        for i in range(len(lines) - 1):
            for j in range(len(lines) - 1):
                if len(lines[j]) > len(lines[j + 1]):
                    lines = self.swapStrings(lines, j, j + 1)
        self.writeLinesInFile(args.result, lines)

    def sortLinesByLengthInDescendingOrder(self, args):
        file = open(args.source, 'r')
        lines = file.readlines()
        lines = self.deleteLinesDiveders(lines)
        file.close()
        for i in range(len(lines) - 1):
            for j in range(len(lines) - 1):
                if len(lines[j]) < len(lines[j + 1]):
                    lines = self.swapStrings(lines, j, j + 1)
        self.writeLinesInFile(args.result, lines)

    def sortLinesByAlphabetInAscendingOrder(self, args):
        file = open(args.source, 'r')
        lines = file.readlines()
        lines = self.deleteLinesDiveders(lines)
        file.close()
        for i in range(len(lines) - 1):
            for j in range(len(lines) - 1):
                if lines[j].lower() > lines[j + 1].lower():
                    lines = self.swapStrings(lines, j, j + 1)
        self.writeLinesInFile(args.result, lines)

    def sortLinesByAlphabetInDescendingOrder(self, args):
        file = open(args.source, 'r')
        lines = file.readlines()
        lines = self.deleteLinesDiveders(lines)
        file.close()
        for i in range(len(lines) - 1):
            for j in range(len(lines) - 1):
                if lines[j].lower() < lines[j + 1].lower():
                    lines = self.swapStrings(lines, j, j + 1)
        self.writeLinesInFile(args.result, lines)

    def randomMixLines(self, args):
        file = open(args.source, 'r')
        lines = file.readlines()
        lines = self.deleteLinesDiveders(lines)
        file.close()
        for i in range(len(lines)):
            randomSwapIndex = random.randint(0, len(lines) - 1)
            lines = self.swapStrings(lines, i, randomSwapIndex)
        self.writeLinesInFile(args.result, lines)
