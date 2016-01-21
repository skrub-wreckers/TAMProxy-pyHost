from .device import ContinuousReadDevice
from .. import config as c

class LongIR(ContinuousReadDevice):

    DEVICE_CODE =   c.devices.ir.code
    READ_CODE =     c.devices.ir.code

    TOO_FAR_TICKS = 9000
    # Tick range where need to double check with ultrashort IR
    AMBIGUOUS_TICKS_LOW = 22000
    AMBIGUOUS_TICKS_HIGH = 47000
    DISCONNECTED = 56000

    def __init__(self, tamproxy, pin, continuous=True):
        self.pin = pin
        self.distTicks = 0
        self.distInches = 0
        super(LongIR, self).__init__(tamproxy, continuous)

    @property
    def add_payload(self):
        return self.DEVICE_CODE + chr(self.pin)

    def _handle_update(self, request, response):
        self.distTicks = (ord(response[0])<<8) + ord(response[1])
        # Set cutoff of where can't really tell values well
        if self.distTicks < self.TOO_FAR_TICKS:
            self.distInches = "far"
        elif self.distTicks > self.DISCONNECTED:
            self.distInches = "disconnected"
        else:
            # Trendline for converting ticks to inches found experimentally
            self.distInches = 407924 * pow(self.distTicks, -1.0675)
            # if self.distTicks > 25000 :
            #     self.distInches = -0.0002 * self.distTicks + 12.4
            # elif self.distTicks > 16000 :
            #     self.distInches = -0.0005 * self.distTicks + 21.3
            # else:
            #     self.distInches = -0.001 * self.distTicks + 31.8
