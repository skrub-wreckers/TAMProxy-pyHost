from .device import ContinuousReadDevice
from .. import config as c
import .analog_input import AnalogInput

class ShortIR(AnalogInput):

    DEVICE_CODE =   c.devices.ir.code
    READ_CODE =     c.devices.ir.read_code

    def __init__(self, tamproxy, pin, continuous=False):
        self.pin = pin
        self.val = 0
        self.dist = 0
        super(AnalogInput, self).__init__(tamproxy, continuous)

    def _handle_update(self, request, response):
        self.val = (ord(response[0])<<8) + ord(response[1])
        # Have some conversion in here for doing moving average to distance
