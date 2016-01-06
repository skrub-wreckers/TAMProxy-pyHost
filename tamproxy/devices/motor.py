from six import int2byte

from .device import Device
from .. import config as c

class Motor(Device):

    DEVICE_CODE =   c.devices.motor.code
    WRITE_CODE =    c.devices.motor.write_code

    def __init__(self, tamproxy, dir_pin, pwm_pin):
        self.dir_pin = dir_pin
        self.pwm_pin = pwm_pin
        super(Motor, self).__init__(tamproxy)
        while self.id is None: pass

    @property
    def add_payload(self):
        return self.DEVICE_CODE + int2byte(self.dir_pin) + int2byte(self.pwm_pin)

    def write(self, direction, pwm):
        self.tamp.send_request(self.id,
                               self.WRITE_CODE + 
                               int2byte(direction > 0) + 
                               int2byte((int(pwm) >> 8) & 0xFF) + 
                               int2byte(int(pwm) & 0xFF))
