import sys
import argparse
import FileWorker

class Parser:

    def createParser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-s', '--source', required = True, 
        help = 'file with source data', metavar = 'write [name_of_file].[extension] to start work')
        parser.add_argument('-r', '--result', required = True,
        help = 'file with result data', metavar = 'write [name_of_file].[extension] to start work')
        parser.add_argument('-o', '--output', help = 'output data of source and result files', action='store_true')
        parser.add_argument('-al', '--ascendingLength', help = 'sorts lines from the source file by ' + 
        'their lengthes in ascending order and write them to result file', action='store_true')
        parser.add_argument('-dl', '--descendingLength', help = 'sorts lines from the source file by ' + 
        'their lengthes in descending order and write them to result file', action='store_true')
        parser.add_argument('-aw', '--ascendingWords', help = 'sorts lines from the source file by ' + 
        'alphabet in ascending order and write them to result file', action='store_true')
        parser.add_argument('-dw', '--descendingWords', help = 'sorts lines from the source file by ' + 
        'alphabet in descending order and write them to result file', action='store_true')
        parser.add_argument('-m', '--mix', help = 'mixes lines from the source file in random order ' + 
        'and writes them to the result file', action='store_true')
        return parser

    def parseCommandLine(self):
        fileWorker = FileWorker.FileWorker()
        parser = self.createParser()
        args = parser.parse_args(sys.argv[1:])
        for i in sys.argv:
            print(i)
        print(args)
        fileWorker.writeDataInFile(args)
        for arg in sys.argv[5:]:
            print(arg)
            if arg == '-o' or arg == '--output':
                print('Output files:\n')
                fileWorker.outputFiles(args)
            elif arg == '-al' or arg == '--ascendingLength':
                print('Sorting strings by their lengths in ascending order\n')
                fileWorker.sortLinesByLengthInAscendingOrder(args)
                fileWorker.outputFiles(args)
            elif arg == '-dl' or arg == '--descendingLength':
                print('Sorting strings by their lengths in descending order\n')
                fileWorker.sortLinesByLengthInDescendingOrder(args)
                fileWorker.outputFiles(args)
            elif arg == '-aw' or arg == '--ascendingWords':
                print('Sorting strings by alphabet in ascending order\n')
                fileWorker.sortLinesByAlphabetInAscendingOrder(args)
                fileWorker.outputFiles(args)
            elif arg == '-dw' or arg == '--descendingWords':
                print('Sorting strings by alphabet in descending order\n')
                fileWorker.sortLinesByAlphabetInDescendingOrder(args)
                fileWorker.outputFiles(args)
            elif arg == '-m' or arg == '--mix':
                fileWorker.randomMixLines(args)
                fileWorker.outputFiles(args)
            else:
                print('Wrong argument of command string\n')
