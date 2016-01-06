from six import int2byte
from .device import Device
from .. import config as c

class AnalogOutput(Device):

    DEVICE_CODE =   c.devices.analog_output.code
    WRITE_CODE =    c.devices.analog_output.write_code

    def __init__(self, tamproxy, pin):
        self.pin = pin
        super (AnalogOutput, self).__init__(tamproxy)
        while self.id is None: pass

    @property
    def add_payload(self):
        return self.DEVICE_CODE + int2byte(self.pin)

    def write(self, value):
        self.tamp.send_request(self.id,
                               self.WRITE_CODE + 
                               int2byte((int(value) >> 8) & 0xFF) + 
                               int2byte(int(value) & 0xFF))
