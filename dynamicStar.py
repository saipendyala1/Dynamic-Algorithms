import math
import matplotlib.pyplot as plt 

class Star:
  
   def __init__(self,graphSize):
        self.size = int(graphSize) 
        self.starGraph_dict   = {}
        self.totalSlots_Star  = []
        self.totalVertex_Star = []      
        self.totalExcessedges_Star = [] 

   def constructGraph(self):
      """
      constructs star graph of size 'n' in [log n] slots and identifies the excess edges in each slot for star graph and shows the time complexity of the graph construction
      """
      starNodes = [1]
      listOfnodes = []
      total_nodes = len(starNodes)
      print("--------------------------------------------------------------------")
      print("Star Graph Construction")
      for slot in range (1, (math.ceil(math.log(self.size, 2)) + 1)):
         nextNode = total_nodes + 1
         for vertex in starNodes:
            listOfnodes.append(vertex)
            if nextNode in range(1, self.size + 1):
               key = slot               
               if self.starGraph_dict.get(key) is None:
                  self.starGraph_dict[key] = []
               self.starGraph_dict[key].append(["u" + str(vertex), "u" + str(nextNode)])
               listOfnodes.append(nextNode)   
            nextNode += 1
         starNodes = listOfnodes
         total_nodes = len(starNodes)
         listOfnodes = listOfnodes.sort()
         listOfnodes = []          
         star = self.starGraph_dict[key]
         excessStaredges = []
         self.totalSlots_Star.append("t"+ str(key))
         for edge in star:
            if(edge[0] != "u1"):
              excessStaredges.append(edge)
         self.totalExcessedges_Star.append(len(excessStaredges))
         print("--------------------------------------------------------------------")
         print("\nExcess edges in star graph at slot t{}: ".format(key) , *(list("-->".join(map(str , xedge)) for xedge in excessStaredges)), sep= " || ")
         print()
         for edge in star:
            if(edge[0] != "u1"):
               center ="u1"
               edge[0] = center
         starGraph = list(sum(self.starGraph_dict[key], []))
         myGraph = starGraph
         if slot == "t" + str(len(self.starGraph_dict)):          
            myGraph.append("u" + str(self.size))
            myGraph = list(dict.fromkeys(myGraph))   
         for node in myGraph:
            if node == "u1":
               myGraph.remove(node)
         print( "New Nodes generated in slot " + "t"+str(slot)+ ': '+', '.join(map(str, myGraph)))
         print()
         print("Edges activated in star graph at slot t{}: ".format(key) , *(list("-->".join(map(str , graph)) for graph in star)), sep= " || ")
      print("------------------------------------------------------------------------")
      starResult = "\n Star construction schedule for graph size 'n'= {} ".format(self.size)
      print(starResult)
      print("---------------------------------------------------------------------------")
      for slot in self.starGraph_dict:
         print( "t"+str(slot) + ":", *(list("-->".join(map(str , graph)) for graph in self.starGraph_dict[slot])), sep= " || ")
         print("----------------------------------------------------------------------------")
      for node in range(1, (math.ceil(math.log(self.size, 2)) + 1)):
         self.totalVertex_Star.append(2**node)
      print( "excess edges:",self.totalExcessedges_Star)
      plt.plot(self.totalVertex_Star , self.totalSlots_Star)
      plt.ylabel('Time slots')
      plt.xlabel('Star graph size')
      plt.title('Complexity of Star Graph')
      plt.show()
      plt.plot(self.totalExcessedges_Star, self.totalVertex_Star)
      plt.ylabel('Size of the graph')
      plt.xlabel('Number of Excess edges')
      plt.title('Complexity of Excess edges in Star Graph')
      plt.show()
