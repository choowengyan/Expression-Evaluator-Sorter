from eval_expression import *
# from BinaryTree import BinaryTree
# from Stack import Stack

# open input file 

# inputFileName = input('Please enter input file: ')
# # outputFileName = input('Please enter output file: ')

# # read input file 
# inputFile =  open(inputFileName, 'r')
# # outputFile = open(outputFileName, 'w')

# for exp in inputFile:
#     print(exp)
    #buildParseTree(exp)
    # evaluate()

def openFile():
    while True: 
        try:
            inputFileName = input('Please enter input file: ')

            with open(inputFileName) as inputFile:
                for exp in inputFile:
                    print(exp)
                return False
                #print(inputFile.readlines())
        #error raised when an input/output operation fails
        except IOError:
            print('File not accessible, please try again')
            openFile()

# inputFile.close()
# outputFile.close()
openFile()