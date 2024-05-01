# Note! this is not a Factory pattern, we need to reimplement it
# Factory class should create new instances based on their type
class EQsFactory:
    def __init__(self):
        # define protected Set property of classes
        # it is like a class/object attributes
        # they are inherited by subclasses and instances
        self._eqsfactory = {
            FabFilter(5, "Pro Q"),
            UAD(4, "UAD"),
            Waves(10, "Waves")
        }

    # define a decorator method to return class/instance property
    @property
    def eqs(self):
        return self._eqsfactory


class EQ:
    # the "init" function is called when the instance is created and ready to be initialized
    # bands and name are attributes of an object
    def __init__(self, bands, name):
        # define private property of an instance:
        self.bands = bands
        self.name = name

    def getBands(self):
        return self.bands

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def setBands(self, bands):
        self.bands = bands


class FabFilter(EQ):
    def __init__(self, bands, name):
        super().__init__(bands, name)

    def getBands(self):
        return super().getBands()


class Waves(EQ):
    def __init__(self, bands, name):
        super().__init__(bands, name)

    def getBands(self):
        return super().getBands()


class UAD(EQ):
    def __init__(self, bands, name):
        super().__init__(bands, name)

    def getBands(self):
        return super().getBands()
