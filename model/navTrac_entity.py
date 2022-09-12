class NavTrack:
    
    def __init__(self, total, direction, createdAt, detectedAt, updatedAt, hasSeal, loadId, gateId, sealNumber, hasReeferUnit,load, vehicle, chassis, imagePath):        
        self._direction = direction
        self._total = total
        self._createdAt = createdAt
        self._detectedAt = detectedAt
        self._updatedAt = updatedAt
        self._hasSeal = hasSeal
        self._loadId = loadId
        self._gateId = gateId
        self._sealNumber = sealNumber
        self._hasReeferUnit = hasReeferUnit
        self._load = load
        self._vehicle = vehicle
        self._chassis = chassis
        self._imagePath = imagePath

    # Getter Method
    @property
    def direction(self):
        return self._direction

    @property
    def total(self):
        return self._total

    @property
    def createdAt(self):
        return self._createdAt

    @property
    def detectedAt(self):
        return self._detectedAt

    @property
    def updatedAt(self):
        return self._updatedAt

    @property
    def hasSeal(self):
        return self._hasSeal

    @property
    def loadId(self):
        return self._loadId

    @property
    def gateId(self):
        return self._gateId

    @property
    def sealNumber(self):
        return self._sealNumber

    @property
    def hasReeferUnit(self):
        return self._hasReeferUnit

    @property
    def load(self):
        return self._load

    @property
    def vehicle(self):
        return self._vehicle
        
    @property
    def chassis(self):
        return self._chassis

    @property
    def imagePath(self):
        return self._imagePath

    # Setter Method
    @direction.setter
    def direction(self, value):
        self._direction=value

    @createdAt.setter
    def createdAt(self, value):
        self.createdAt = value

    @detectedAt.setter
    def detectedAt(self, value):
        self._detectedAt = value

    @updatedAt.setter
    def updatedAt(self, value):
        self._updatedAt = value

    @hasSeal.setter
    def hasSeal(self, value):
        self._hasSeal = value

    @loadId.setter
    def loadId(self, value):
        self._loadId = value

    @gateId.setter
    def gateId(self, value):
        self._gateId = value

    @sealNumber.setter
    def sealNumber(self, value):
        self._sealNumber = value

    @hasReeferUnit.setter
    def hasReeferUnit(self, value):
        self._hasReeferUnit = value

    @load.setter
    def load(self, value):
        self._load = value

    @vehicle.setter
    def vehicle(self, value):
        self._vehicle = value
        
    @chassis.setter
    def chassis(self, value):
        self._chassis = value

    @imagePath.setter
    def imagePath(self, value):
        self._imagePath = value

    @total.setter
    def total(self, value):
        self._total = value