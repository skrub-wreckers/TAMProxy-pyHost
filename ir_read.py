from tamproxy import Sketch, SyncedSketch, Timer
from tamproxy.devices import LongIR

# Detects changes in allllll the pins!

class IRRead(SyncedSketch):

    adc_pin = 4

    def setup(self):
        self.testpin = LongIR(self.tamp, self.adc_pin)
        self.timer = Timer()

    def loop(self):
        if self.timer.millis() > 100:
            self.timer.reset()
            print str(self.testpin.dist)

if __name__ == "__main__":
    sketch = IRRead(1, -0.00001, 100)
    sketch.run()