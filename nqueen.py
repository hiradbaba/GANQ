from Borad import Chess,GeneticChess
import tkinter
from tkinter import *
from tkinter import ttk
'''Single BackTracking -------------------------------'''
# dimension = int(input("Enter board dimension: "))
# chess = Chess(dimension)

# chess.solveBackTracking(0)
# for solution in chess.solutions:
#     for row in solution:
#         print(row)
#     print("")

# chess.showBoardGui(solution)
'''All solutions backtracking------------------------------'''
# dimension = int(input("Enter board dimension: "))
# chess = Chess(dimension)

# chess.getAllSolutions(0)
# print(chess.solutionCount)

'''Single BackTracking report --------------------------------'''
# with open("Single_BackTrackingResults.txt","r+") as file:
#     file.truncate(0)
#     file.close()
# for i in range(4,29):
#     chess = Chess(i)
#     chess.reportBackTrackingTime()
#     print("dimension "+str(i)+" completed")
'''All solutions BackTracking report --------------------------------'''
# with open("All_BackTrackingResults.txt","r+") as file:
#     file.truncate(0)
#     file.close()
# for i in range(4,25):
#     chess = Chess(i)
#     chess.reportAllSolutionsTime()
#     print("dimension "+str(i)+" completed")
'''GA report------------------------------------------------'''
# with open("GA_report.txt","r+") as file:
#     file.truncate(0)
#     file.close()
# for i in range(4,70):
#     chess = GeneticChess(i)
#     chess.reportGASolverTime()
#     print("dimension "+str(i)+" completed")
'''Single GA solution ---------------------------------'''
dimension = int(input("Enter board dimension: "))
chess = GeneticChess(dimension)
from time import time
start = time()
solution = chess.solveGA()
end =time()
board = chess.createBoard(chess.size)
chess.setBoard(board,solution)
print("Solution:")
print(solution)
# print("\nBoard:")
# for row in board:
#     print(row)
print(end - start)
# chess.showBoardGui(board)





'''/---------------------------------------/
  /-------------GRAPHICAL APP-------------/
 /---------------------------------------/
'''
def solveProblem():
    if choice.get() == 1:
        chess = Chess(int(n.get()))
        chess.solveBackTracking(0)
        solution = chess.solutions[0]
        for solution in chess.solutions:
            for row in solution:
                print(row)
            print("")
        chess.showBoardGui(solution)
    elif choice.get() == 2:
        chess = GeneticChess(int(n.get()))
        solution = chess.solveGA()
        board = chess.createBoard(chess.size)
        chess.setBoard(board,solution)
        print("Solution:")
        print(solution)
        # print("\nBoard:")
        # for row in board:
        #     print(row)
        chess.showBoardGui(board)
        
    return

# window = Tk()
# window.wm_title("HX N queen solver")

# l = Label(window,text="Dimension:")
# l.grid(row=0,column=0)

# n = StringVar()
# e1 = Entry(window,textvariable = n)
# e1.grid(row=0,column=1)

# solver = ttk.Button(window,text="Solve",width=8,command=solveProblem)
# solver.grid(row=1,column=2)
# choice = tkinter.IntVar()
# back = tkinter.Radiobutton(window, 
#               text="Backtracking",
#               indicatoron =0,
#               width=11,
#               padx = 20, 
#               variable=choice, 
#               value=1)
# ga = tkinter.Radiobutton(window, 
#               text="Genetic",
#               indicatoron =0,
#               width=11,
#               padx = 20, 
#               variable=choice, 
#               value=2)
# back.grid(row=1,column=1)
# ga.grid(row=2,column=1)



# window.mainloop()

