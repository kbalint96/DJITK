from DJITK import Tello

"""
    1. feladat - Sajat DJITK_demo dron osztaly letrehozasa

    a) hozz letre egy DJITK ososztalybol orokolt DJITK_demo osztalyt!
    b) hozz letre egy DJITK_demo peldanyt DJITKDemo neven!
    c) Peldanyositas utan hivd meg a sajat osztalyodon keresztul az ososztaly nehany fuggvenyet!

"""


# 1) a - DJITK_demo osztaly letrehozasa!

class DJITK_demo(Tello):
    pass


# 1) b - DJITK_c2 peldanyositasa
""" INNENTOL """

""" EDDIG """

# 1) c - ososztaly fuggvenyinek hivasa
""" INNENTOL """

""" EDDIG """

"""
    2. feladat - Hozd letre es alakitsd egyedive az orokoltetett osztalyodat!

    a) hozd letre a sajat dron osztalyodat ,a DJITK ososztalybol orokoltetve
    b) implementald osztalyszinten a kurzus elso orajan megirt Custompatrol() metodust, vagy
    c) implementalj legalabb ket peldanymetodust!
"""


class DJITK_patrols(Tello):
    def customPatrol(self, edge):
        pass
        """ INNENTOL """

        """ EDDIG """

    # a dron egy radius sugaru korben emelkedik height magassagig
    def spiral(self, height, radius):
        pass
        """ INNENTOL """

        """ EDDIG """

    # a dron egy nyolcas alakzatot jar be
    def eighty(self):
        pass
        """ INNENTOL """

        """ EDDIG """

    # a dron egy L alakot jar be
    def formL(self):
        pass
        """ INNENTOL """

        """ EDDIG """

    # a dron elore es hatra megy
    def backAndForth(self, length):
        pass
        """ INNENTOL """

        """ EDDIG """

    """
        3. feladat - Hozd letre az osztalyod valtozoihoz szukseges getter es setter fuggvenyeket!

        a) mode valtozo, valamint a hozza tartozo getter es setter
        b) modositsd a modnak megfeleloen a sebesseget a mod settereben!
        c) fuggveny segitsegevel jarj be ugy egy negyzetet, hogy az oldalait kulonbozo modban teszed meg!

    """

    # 3) a
    # mode valtozo letrehozasa
    """ INNENTOL """

    """ EDDIG """

    # mode getter, getMode()
    """ INNENTOL """

    """ EDDIG """

    def setMode(self, newMode):
        if newMode in ("Eco", "Normal", "Turbo"):
            # peldanyunk mode valtozojanak frissitese
            """ INNENTOL """

            """ EDDIG """
            # 3) b - mode getter es sebesseg beallitas
            """ INNENTOL """

            """ EDDIG """
        else:
            print ">> Mod nem megfelelo!"

    # 3) c - negyzet bejarasa kulonbozo modokban
    def squareModes(self, lenght):
        pass
        """ INNENTOL """

        """ EDDIG """


# foprogram, peldany letrahozasa, parancsok kiadasa
""" INNENTOL """

""" EDDIG """

