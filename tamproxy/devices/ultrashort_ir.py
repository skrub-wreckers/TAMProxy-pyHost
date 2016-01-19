from .device import ContinuousReadDevice
from .. import config as c
from .digital_input import DigitalInput

class UltraShortIR(DigitalInput):

    DEVICE_CODE =   c.devices.digital_input.code
    READ_CODE =     c.devices.digital_input.read_code

    def __init__(self, tamproxy, pin, pullup=True, continuous=False):
        self.pin = pin
        self.pullup = pullup
        self.val = 0
        self.prev_val = None
        super(DigitalInput, self).__init__(tamproxy, continuous)

    def isClose(self):
        return self.val
