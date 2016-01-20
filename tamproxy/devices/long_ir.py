from .device import ContinuousReadDevice
from .. import config as c

class LongIR(ContinuousReadDevice):

    DEVICE_CODE =   c.devices.ir.code
    READ_CODE =     c.devices.ir.code

    def __init__(self, tamproxy, pin, continuous=True):
        self.pin = pin
        self.dist = 0
        super(LongIR, self).__init__(tamproxy, continuous)

    @property
    def add_payload(self):
        return self.DEVICE_CODE + chr(self.pin)

    def _handle_update(self, request, response):
        self.dist = (ord(response[0])<<8) + ord(response[1])
        # Have some conversion in here for doing moving average to distance
