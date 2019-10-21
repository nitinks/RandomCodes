# 
# Generates random mac addresses from a given start till valid count.
# Mac addresses can be allocated on request uniquely.
# They can be free'd and checked for usage.
# 

# Global imports.
import netaddr, random
class ListDB:
    def __init__(self):
        self.allocatedMacs = None

    def initialiseDB(self):
        self.allocatedMacs = []

    def NotExhausted(self, count):
        if len(self.allocatedMacs) < count-1:
            return True
        return False

    def Contains(self, macVal):
        if mac in self.allocatedMacs:
            return True
        return False

    def Remove(self, macVal):
        self.allocatedMacs.pop(macVal)

    def Add(self, macVal):
        self.allocatedMacs.append(macVal)

class MacDatabase:
    """
    Interface class.
    This uses a underlying database object, interfaces that with MacAddrGen object.
    The DB can be a simple list, Dictionary, file or regular database.
    """
    def __init__(self, startMac, macCount):
        self.DB = ListDB()
        self.DB.initialiseDB()

        self.startMac = startMac
        self.macCount = macCount

    def __contains__(self, mac):
        if self.DB.Contains(mac):
            return True
        return False

    def Free(self, mac):
        macVal = int(EUI(self.startMac)) - int(EUI(mac))
        self.DB.Remove(macVal)

    def Allocate(self, mac):
        macVal = int(EUI(self.startMac)) - int(EUI(mac))
        self.DB.Add(macVal)

    def GetMacAddr(self):
        # Generate a random number between 0 - macCount.
        if not self.DB.NotExhausted():
            return None

        # Find and allocate a random number of unallocated mac address.
        rand = 0

        while True:
            rand = random.randint(0,self.macCount)
            if self.DB.Contains(rand):
                continue

            self.DB.Add(rand)
            break

        allocatedMacVal = int(EUI(self.startMac)) + rand

        # Convert this mac integer value into Mac address.
        allocatedMacXex = "{:012x}".format(allocatedMacVal)
        allocatedMac = ":".join(allocatedMacXex[i:i + 2] \
                                for i in range(0, len(allocatedMacXex), 2))

        return allocatedMac


class MacAddrGen:
    def __init__(self, startMac, macCount):
        """
        Initialize the object.
        :param start: string notation for first mac address.
        :param count: Number of mac addresses to be maintained.
        """
        self.startMac = startMac
        self.macCount = macCount

        if self.macCount <= 0:
            raise Exception ("Not possible to issue mac addresses in this range")

        if netaddr.valid_mac(self.startMac):
            raise Exception ("Not a valid mac address")

        self.EnsureMacsAvailable(self.startMac, self.macCount)

        self.macDB = MacDatabase(self, self.startMac, self.macCount)

    def EnsureMacsAvailable(self, startMac, macCount):
        """
        Check to ensure we have sufficient mac addresses available from the mac address start.
        :param startMac: Mac from where to start allocating.
        :param macCount: number of mac addresses required.
        :return: Raise if failed.
        """
        macMax = EUI('ff-ff-ff-ff-ff-ff')
        macStart = EUI(self.startMac)

        if (int(macMax) - int(macStart)) < self.macCount:
            raise Exception ("Dont have enough mac count from mac start")

    def IsAllocatted(self, mac):
        """
        Check if this mac is allocated.
        :param mac:
        :return:
        """
        if mac in self.macDB:
            return True
        return False

    def IsFree(self, mac):
        """
        Check is the mac is free.
        :param mac:
        :return:
        """
        if mac not in self.macDB:
            return True
        return False

    def Free(self, mac):
        """
        Release a mac addressed.
        :param mac:
        :return:
        """
        if self.IsAllocatted(mac):
            self.macDB.Free(mac)
        else:
            pass
            # Handle freeing up a already freed mac address.

    def Allocate(self, mac):
        if self.IsFree(mac):
            self.macDB.Allocate(mac)

        else:
            pass
            # Handle allocating a already used mac address.

    def IssueMac(self):
        return self.macDB.GetMacAddr()
