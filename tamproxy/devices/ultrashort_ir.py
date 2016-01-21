from .device import ContinuousReadDevice
from .. import config as c
from .digital_input import DigitalInput

class UltraShortIR(DigitalInput):
    def isClose(self):
        return self.val
