class TMS:
    
    def __init__(self, total, no, site, port, type, containerNum, size, chasisNum, pool, plate, seal, createdAt, dmg, truckNum, driverName, user, tires, tier, remark, repaired):
        
        self._total = total
        self._no = no
        self._site = site
        self._port = port
        self._type = type
        self._containerNum = containerNum
        self._size = size
        self._chasisNum = chasisNum
        self._pool = pool
        self._plate = plate
        self._seal = seal
        self._createdAt = createdAt
        self._dmg = dmg
        self._truckNum = truckNum
        self._driverName = driverName
        self._user = user
        self._tires = tires
        self._tier = tier
        self._remark = remark
        self._repaired = repaired

    # Getter Method
    @property
    def total(self):
        return self._total

    @property
    def no(self):
        return self._no

    @property
    def site(self):
        return self._site

    @property
    def port(self):
        return self._port

    @property
    def type(self):
        return self._type

    @property
    def containerNum(self):
        return self._containerNum

    @property
    def size(self):
        return self._size

    @property
    def chasisNum(self):
        return self._chasisNum

    @property
    def pool(self):
        return self._pool

    @property
    def plate(self):
        return self._plate

    @property
    def seal(self):
        return self._seal

    @property
    def createdAt(self):
        return self._createdAt

    @property
    def time(self):
        return self._time
        
    @property
    def dmg(self):
        return self._dmg

    @property
    def truckNum(self):
        return self._truckNum

    @property
    def driverName(self):
        return self._driverName

    @property
    def user(self):
        return self._user

    @property
    def tires(self):
        return self._tires

    @property
    def tier(self):
        return self._tier

    @property
    def remark(self):
        return self._remark

    @property
    def repaired(self):
        return self._repaired

    # Setter Method
    @total.setter
    def total(self, value):
        self._total=value

    @no.setter
    def no(self, value):
        self._no=value

    @site.setter
    def site(self, value):
        self._site=value

    @port.setter
    def port(self, value):
        self.port = value

    @type.setter
    def type(self, value):
        self._type = value

    @containerNum.setter
    def containerNum(self, value):
        self._containerNum = value

    @size.setter
    def size(self, value):
        self._size = value

    @chasisNum.setter
    def chasisNum(self, value):
        self._chasisNum = value

    @pool.setter
    def pool(self, value):
        self._pool = value

    @plate.setter
    def plate(self, value):
        self._plate = value

    @seal.setter
    def seal(self, value):
        self._seal = value

    @createdAt.setter
    def createdAt(self, value):
        self._createdAt = value

    @time.setter
    def time(self, value):
        self._time = value
        
    @dmg.setter
    def dmg(self, value):
        self._dmg = value

    @truckNum.setter
    def truckNum(self, value):
        self._truckNum = value

    @driverName.setter
    def driverName(self, value):
        self._driverName = value
    
    @user.setter
    def user(self, value):
        self._user = value

    @tires.setter
    def tires(self, value):
        self._tires = value

    @tier.setter
    def tier(self, value):
        self._tier = value

    @remark.setter
    def remark(self, value):
        self._remark = value

    @repaired.setter
    def repaired(self, value):
        self._repaired = value