from DJITK import Tello

"""
---===================================DJITK utasitaskeszlet===============================-
    DJITKDrone.doInit()                 >> Kapcsolat inicializalasa a Telloval
    DJITKDrone.getBattery()             >> akkumulator szint lekerdezese [%]
    DJITKDrone.getSpeed()               >> sebesseg/rotor teljesitmeny lekerdezese [%]
    DJITKDrone.getTime()                >> repulesi ido lekerdezese [s]
    DJITKDrone.getWifiSNR()             >> WiFi erosseg lekerdezese [%]
    DJITKDrone.getSdk()                 >> Tello SDK verzio lekerdezese
    DJITKDrone.getSn()                  >> Tello szeriaszam lekerdezese
    DJITKDrone.takeOff()                >> Felszallas, majd lebeges
    DJITKDrone.land()                   >> Leszallas
    DJITKDrone.stop()                   >> Veszhelyzet hajtomu leallitas
    DJITKDrone.move("left", 30)         >> Mozgas (up, down, left, right, forward, back), cm
    DJITKDrone.rotate("right", 180)     >> Fordulas (left, right), fordulasi szog
    DJITKDrone.flip("forward")          >> Porges (left, right, foward, back)

---========================================FELADATOK======================================-

    1. feladat - valtozok es tipusok
    a) Hozz letre harom valtozot, amelyben taroljuk a dronunk
        - nevet                  (name)
        - orjarat hosszusagat    (edge)
        - inicializalas allapoat (isInit)
    b) Adj erteket a valtozoidnak!

"""

# 1) a, b - A valtozok deklaralasa
""" INNENTOL """
name = "balint"
""" EDDIG """

# SOL - Dron peldanyunk letrehozasa
DJITKDrone = Tello(name)

"""
    2. feladat - feltetelek es ciklusok
    a)  Ha a dron inicializalva van, ird ki azt a konzolra, ha nincs, inicializald az doInit() fuggvennyel
    b)  Jarj be a dronnal egy 50cm oldalu negyzetet!
    c)  Miutan bejartad a negyzetet, szervezd ciklusba az utasitasaidat ugy, hogy ezt negyszer tegye meg!
    d)  Modositsd a programot ugy, hogy a fenti utasitasokat addig hajsd vegre, amig az akkumulator
        50% felett van!
"""
# 2) a
""" INNENTOL """

""" EDDIG """

# 2) b hasznald a fenti utasitasokat, es ne felejts el fel- valamint leszallni!
""" INNENTOL """

""" EDDIG """

# 2) c
""" INNENTOL """

""" EDDIG """

# 2) d
""" INNENTOL """

""" EDDIG """

"""
    3. feladat - eljarasok
    a)  Szervezd fuggvenybe az elozo feladatban implementalt orjarat utasitassorozatot!
    b)  Modositsd ezt a fuggvenyt ugy, hogy a bejart negyzet oldala parameterbol valtoztathato legyen!
    +1) Irj egy sajat repulesi sorozatot. Figyelj! A fuggvenynek van eleje es vege!
"""

# 3) a
""" INNENTOL """

""" EDDIG """

# 3) b
""" INNENTOL """

""" EDDIG """

# 3) c - Ide definialj egy sajat fuggvenyesittett utasitassorozatot. Hasznald a fenti utasitasokat!
""" INNENTOL """

""" EDDIG """