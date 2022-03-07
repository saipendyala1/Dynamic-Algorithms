import math
import matplotlib.pyplot as plt 

class Line:        

   def __init__(self,graphSize):
        self.size = int(graphSize)        
        self.lineGraph_dict   = {}
        self.excessEdges_Line = {}
        self.totalExcessEdges_Line = []
        self.totalSlots_Line  = []
        self.totalVertex_Line = []
  
   def constructGraph(self):
      """
      Generates construction schedule of line graph of size 'n' in [log n] slots
      """
      lineNodes    = [1]
      listofVertex = []
      for slot in range (1, (math.ceil(math.log(self.size, 2)) + 1)):
        for vertex in lineNodes:
            listofVertex.append(vertex)
            nextNode =  vertex + math.ceil(self.size/(2 ** slot))
            if nextNode in range(1, self.size + 1):
               key = "t" + str(slot)
               if self.lineGraph_dict.get(key) is None:
                  self.lineGraph_dict[key] = []
               self.lineGraph_dict[key].append(("u" + str(vertex), "u" + str(nextNode)))
               listofVertex.append(nextNode)
        self.totalSlots_Line.append(key)
        lineNodes = listofVertex
        listofVertex = []      

   def getExcessedgeinLine(self):
      """
      Identifies the excess edges for each time-slot in the line graph
      """
      schedule = ""
      for slot in self.lineGraph_dict:  
        if self.excessEdges_Line.get(slot) is None:
            self.excessEdges_Line[slot] = []
        if len(schedule) == 0:
           schedule = slot 
           continue
        exEdge_list = list(self.excessEdges_Line)
        try:
          res = exEdge_list[exEdge_list.index(schedule) + 1]
        except (ValueError, IndexError):
          res = None
        graph = self.lineGraph_dict[schedule]
        prev = ()
        for edge in graph:
            current = edge 
            if ((len(prev) != 0) and (prev[1] == current[0])) or (len(prev) == 0) :
               prev = current
               continue
            edge = (prev[1] , current[0])
            self.excessEdges_Line[res].append((edge))
            prev = current
        excessEdge = self.excessEdges_Line[schedule]
        for xEdge in excessEdge:
         self.excessEdges_Line[slot].append((xEdge))   
        for round in graph:
         self.excessEdges_Line[slot].append((round))    
        schedule = slot

   def __str__(self):
      lineResult = "\nLine construction schedule for graph length 'n'= {} ".format(self.size)
      print(lineResult)
      print("---------------------------------------------------------------------------")
      for slot in self.lineGraph_dict:
         line = list(sum(self.lineGraph_dict[slot], ()))
         myGraph = line
         if slot == "t" + str(len(self.lineGraph_dict)):
            myGraph.append("u" + str(self.size))
         myGraph = list(dict.fromkeys(myGraph))
         print(slot+ ': '+' -- '.join(map(str, myGraph)))
      print('---------------------------------------------------------------------------')
      for round in self.excessEdges_Line:
         excessEdges = len(self.excessEdges_Line[round])
         self.totalExcessEdges_Line.append(excessEdges)
         print("Excess edges in line graph at slot " + round + ': ', *(("".join(map(str , xedge)) for xedge in self.excessEdges_Line[round])), sep= " -- ")             
         print("Number of excess edges in line graph :" , len(self.excessEdges_Line[round]), '\n')
         print("---------------------------------------------------------------------------")
      for node in range(1, (math.ceil(math.log(self.size, 2)) + 1)):
         self.totalVertex_Line.append(2**node)
      plt.plot(self.totalVertex_Line , self.totalSlots_Line)
      plt.ylabel('Time slots')
      plt.xlabel('Size of the Line graph')
      plt.title('Complexity of Line Graph')
      plt.show()
      plt.plot(self.totalExcessEdges_Line, self.totalVertex_Line)
      plt.ylabel('size of the graph')
      plt.xlabel('Number of Excess edges')
      plt.title('Complexity of Excess edges in line Graph')
      plt.show()
