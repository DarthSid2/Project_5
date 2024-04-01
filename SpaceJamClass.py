from panda3d.core import * 
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Vec3
from direct.task import Task
from collideObjectBase import * 
from typing import Callable

class Universe(ShowBase):
    def __init__ (self, loader: Loader, modelPath: str, parentNode: NodePath, NodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
    
        self.modelNode.setName(modelPath)
        tex = loader. loadTexture(texPath)
        self.modelNode.setTexture(tex, 1 )


class Planets(ShowBase):
    
    def __init__ (self, loader: Loader, modelPath: str, parentNode: NodePath, NodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
    
        self.modelNode.setName(modelPath)
        tex = loader. loadTexture(texPath)
        self.modelNode.setTexture(tex, 1 )    

class Drones(ShowBase):
    droneCount = 0 
   
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1) 

class increment():
    Increment = 0            

class SpaceStation(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
    
class SpaceShip_1(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        self.taskManager = self.taskMgr()
        self.SetkeyBindings()


    def Thrust(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyThrust, 'Forward-thrust')
        else:
            self.taskManager.remove('Forward-thrust')

    def ApplyThrust(self, task):
        rate = 7
        trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
        return Task.cont

    def SetkeyBindings(self):
        self.accept("space", self.Thrust, [1])
        self.accept("space-up", self.Thrust, [0])
        self.accept("a", self.LeftTurn, [1])
        self.accept("a-up", self.LeftTurn, [0])
        self.accept("d", self.RightTurn, [1])
        self.accept("d-up", self.RightTurn, [0])
        self.accept("w", self.LookUp, [1])
        self.accept("w-up", self.LookUp, [0])
        self.accept("s", self.LookDown, [1])
        self.accept("s-up", self.LookDown, [0])
        self.accept("e", self.RollLeft, [1])
        self.accept("e-up", self.RollLeft [0])
        self.accept("q", self.RollRight, [1])
        self.accept("q-up", self.RollRight, [0])
        
    
    def RightTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRightTurn, 'Right-turn')

        else:
            self.taskManager.remove('Right-turn')

    def ApplyLeftTurn(self, task):
        rate = .7
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont        

    def LeftTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLeftTurn, 'Left-turn')

        else:
            self.taskManager.remove('Left-turn')           

    def ApplyRightTurn(self, task):
        rate = .7
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont        

    def LookUp(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLookUp, 'Look-Up')

        else:
            self.taskManager.remove('Look-Up')

    def ApplyLookUp(self, task):
        rate = .7
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont        

    def LookDown(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLookDown, 'Look-Down')

        else:
            self.taskManager.remove('Look-Down')

    def ApplyLookDown(self, task):
        rate = .7
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont 

    def RollLeft(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRollLeft, 'Roll-Left')

        else:
            self.taskManager.remove('Roll-Left')

    def ApplyRollLeft(self, task):
        rate = .7
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont

    def RollRight(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRollRight, 'Roll-Right')

        else:
            self.taskManager.remove('Roll-Right')

    def ApplyRollRight(self, task):
        rate = .7
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont                           








class yz():
    circleIncrement = 0

class xy():
     circleIncrement = 0

class xz():
    circleIncrement = 0
