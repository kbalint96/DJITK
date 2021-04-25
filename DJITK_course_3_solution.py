from DJITK import Tello

class DJITK_patrols(Tello):

    commandsDict = {
        "up": "fel",
        "down": "le",
        "left": "balra",
        "right": "jobbra",
        "forward": "elore",
        "back": "hatra",
        "cw": "balrafordul",
        "ccw": "jobbrafordul",
        "flip": "pordul",
        "takeoff": "felszall",
        "land": "leszall",
        "speed?": "sebesseg?",
        "battery?": "akkumulator?",
        "time?": "ido?",
        "wifi?": "wifi?",
    }

    def doDict(self, myCommand):

        oneWord = ["takeoff", "land"]

        commands = []
        command = ""
        value = ""
        commandOk = False

        if len(myCommand.split()) > 1:
            commands = myCommand.split()
            value = commands[1]
        elif len(myCommand.split()) > 2:
            print "Ismeretlen parancs, tul sok argumentum!"
        else:
            commands = [myCommand]

        for x in self.commandsDict.keys():
            if self.commandsDict[x] == commands[0]:
                command = x
                commandOk = True

        if not commandOk:
            for x in self.commandsDict.keys():
                if x == commands[0]:
                    command = commands[0]
                    commandOk = True

        if commandOk:
            if len(commands) > 1:
                if command in oneWord:
                    print "[" + command + "] Egy argumentumot var! Kapott: [" + command + " " + value + "]"
                    return 1
                else:
                    return command + " " + value
            else:
                if command not in oneWord:
                    print "[" + command + "] Ket argumentumot var! Vart formatum: [" + command + " 20]"
                    return 1
                else:
                    return command
        else:
            print "[" + commands[0] + "] Nem ertelmezheto parancs!"
            return 1

    def doQueue(self, myQueue):

        commands = []

        if len(myQueue) == 0:
            print ("Ures parancshalmaz!")
            exit()

        for command in myQueue:
            if self.doDict(command) != 1:
                commands.append(self.doDict(command))
            else:
                exit()

        print (">> Parancsok beolvasasa sikeres")
        print commands
        print (">> Parancsok vegrehajtasa...")

        for command in commands:
            self.do(command)

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


commandsQueue = ["takeOff", "elore 50", "back 20", "land"]

dron = DJITK_patrols("kurzus3")
dron.doInit()
dron.doQueue(commandsQueue)

