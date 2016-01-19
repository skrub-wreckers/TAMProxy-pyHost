from .device import ContinuousReadDevice
from .. import config as c
import .analog_input import AnalogInput

class LongIR(AnalogInput):

    DEVICE_CODE =   c.devices.analog_input.code
    READ_CODE =     c.devices.analog_input.read_code

    def __init__(self, tamproxy, pin, continuous=False):
        self.pin = pin
        self.val = 0
        self.dist = 0
        super(AnalogInput, self).__init__(tamproxy, continuous)

    def _handle_update(self, request, response):
        self.val = (ord(response[0])<<8) + ord(response[1])
        # Have some conversion in here for doing val to distance
