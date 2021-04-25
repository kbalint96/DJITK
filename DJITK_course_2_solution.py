from DJITK import Tello

"""
    1. feladat - Sajat DJITK_demo dron osztaly letrehozasa

    a) hozz letre egy DJITK ososztalybol orokolt DJITK_demo osztalyt!
    b) hozz letre egy DJITK_demo peldanyt DJITKDemo neven!
    c) Peldanyositas utan hivd meg a sajat osztalyodon keresztul az ososztaly nehany fuggvenyet!

"""

# 1) a - DJITK_demo osztaly letrahozasa!

class DJITK_demo(Tello):
    pass

# 1) b - DJITK_c2 peldanyositasa
name = "DemoDrone"
DJITKDemo = DJITK_demo(name)

# 1) c - ososztaly fuggvenyinek hivasa
DJITKDemo.doInit()
DJITKDemo.takeOff()
DJITKDemo.move("up", 50)
DJITKDemo.land()


"""
    2. feladat - Hozd letre es alakitsd egyedive az orokoltetett osztalyodat!

    a) hozd letre a sajat dron osztalyodat ,a DJITK ososztalybol orokoltetve
    b) implementald osztalyszinten a kurzus elso orajan megirt Custompatrol() metodust, vagy
    c) implementalj legalabb ket peldanymetodust!
"""

class DJITK_patrols(Tello):

    def customPatrol(self, edge):
        self.takeOff()
        for edges in range(4):
            self.move("forward", edge)
            self.rotate("left", 90)
        self.land()

    def spiral(self, height, radius):
        # @TODO, ha van ertelme - spriralt jar be felfele
        pass

    def eighty(self):
        # @TODO, ha van ertelme - nyolcast jar be
        pass

    def formL(self):
        # @TODO, ha van ertelme - L alakot jar be
        pass

    def backAndForth(self, length):
        self.takeOff()
        self.move("forward", length)
        self.move("back", length)
        self.land()

    """
        3. feladat - Hozd letre az osztalyod valtozoihoz szukseges getter es setter fuggvenyeket!

        a) mode valtozo, valamint a hozza tartozo getter es setter
        b) modositsd a modnak megfeleloen a sebesseget a mod settereben!
        c) fuggveny segitsegevel jarj be ugy egy negyzetet, hogy az oldalait kulonbozo modban teszed meg!

    """

    # 3) a - mode getter es setter
    mode = "Normal"

    def getMode(self):
        return self.mode

    def setMode(self, newMode):
        if newMode in ("Eco", "Normal", "Turbo"):
            self.mode = newMode
    # 3) b - mode getter es sebesseg beallitas
            if newMode == "Eco":
                self.setSpeed(25)
            elif newMode == "Normal":
                self.setSpeed(60)
            elif newMode == "Turbo":
                self.setSpeed(100)
        else:
            print ">> Mod nem megfelelo!"

    # 3) c - negyzet bejarasa kulonbozo modokban
    def squareModes(self, lenght):
        self.takeOff()
        self.move("up", 100)

        self.setMode("Eco")
        self.move("forward", lenght)
        self.rotate("left", 90)

        self.setMode("Normal")
        self.move("forward", lenght)
        self.rotate("left", 90)

        self.setMode("Turbo")
        self.move("forward", lenght)
        self.rotate("left", 90)

        self.move("forward", lenght)
        self.rotate("left", 90)

        self.land()

DJITKPatrol = DJITK_patrols("Orzovedo")
DJITKPatrol.doInit()
DJITKPatrol.squareModes(150)

