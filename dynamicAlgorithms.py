import dynamicLine 
import dynamicStar      

if __name__=="__main__":
   lineGraph = dynamicLine.Line(15000)
   lineGraph.constructGraph()
   lineGraph.getExcessedgeinLine()
   lineGraph.__str__()

   starGraph = dynamicStar.Star(16384) 
   starGraph.constructGraph()
