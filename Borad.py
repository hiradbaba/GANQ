class Chess:

    def createBoard(self,n):
        board = [[0 for i in range(n)] for j in range(n)]
        return board
    def __init__(self,n):
        self.board = self.createBoard(n)
        self.solutions = []
        self.size = n
        self.solutionCount = 0

    def isSafe(self,row,col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False
        for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
            if self.board[i][j] == 1:
                return False
        for i,j in zip(range(row,self.size,1),range(col,-1,-1)):
            if self.board[i][j] == 1:
                return False
        return True

    '''close enough to O(n!)'''
    def solveBackTracking(self,col):

        if col >= self.size:
            self.solutions.append(self.board)
            return True

        for i in range(self.size):
            if self.isSafe(i,col):
                self.board[i][col] = 1
                if self.solveBackTracking(col+1) == True:
                    return True

            self.board[i][col] = 0

        return False

    def getAllSolutions(self,col):

        if col >= self.size:
            self.solutions.append(self.board)
            self.solutionCount+=1
            # for row in self.board:
            #     print(row)
            # print("")
            return True

        solutionFound = False
        for i in range(self.size):
            if self.isSafe(i,col):
                self.board[i][col] = 1
                solutionFound = self.getAllSolutions(col+1)
            self.board[i][col] = 0

        return solutionFound


    def reportBackTrackingTime(self):
        from time import time
        start = time()
        self.solveBackTracking(0)
        end = time()
        with open("Single_BackTrackingResults.txt","a") as file:
            file.write(str(end-start)+"\n")

    def reportAllSolutionsTime(self):
        from time import time
        start = time()
        self.getAllSolutions(0)
        end = time()
        with open("All_BackTrackingResults.txt","a") as file:
            file.write(str(end-start)+"\n")


    def showBoardGui(self,board):
        import pygame
        pygame.init()
        colors = [(255,255,255), (100,100,100)]
        blue = (0,0,255)
        n = len(board[0])
        surfaceSize = 500
        squareSize = surfaceSize // n
        surfaceSize = n * squareSize
        surface = pygame.display.set_mode((surfaceSize, surfaceSize))
        while True:

            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break#;

            for row in range(n):
                colorIndex = row % 2
                for col in range(n):
                    square = (col*squareSize, row*squareSize, squareSize, squareSize)
                    if board[row][col] == 1:
                        surface.fill(blue,square)
                    else:
                        surface.fill(colors[colorIndex], square)
                    colorIndex = (colorIndex + 1) % 2


            pygame.display.flip()


        pygame.quit()


'''
-------- Solving the problem using genetic algorithm----------

'''
'''Genetic Chess'''
counter = 0
class GeneticChess:

    def __init__(self,n):
        self.board = self.createBoard(n)
        self.solutions = []
        self.size = n
        self.env = []
        self.goal = None
        self.goalIndex = -1


    def createBoard(self,n):
        board = [[0 for i in range(n)] for j in range(n)]
        return board

    def setBoard(self,board,gen):
        for i in range(self.size):
            board[gen[i]][i] = 1
    def genereteDNA(self):
        #genereates random list of length n
        from random import shuffle
        DNA = list(range(self.size))
        shuffle(DNA)
        while DNA in self.env:
            shuffle(DNA)
        return DNA

    def initializeFirstGenereation(self):
        for i in range(500):
            self.env.append(self.genereteDNA())

    def utilityFunction(self,gen):

        hits = 0
        board = self.createBoard(self.size)
        self.setBoard(board,gen)
        col = 0

        for dna in gen:
            try:
                for i in range(col-1,-1,-1):
                    if board[dna][i] == 1:
                        hits+=1
            except IndexError:
                print(gen)
                quit()
            for i,j in zip(range(dna-1,-1,-1),range(col-1,-1,-1)):
                if board[i][j] == 1:
                    hits+=1
            for i,j in zip(range(dna+1,self.size,1),range(col-1,-1,-1)):
                if board[i][j] == 1:
                    hits+=1
            col+=1
        return hits

    def isGoalGen(self,gen):
        if self.utilityFunction(gen) == 0:
            return True
        return False

    def crossOverGens(self,firstGen,secondGen):
        '''Approach #1'''
        # bound = self.size//2
        # for i in range(bound):
        #     firstGen[i],secondGen[i] = secondGen[i],firstGen[i]
        '''Approach #2'''
        for i in range(1,len(firstGen)):
            if abs(firstGen[i-1] - firstGen[i])<2:
                firstGen[i],secondGen[i] = secondGen[i],firstGen[i]
            if abs(secondGen[i-1] - secondGen[i])<2:
                firstGen[i],secondGen[i] = secondGen[i],firstGen[i]
        '''App1 + App2'''
        # isSwapped = False
        # for i in range(1,len(firstGen)):
        #     if abs(firstGen[i-1] - firstGen[i])<2:
        #         isSwapped = True
        #         firstGen[i],secondGen[i] = secondGen[i],firstGen[i]
        #     if abs(secondGen[i-1] - secondGen[i])<2:
        #         isSwapped = True
        #         firstGen[i],secondGen[i] = secondGen[i],firstGen[i]
        # if not isSwapped:
        #     bound = self.size//2
        #     for i in range(bound):
        #          firstGen[i],secondGen[i] = secondGen[i],firstGen[i]


    def MutantGen(self,gen):
        '''Approach #1'''
        # bound = self.size//2
        # from random import randint as rand
        # leftSideIndex = rand(0,bound)
        # RightSideIndex = rand(bound+1,self.size-1)
        # gen[leftSideIndex],gen[RightSideIndex] = gen[RightSideIndex],gen[leftSideIndex]
        # return gen
        '''Approach #2'''
        # from random import randint as rand
        # newGen = []
        # for dna in gen:
        #     if dna not in newGen:
        #         newGen.append(dna)
        # for i in range(self.size):
        #     if i not in newGen:
        #         # newGen.insert(rand(0,len(gen)),i)
        #         newGen.append(i)
        # gen = newGen
        # return gen
        '''Approach #3'''
        # from random import randint as rand
        # newGen = []
        # for dna in gen:
        #     if dna not in newGen:
        #         newGen.append(dna)
        # for i in range(self.size):
        #     if i not in newGen:
        #         inserted = False
        #         for j in range(len(newGen)):
        #             if abs(newGen[j] - i) >=2:
        #                 newGen.insert(j,i)
        #                 inserted = True
        #         if not inserted:
        #             newGen.append(i)
        # gen = []
        # for dna in newGen:
        #     if dna not in gen:
        #         gen.append(dna)

        # return gen
        '''Approach #4'''
        bound = self.size//2
        from random import randint as rand
        leftSideIndex = rand(0,bound)
        RightSideIndex = rand(bound+1,self.size-1)
        newGen = []
        for dna in gen:
            if dna not in newGen:
                newGen.append(dna)
        for i in range(self.size):
            if i not in newGen:
                # newGen.insert(rand(0,len(gen)),i)
                newGen.append(i)

        gen = newGen
        gen[leftSideIndex],gen[RightSideIndex] = gen[RightSideIndex],gen[leftSideIndex]
        return gen


    def crossOverAndMutant(self):
        for i in range(1,len(self.env),2):
            firstGen = self.env[i-1][:]
            secondGen = self.env[i][:]
            self.crossOverGens(firstGen,secondGen)
            firstGen = self.MutantGen(firstGen)
            secondGen = self.MutantGen(secondGen)
            self.env.append(firstGen)
            self.env.append(secondGen)

    def makeSelection(self):
        #index problem
        genUtilities = []
        newEnv = []

        for gen in self.env:
            genUtilities.append(self.utilityFunction(gen))
        if min(genUtilities) == 0:
            self.goalIndex = genUtilities.index(min(genUtilities))
            self.goal = self.env[self.goalIndex]
            return self.env
        minUtil=None
        while len(newEnv)<self.size:
            minUtil = min(genUtilities)
            minIndex = genUtilities.index(minUtil)
            newEnv.append(self.env[minIndex])
            genUtilities.remove(minUtil)
            self.env.remove(self.env[minIndex])

        return newEnv

    def solveGA(self):
        self.initializeFirstGenereation()
        for gen in self.env:
            if self.isGoalGen(gen):
                return gen
        count = 0
        while True:
            self.crossOverAndMutant()
            self.env = self.makeSelection()
            count +=1
            if self.goalIndex >= 0 :
                try:
                    print(count)
                    return self.goal
                except IndexError:
                    print(self.goalIndex)
            else:
                continue



    def reportGASolverTime(self):
        from time import time
        start = time()
        self.solveGA()
        end = time()
        with open("GA_report.txt","a") as file:
            file.write(str(end-start)+"\n")

    def showBoardGui(self,board):
        import pygame
        pygame.init()
        colors = [(255,255,255), (100,100,100)]
        blue = (0,0,255)
        n = len(board[0])
        surfaceSize = 500
        squareSize = surfaceSize // n
        surfaceSize = n * squareSize
        surface = pygame.display.set_mode((surfaceSize, surfaceSize))
        while True:

            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break;

            for row in range(n):
                colorIndex = row % 2
                for col in range(n):
                    square = (col*squareSize, row*squareSize, squareSize, squareSize)
                    if board[row][col] == 1:
                        surface.fill(blue,square)
                    else:
                        surface.fill(colors[colorIndex], square)
                    colorIndex = (colorIndex + 1) % 2


            pygame.display.flip()


        pygame.quit()
