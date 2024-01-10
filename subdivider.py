import random

class Cube:
    
    def __init__(self, ownerComp):
        clear()
        self.ownerComp = ownerComp
        self.dat = op("../table_pos")
        self.ranList = [i for i in range(500)]
        List = random.shuffle(self.ranList)
        print(self.ranList)
        
        print('Cube has init')
        
        
    def Subdivider(self, iterations = 150, delete = 100, index = 0):
        

        def getPoints(center = [0,0,0], pscale = 1):
            
            # pscale = 1
            scale = pscale * 2
            # center = [0,0,0]
            p0 = [center[0] + pscale, center[1] + pscale, center[2] + pscale, scale]
            p1 = [center[0] + pscale, center[1] + pscale, center[2] - pscale, scale]
            p2 = [center[0] + pscale, center[1] - pscale, center[2] + pscale, scale]
            p3 = [center[0] + pscale, center[1] - pscale, center[2] - pscale, scale]
            p4 = [center[0] - pscale, center[1] + pscale, center[2] + pscale, scale]
            p5 = [center[0] - pscale, center[1] + pscale, center[2] - pscale, scale]
            p6 = [center[0] - pscale, center[1] - pscale, center[2] + pscale, scale]
            p7 = [center[0] - pscale, center[1] - pscale, center[2] - pscale, scale]
            listofPoints = [p0, p1, p2, p3, p4, p5, p6, p7]
            
            
            return listofPoints

        listofPoints = getPoints(center = [0,0,0], pscale = 1)



        def subdivide(listofPoints, index = index):
            
            # sort listofPoints by pscale from big to small
            listofPoints.sort(key=lambda x: x[3], reverse=True)

            # select a random point in list listofPoints           
            nPoint = listofPoints[index]
            nPscale = nPoint[3] * .25    
            # remove index from list listofPoints
            listofPoints.pop(index)
            newList = getPoints(nPoint, nPscale)

            final = listofPoints + newList
        
            return final

        for i in range(iterations):
            
            try :
                listofPoints = subdivide(listofPoints, index = self.ranList[i])
            except:
                nindex = 0
                
                listofPoints = subdivide(listofPoints, index = nindex)


        for i in range(delete):
            
            # sort listofPoints by pscale from big to small
            listofPoints.sort(key=lambda x: x[3], reverse=True)
            
            # select a random point in list listofPoints
            #random select 1 point in the 10% first index
                        
            index = random.randint(0, int(len(listofPoints)*.1))
            # index = random.randint(0, len(listofPoints)-1)
            listofPoints.pop(index)



        return [listofPoints, self.ranList]
