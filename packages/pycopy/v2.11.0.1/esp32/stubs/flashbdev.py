"""
Module: 'flashbdev' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v2.11.0.1 on 2019-07-26', machine='ESP32 module with ESP32')
# Stubber: 1.2.0

class FlashBdev:
    ''
    SEC_SIZE = 4096
    START_SEC = 512
    def ioctl():
        pass

    def readblocks():
        pass

    def writeblocks():
        pass

bdev = None
esp = None
size = 4194304
