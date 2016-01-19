from .device import Device, ContinuousReadDevice
from .. import config as c

import struct

class Odometer(ContinuousReadDevice):

    DEVICE_CODE =   c.devices.odometer.code
    READ_CODE =    c.devices.odometer.read_code

    def __init__(self, tamproxy, left_enc, right_enc, gyro, alpha):
        self.left_enc = left_enc
        self.right_enc = right_enc
        self.gyro = gyro
        self.alpha = alpha
        self.val = 0
        super(Odometer, self).__init__(tamproxy, continuous=False)

    def __repr__(self):
        return super(Odometer, self).__repr__(
            self.left_enc,
            self.right_enc,
            self.gyro,
            alpha=self.alpha)

    @property
    def add_payload(self):
        return self.DEVICE_CODE + (
            chr(self.left_enc.id) +
            chr(self.right_enc.id) +
            chr(self.gyro.id) +
            chr(self.alpha.id)
        )

    def read(self):
        self.tamp.send_request(self.id,
                               self.READ_CODE, self.handle_request)

    def _handle_update(self, request, response):
        self.val = struct.unpack('!f', response)[0]
