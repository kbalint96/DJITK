from DJITK import Tello

class DJITK_patrols(Tello):

    commandsDict = {
        "up": "fel",
        "down": "le",
        "left": "balra",
        "right": "",
        "forward": "",
        "back": "",
        "cw": "",
        "ccw": "",
        "flip": "",
        "takeoff": "",
        "land": "",
        "speed?": "",
        "battery?": "",
        "time?": "",
        "wifi?": "",
    }

    def testDict(self, myCommand):
        """
        A fuggveny megvizsgalja, hogy a kapott, ertek nelkuli parancs torzs (fel, le, balra stb)
        szerepel-e a szotarban
        :param myCommand: ertek nelkuli parancs torzs
        """
        # iteraljunk vegig a szotarunkon. x lesz a kulcsunk
        for x in self.commandsDict.keys():
            # amennyiben a kulcsunk megegyezik a parameterben kapott myCommand-dal, irjuk ki a kulcsot
            if "---":
                print "---"
            # egyebkent dobjunk hibat
            else:
                print "Parancs nem talalhato!"

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
        # ebben a listaban taroljuk az egyszavas parancsokat
        oneWord = ["takeoff", "land"]
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
        # ha igen, a command valtozoba mentsuk el a szotarunk kulcsat (SDK parancsot),
        # es nyugtazzuk a parancsunk szabalyossagat a commandOk valtozo allitasaval
        for x in self.commandsDict.keys():
            if self.commandsDict[x] == commands[0]:
                command = x
                commandOk = True

        # elofordulhat azonban, hogy paramterkent mar az eredeti SDK parancsot kapjuk meg, igy
        # ha az elozo vizsgalat soran nem talaltuk meg a parancsot, vizsgaljuk meg, hogy
        # a kapott paramter megtalalhato-e a a szotar kulcsai kozt
        # ha igen, a command valtozoba mentsuk el a szotarunk kulcsat (SDK parancsot),
        # es nyugtazzuk a parancsunk szabalyossagat a commandOk valtozo allitasaval
        if not commandOk:
            for x in self.commandsDict.keys():
                if x == commands[0]:
                    command = commands[0]
                    commandOk = True

        """ SDK parancs ellenorzese """
        # ha sikerult a parancs leforditasa
        if commandOk:
            # es a parancs tobb, mint egy reszbol all
            if len(commands) > 1:
                # de a parancs szerepel az egy reszes parancsok kozt, hibat dobunk es return 1
                if command in oneWord:
                    print "[" + command + "] Egy argumentumot var! Kapott: [" + command + " " + value + "]"
                    return 1
                # ha nincs benne, visszaadjuk a forditott parancsot es az erteket (pl. forward 10)
                else:
                    return command + " " + value
            # ha a parancs egy reszbol all
            else:
                # de a parancs nem szerepel az egy reszes parancsok kozt, hibat dobunk es return 1
                if command not in oneWord:
                    print "[" + command + "] Ket argumentumot var! Vart formatum: [" + command + " 20]"
                    return 1
                # ha benne van, visszadjuk a forditott parancsot (pl. takeoff)
                else:
                    return command
        # amennyiben nem sikeult parancsot forditani, hibat dobunk es return 1
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

