from .device import Device, ContinuousReadDevice
from .. import config as c

class Odometer(Device):

    DEVICE_CODE =   c.devices.odometer.code
    WRITE_CODE =    c.devices.odometer.read_code

    def __init__(self, tamproxy, left_enc, right_enc, gyro, alpha):
        self.left_enc = left_enc
		self.right_enc = right_enc
		self.gyro = gyro
		self.alpha = alpha
		self.val = None
        super(Odometer, self).__init__(tamproxy)
        while self.id is None: pass

    @property
    def add_payload(self):
        return self.DEVICE_CODE + chr(self.left_enc) + chr(self.right_enc) + chr(self.gyro) + chr(self.alpha)

    def read(self):
        self.tamp.send_request(self.id,
                               self.READ_CODE, self.handle_request)
							   
	def handle_reading(self, request, response):
		self.val = response
