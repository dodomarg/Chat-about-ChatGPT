from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.TopoDS import TopoDS_Shape, TopoDS_Face, TopoDS_Wire
from OCC.BRepAlgoAPI import BRepAlgoAPI_Cut
from OCC.BRepBuilderAPI import (BRepBuilderAPI_MakeFace, BRepBuilderAPI_MakeEdge,
                                BRepBuilderAPI_MakeWire, BRepBuilderAPI_Transform)
from OCC.gp import gp_Trsf, gp_Pln, gp_Pnt, gp_Dir
from OCC.StlAPI import StlAPI_Writer, StlAPI_ErrorStatus
#from OCC.Display.SimpleGui import init_display


# Define the dimensions of the Arduino Uno and the enclosure
arduinoLength = 68.6
arduinoWidth = 53.4
enclosureThickness = 3.0

# Create the base of the enclosure using a box
base = BRepPrimAPI_MakeBox(arduinoLength, arduinoWidth, enclosureThickness)
enclosureBase = base.Shape()

# Create a face for the front panel of the enclosure
frontPanel = BRepBuilderAPI_MakeFace(gp_Pln(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1)), 0, arduinoWidth, 0, arduinoLength).Face()

# Create the opening for the Arduino's USB port by cutting a rectangular hole in the front panel
holeWidth = 6.5
holeHeight = 2.0
holeX = arduinoLength/2 - holeWidth/2
holeY = arduinoWidth/2 - holeHeight/2
hole = BRepPrimAPI_MakeBox(holeWidth, holeHeight, enclosureThickness + 1)
holeTransform = gp_Trsf()
holeTransform.SetTranslation(gp_Vec(holeX, holeY, 0))
holeMoved = BRepBuilderAPI_Transform(hole.Shape(), holeTransform)
holeShape = holeMoved.Shape()
cut = BRepAlgoAPI_Cut(frontPanel, holeShape)
frontPanel = TopoDS.Face(cut.Shape())

# Create the sides and back panel of the enclosure using the same method
leftPanel = BRepBuilderAPI_MakeFace(gp_Pln(gp_Pnt(0, 0, 0), gp_Dir(-1, 0, 0)), 0, arduinoWidth, 0, enclosureThickness).Face()
rightPanel = BRepBuilderAPI_MakeFace
rightPanel = BRepBuilderAPI_MakeFace(gp_Pln(gp_Pnt(arduinoLength, 0, 0), gp_Dir(1, 0, 0)), 0, arduinoWidth, 0, enclosureThickness).Face()
backPanel = BRepBuilderAPI_MakeFace(gp_Pln(gp_Pnt(0, 0, enclosureThickness), gp_Dir(0, 0, -1)), 0, arduinoLength, 0, arduinoWidth).Face()

