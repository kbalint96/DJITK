from DJITK import Tello

"""
        1. feladat - Szotar letrehozasa es tesztelse

        a) commandsDict szotar kiegeszitese
        b) testDict fuggveny kiegeszitese es tesztelese
        c) doDict fuggveny vizsgalata
"""

class DJITK_patrols(Tello):

    # 1) a - commandsDict szotar kiegeszitese
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
        "wifi?": "wifi?"
    }

    # 1) b/1 - testDict fuggveny kiegeszitse
    def testDict(self, myCommand):
        """
        A fuggveny megvizsgalja, hogy a kapott, ertek nelkuli parancs torzs (fel, le, balra stb)
        szerepel-e a szotarban
        :param myCommand: ertek nelkuli parancs torzs
        """
        for x in self.commandsDict.keys():
            if self.commandsDict[x] == myCommand:
                print x

    # 1) c - doDict fuggveny vizsgalata
    def doDict(self, myCommand):
        """
        A fuggveny megvizsgalja, hogy a parameterkent kapott parancs szerepel-e a szotarban, valamint hogy
        az szabalyos-e (argumentumok szama)
        :param myCommand: forditani kivant parancs
        :return:
            - 1, ha nem sikeres a forditas / nem megfelelo a formatum
            - "command", ha egy reszes parancsot forditottunk
            - "command value", ha tobb reszes parancsot forditottunk
        """

        """ Fuggvenyben hasznald valtozok inicializalasa"""
        # lista, amelybe szetszedjuk a ket parameteres parancsokat (command + value)
        commands = []
        # a Tello szamara kuldott parancs
        command = ""
        # es annak erteke
        value = ""
        # taroljuk el, hogy a kapott parancs szabalyos-e
        commandOk = False

        """ Kapott parancs formai kovetelmenyeinek vizsgalata """
        # amennyiben parameterkent kapott parancs ket reszbol all (pl. "elore 10")
        if len(myCommand.split()) > 1:
            commands = myCommand.split()
            # a commands listank masodik ertekenek mentsuk el a kapott parancs masodik erteket
            # a parancs szabalyossagat a kesobbekben vizsgaljuk
            value = commands[1]
        # amennyiben a kapott parancs tobb, mint ket reszbol all, ervenytelennek tekintjuk
        elif len(myCommand.split()) > 2:
            print "Ismeretlen parancs, tul sok argumentum!"
        # ha a kapott parancs egyreszes, csak rakjuk azt bele a tombbe
        else:
            commands = [myCommand]

        """ Kapott parancs keresese a szotarunkban """
        # nezzuk meg, hogy az ertek (pl. elore ..., balra ...) megtalalhato-e a szotartban
        # ha igen, a command valtozoba mentsuk el a szotarunk erteket (SDK parancsot),
        # es nyugtazzuk a parancsunk szabalyossagat a commandOk valtozo allitasaval
        for x in self.commandsDict.keys():
            if x == commands[0]:
                command = commands[0]
                commandOk = True

        # elofordulhat azonban, hogy paramterkent mar az eredeti SDK parancsot kapjuk meg, igy
        # ha az elozo vizsgalat soran nem talaltuk meg a parancsot, vizsgaljuk meg, hogy
        # a kapott paramter megtalalhato-e a a szotar kulcsai kozt
        # ha igen, a command valtozoba mentsuk el a szotarunk kulcsat (SDK parancsot),
        # es nyugtazzuk a parancsunk szabalyossagat a commandOk valtozo allitasaval
        if not commandOk:
            for x in self.commandsDict.keys():
                if self.commandsDict[x] == commands[0]:
                    command = x
                    commandOk = True

        """ SDK parancs ellenorzese """
        # ha sikerult a parancs leforditasa
        if commandOk:
            # es a parancs tobb, mint egy reszbol all
            if len(commands) == 2:
                # de a parancs szerepel az egy reszes parancsok kozt, hibat dobunk es return 1
                if command in self.oneWord:
                    print "[" + command + "] Egy argumentumot var! Kapott: [" + command + " " + value + "]"
                    return -1
                # ha nincs benne, visszaadjuk a forditott parancsot es az erteket (pl. forward 10)
                else:
                    return command + " " + value
            # ha a parancs egy reszbol all
            else:
                # de a parancs nem szerepel az egy reszes parancsok kozt, hibat dobunk es return 1
                if command not in self.oneWord:
                    print "[" + command + "] Ket argumentumot var! Vart formatum: [" + command + " 20]"
                    return -1
                # ha benne van, visszadjuk a forditott parancsot (pl. takeoff)
                else:
                    return command
        # amennyiben nem sikeult parancsot forditani, hibat dobunk es return 1
        else:
            print "[" + commands[0] + "] Nem ertelmezheto parancs!"
            return -1

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

    def doStack(self, myStack):
        commands = []

        if len(myStack) == 0:
            print ("Ures parancshalmaz!")
            exit()

        for command in range(len(myStack), 0, -1):
            if self.doDict(myStack[command]) != 1:
                commands.append(self.doDict(myStack[command]))
            else:
                exit()
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


DJITKPatrol3 = DJITK_patrols("Course3")
DJITKPatrol3.doInit()

# 1) b/1 - testDict() fuggveny tesztelese
DJITKPatrol3.testDict("felszall")
DJITKPatrol3.testDict("felszall 30")
DJITKPatrol3.testDict("elore")
DJITKPatrol3.testDict("elore 50")
DJITKPatrol3.testDict("ismeretlen")

"""
        2. feladat - Queue parancs atadas

        a) Queue segitsegevel L alak bejarasa
        b) commandsQueue atadasa a doQueue fuggvenynek es
"""

# 2) a - Queue feltoltese parancsokkal
commandsQueue = ["felszall", "elore 100", "balrafordul 90", "elore 20",
                 "balrafordul 90", "elore 70", "jobbrafordul 90", "elore 40",
                 "balrafordul 90", "elore 30", "balrafordul 90", "elore 70", "balrafordul 90", "land"]

# 2) b - doQueue() fuggveny tesztelese a commandsQueue-val
DJITKPatrol3.doQueue(commandsQueue)

"""
        3. feladat - Stack parancs atadas

        a) Teszt: commandsQueue atadasa a doStack fuggvenynek! Mit tapasztalsz?
        b) Stack segitsegevel irj egy tetszoleges utasitas sorozatot! Add at a doStack fuggvenynek!
        c) Vizsgald meg kiirt szenzor adatokat. Mit tapasztalsz?
"""

# 3) a - doStack() fuggveny tesztelese a commandsQueue-vel
DJITKPatrol3.doStack(commandsQueue)

# 3) b - Stack segitsegevel tetszolges utasitas sorozat
# L alak bejarasa visszafele
DJITKPatrol3.takeOff()
commandsStack = ["battery?", "elore 100", "battery?", "jobbrafordul 90", "battery?",
                 "elore 20", "battery?", "jobbrafordul 90", "battery?", "elore 70", "battery?",
                 "balrafordul 90", "battery?", "elore 40", "battery?", "jobbrafordul 90", "battery?",
                 "elore 30", "battery?", "jobbrafordul 90", "battery?", "elore 70", "battery?",
                 "jobbrafordul 90", "battery?"]
DJITKPatrol3.land()


