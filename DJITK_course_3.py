from DJITK import Tello

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

    mode = "Normal"

    def getMode(self):
        return self.mode

    def setMode(self, newMode):
        if newMode in ("Eco", "Normal", "Turbo"):
            self.mode = newMode
            if newMode == "Eco":
                self.setSpeed(25)
            elif newMode == "Normal":
                self.setSpeed(60)
            elif newMode == "Turbo":
                self.setSpeed(100)
        else:
            print ">> Mod nem megfelelo!"

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