# Assemble the enclosure by joining the individual panels together
frontWire = BRepBuilderAPI_MakeWire(BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeVertex(gp_Pnt(0, 0, 0)), BRepBuilderAPI_MakeVertex(gp_Pnt(0, arduinoWidth, 0))))
frontWire = BRepBuilderAPI_MakeWire(frontWire, BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeVertex(gp_Pnt(0, arduinoWidth, 0)), BRepBuilderAPI_MakeVertex(gp_Pnt(arduinoLength, arduinoWidth, 0))))
frontWire = BRepBuilderAPI_MakeWire(frontWire, BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeVertex(gp_Pnt(arduinoLength, arduinoWidth, 0)), BRepBuilderAPI_MakeVertex(gp_Pnt(arduinoLength, 0, 0))))
frontWire = BRepBuilderAPI_MakeWire(frontWire, BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeVertex(gp_Pnt(arduinoLength, 0, 0)), BRepBuilderAPI_MakeVertex(gp_Pnt(0, 0, 0))))
frontFace = BRepBuilderAPI_MakeFace(frontWire)
leftWire = BRepBuilderAPI_MakeWire(BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeVertex(gp_Pnt(0, 0, 0)), BRepBuilderAPI_MakeVertex(gp_Pnt(0, 0, enclosureThickness))))
leftWire = BRepBuilderAPI_MakeWire(leftWire, BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeVertex(gp_Pnt(0, 0, enclosureThickness)), BRepBuilderAPI_MakeVertex(gp_Pnt(0, arduinoWidth, enclosureThickness))))
leftWire = BRepBuilderAPI_MakeWire(leftWire, BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeVertex(gp_Pnt(0, arduinoWidth, enclosureThickness)), BRepBuilderAPI_MakeVertex(gp_Pnt(0, arduinoWidth, 0))))
leftWire = BRepBuilderAPI_MakeWire(leftWire, BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeVertex(gp_Pnt(0, arduinoWidth, 0)), BRepBuilderAPI_MakeVertex(gp_Pnt(0, 0, 0))))
leftFace = BRepBuilderAPI_MakeFace(leftWire)
rightWire = BRepBuilderAPI_MakeWire(rightWire, BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeVertex(gp_Pnt(arduinoLength, arduinoWidth, 0)), BRepBuilderAPI_MakeVertex(gp_Pnt(arduinoLength, arduinoWidth, enclosureThickness))))
rightWire = BRepBuilderAPI_MakeWire(rightWire, BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeVertex(gp_Pnt(arduinoLength, arduinoWidth, enclosureThickness)), BRepBuilderAPI_MakeVertex(gp_Pnt(arduinoLength, 0, enclosureThickness))))
rightWire = BRepBuilderAPI_MakeWire(rightWire, BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeVertex(gp_Pnt(arduinoLength, 0, enclosureThickness)), BRepBuilderAPI_MakeVertex(gp_Pnt(arduinoLength, 0, 0))))
rightFace = BRepBuilderAPI_MakeFace(rightWire)
backWire = BRepBuilderAPI_MakeWire(BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeVertex(gp_Pnt(0, 0, enclosureThickness)), BRepBuilderAPI_MakeVertex(gp_Pnt(arduinoLength, 0, enclosureThickness))))
backWire = BRepBuilderAPI_MakeWire(backWire, BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeVertex(gp_Pnt(arduinoLength, 0, enclosureThickness)), BRepBuilderAPI_MakeVertex(gp_Pnt(arduinoLength, arduinoWidth, enclosureThickness))))
backWire = BRepBuilderAPI_MakeWire(backWire, BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeVertex(gp_Pnt(arduinoLength, arduinoWidth, enclosureThickness)), BRepBuilderAPI_MakeVertex(gp_Pnt(0, arduinoWidth, enclosureThickness))))
backWire = BRepBuilderAPI_MakeWire(backWire, BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeVertex(gp_Pnt(0, arduinoWidth, enclosureThickness)), BRepBuilderAPI_MakeVertex(gp_Pnt(0, 0, enclosureThickness))))
backFace = BRepBuilderAPI_MakeFace(backWire)
enclosure = BRepBuilderAPI_MakeShell(frontFace).Shell()
enclosure = BRepBuilderAPI_MakeSolid(enclosure).Solid()
enclosure = BRepAlgoAPI_Cut(enclosure, BRepBuilderAPI_MakeSolid(backFace).Solid()).Shape()
enclosure = BRepAlgoAPI_Cut(enclosure, BRepBuilderAPI_MakeSolid(leftFace).Solid()).Shape()
enclosure = BRepAlgoAPI_Cut(enclosure, BRepBuilderAPI_MakeSolid(rightFace).Solid()).Shape()
enclosure = BRepAlgoAPI_Cut(enclosure, BRepBuilderAPI_MakeSolid(enclosureBase).Solid()).Shape()

stl_writer = StlAPI_Writer()
status = stl_writer.Write(enclosure, './output.stl')

if status == StlAPI_ErrorStatus.StlAPI_Error:
    print('Error exporting to STL file')
else:
    print('Successfully exported to STL file')
