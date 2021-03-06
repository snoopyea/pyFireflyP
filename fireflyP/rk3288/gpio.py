#!/usr/bin/env python

from fireflyP.lib.devmem import MapReg
from fireflyP.lib.common import cons_list

import pdb
import logging

# GPIO iomux registers
class RegMux:
	GRF_GPIO0A_IOMUX	=0x0084
	GRF_GPIO0B_IOMUX	=0x0088
	GRF_GPIO0C_IOMUX	=0x008c

	GRF_GPIO1D_IOMUX    =0x000c

	GRF_GPIO2A_IOMUX    =0x0010
	GRF_GPIO2B_IOMUX    =0x0014
	GRF_GPIO2C_IOMUX    =0x0018

	GRF_GPIO3A_IOMUX    =0x0020
	GRF_GPIO3B_IOMUX    =0x0024
	GRF_GPIO3C_IOMUX    =0x0028
	GRF_GPIO3DL_IOMUX   =0x002c
	GRF_GPIO3DH_IOMUX   =0x0030

	GRF_GPIO4AL_IOMUX   =0x0034
	GRF_GPIO4AH_IOMUX   =0x0038
	GRF_GPIO4BL_IOMUX   =0x003c
	GRF_GPIO4C_IOMUX    =0x0044
	GRF_GPIO4D_IOMUX    =0x0048

	GRF_GPIO5B_IOMUX    =0x0050
	GRF_GPIO5C_IOMUX    =0x0054

	GRF_GPIO6A_IOMUX    =0x005c
	GRF_GPIO6B_IOMUX    =0x0060
	GRF_GPIO6C_IOMUX    =0x0064

	GRF_GPIO7A_IOMUX    =0x006c
	GRF_GPIO7B_IOMUX    =0x0070
	GRF_GPIO7CL_IOMUX   =0x0074
	GRF_GPIO7CH_IOMUX   =0x0078

	GRF_GPIO8A_IOMUX    =0x0080
	GRF_GPIO8B_IOMUX    =0x0084

# GPIO slew rate control registers
class RegSlew:
	GRF_GPIO1H_SR           =0x0104
	GRF_GPIO2L_SR           =0x0108
	GRF_GPIO2H_SR           =0x010c
	GRF_GPIO3L_SR           =0x0110
	GRF_GPIO3H_SR           =0x0114
	GRF_GPIO4L_SR           =0x0118
	GRF_GPIO4H_SR           =0x011c
	GRF_GPIO5L_SR           =0x0120
	GRF_GPIO5H_SR           =0x0124
	GRF_GPIO6L_SR           =0x0128
	GRF_GPIO6H_SR           =0x012c
	GRF_GPIO7L_SR           =0x0130
	GRF_GPIO7H_SR           =0x0134
	GRF_GPIO8L_SR           =0x0138

# GPIO pull up/pull down registers
class RegPull:
	GRF_GPIO0A_P            =0x0064
	GRF_GPIO0B_P            =0x0068
	GRF_GPIO0C_P            =0x006c

	GRF_GPIO1D_P            =0x014c

	GRF_GPIO2A_P            =0x0150
	GRF_GPIO2B_P            =0x0154
	GRF_GPIO2C_P            =0x0158

	GRF_GPIO3A_P            =0x0160
	GRF_GPIO3B_P            =0x0164
	GRF_GPIO3C_P            =0x0168
	GRF_GPIO3D_P            =0x016c

	GRF_GPIO4A_P            =0x0170
	GRF_GPIO4B_P            =0x0174
	GRF_GPIO4C_P            =0x0178
	GRF_GPIO4D_P            =0x017c

	GRF_GPIO5B_P            =0x0184
	GRF_GPIO5C_P            =0x0188

	GRF_GPIO6A_P            =0x0190
	GRF_GPIO6B_P            =0x0194
	GRF_GPIO6C_P            =0x0198

	GRF_GPIO7A_P            =0x01a0
	GRF_GPIO7B_P            =0x01a4
	GRF_GPIO7C_P            =0x01a8

	GRF_GPIO8A_P            =0x01b0
	GRF_GPIO8B_P            =0x01b4

# GPIO drive strength control registers
class RegDrv:
	GRF_GPIO0A_E            =0x0070
	GRF_GPIO0B_E            =0x0074
	GRF_GPIO0C_E            =0x0078

	GRF_GPIO1D_E            =0x01cc
	
	GRF_GPIO2A_E            =0x01d0
	GRF_GPIO2B_E            =0x01d4
	GRF_GPIO2C_E            =0x01d8

	GRF_GPIO3A_E            =0x01e0
	GRF_GPIO3B_E            =0x01e4
	GRF_GPIO3C_E            =0x01e8
	GRF_GPIO3D_E            =0x01ec

	GRF_GPIO4A_E            =0x01f0
	GRF_GPIO4B_E            =0x01f4
	GRF_GPIO4C_E            =0x01f8
	GRF_GPIO4D_E            =0x01fc

	GRF_GPIO5B_E            =0x0204
	GRF_GPIO5C_E            =0x0208

	GRF_GPIO6A_E            =0x0210
	GRF_GPIO6B_E            =0x0214
	GRF_GPIO6C_E            =0x0218

	GRF_GPIO7A_E            =0x0220
	GRF_GPIO7B_E            =0x0224
	GRF_GPIO7C_E            =0x0228

	GRF_GPIO8A_E            =0x0230
	GRF_GPIO8B_E            =0x0234

# GPIO control registers
class RegCtrl:
    GPIO_SWPORT_DR     =0x00
    GPIO_SWPORT_DDR    =0x04
    GPIO_INTEN         =0x30
    GPIO_INTMASK       =0x34
    GPIO_INTTYPE_LEVEL =0x38
    GPIO_INT_POLARITY  =0x3c
    GPIO_INT_STATUS    =0x40
    GPIO_INT_RAWSTATUS =0x44
    GPIO_DEBOUNCE      =0x48
    GPIO_PORTS_EOI     =0x4c
    GPIO_EXT_PORT      =0x50
    GPIO_LS_SYNC       =0x60

class GpioLevel:
    LOW = 0
    HIGH = 1

class GpioDir:
    INPUT = 0
    OUTPUT = 1

class GpioMux:
	MUX_GPIO	=0
	MUX_1		=1
	MUX_2		=2
	MUX_3		=3
	MUX_4		=4
	MUX_5		=5
	MUX_6		=6
	MUX_7		=7

class GpioPull:
	NORAML		=0
	UP			=1
	DOWN		=2
	BUS_HOLD	=3

class GpioDrv:
	E_2MA		=0
	E_4MA		=1
	E_8MA		=2
	E_12MA	    =3

BANK={
	'GPIO0':0,
	'GPIO1':1,
	'GPIO2':2,
	'GPIO3':3,
	'GPIO4':4,
	'GPIO5':5,
	'GPIO6':6,
	'GPIO7':7,
	'GPIO8':8,
}

PIN={
    'A0': 0,    'A1': 1,    'A2': 2,    'A3': 3,    'A4': 4,    'A5': 5,    'A6': 6,    'A7': 7,
    'B0': 8,    'B1': 9,    'B2':10,    'B3':11,    'B4':12,    'B5':13,    'B6':14,    'B7':15,
    'C0':16,    'C1':17,    'C2':18,    'C3':19,    'C4':20,    'C5':21,    'C6':22,    'C7':23,
    'D0':24,    'D1':25,    'D2':26,    'D3':27,    'D4':28,    'D5':29,    'D6':30,    'D7':31,
}

class Bank:
    def __init__(self, ctrl, iomux, pull, drv):
        self.ctrl   = ctrl
        self.iomux  = iomux
        self.pull   = pull
        self.drv    = drv

    def __str__(self):
        return '\nctrl\t%s\niomux\t%s\npull\t%s\ndrv\t%s' % (self.ctrl, self.iomux, self.pull, self.drv)
    __repr__ = __str__

class Gpio(GpioLevel, GpioDir, GpioMux, GpioPull, GpioDrv):
    _inited = 0

    @staticmethod
    def _set_mapreg(mapname, addr, size):
        mr=MapReg(mapname, addr, size)
        setattr(Gpio, '_' + mapname, mr)

    @staticmethod
    def init():
        """
        Init GPIO function
        implement it before using Gpio
        """
        if Gpio._inited > 0:
            logging.error("Gpio have inited!")
            return None
        Gpio._inited = 1

        Gpio._set_mapreg('gpio0_ctrl',0xff750000,0x100)
       #Gpio._set_mapreg('gpio0_iomux',0xff730084,0x0c)
       #Gpio._set_mapreg('gpio0_pull',0xff730064,0x0c)
       #Gpio._set_mapreg('gpio0_drv',0xff730070,0x0c)
       #Gpio._set_mapreg('gpio18_iomux',0xff770000,0x140)
       #Gpio._set_mapreg('gpio18_pull',0xff770140,0x80)
       #Gpio._set_mapreg('gpio18_drv',0xff7701c0,0x80)
        Gpio._set_mapreg('gpio0_base',0xff730000,0x7c)
        Gpio._set_mapreg('gpio18_base',0xff770000,0x240)

        Gpio._set_mapreg('gpio1_ctrl',0xff780000,0x100)
        Gpio._set_mapreg('gpio2_ctrl',0xff790000,0x100)
        Gpio._set_mapreg('gpio3_ctrl',0xff7a0000,0x100)
        Gpio._set_mapreg('gpio4_ctrl',0xff7b0000,0x100)
        Gpio._set_mapreg('gpio5_ctrl',0xff7c0000,0x100)
        Gpio._set_mapreg('gpio6_ctrl',0xff7d0000,0x100)
        Gpio._set_mapreg('gpio7_ctrl',0xff7e0000,0x100)
        Gpio._set_mapreg('gpio8_ctrl',0xff7f0000,0x100)
        Gpio._set_mapreg('gpio15_ctrl',0xff7f2000,0x100)

        Gpio._regs= {
            "GPIO0": 
                Bank(Gpio._gpio0_ctrl, Gpio._gpio0_base, Gpio._gpio0_base, Gpio._gpio0_base),
            "GPIO1": 
                Bank(Gpio._gpio1_ctrl, Gpio._gpio18_base, Gpio._gpio18_base, Gpio._gpio18_base),
            "GPIO2": 
                Bank(Gpio._gpio2_ctrl, Gpio._gpio18_base, Gpio._gpio18_base, Gpio._gpio18_base),
            "GPIO3": 
                Bank(Gpio._gpio3_ctrl, Gpio._gpio18_base, Gpio._gpio18_base, Gpio._gpio18_base),
            "GPIO4": 
                Bank(Gpio._gpio4_ctrl, Gpio._gpio18_base, Gpio._gpio18_base, Gpio._gpio18_base),
            "GPIO5": 
                Bank(Gpio._gpio5_ctrl, Gpio._gpio18_base, Gpio._gpio18_base, Gpio._gpio18_base),
            "GPIO6": 
                Bank(Gpio._gpio6_ctrl, Gpio._gpio18_base, Gpio._gpio18_base, Gpio._gpio18_base),
            "GPIO7": 
                Bank(Gpio._gpio7_ctrl, Gpio._gpio18_base, Gpio._gpio18_base, Gpio._gpio18_base),
            "GPIO8": 
                Bank(Gpio._gpio8_ctrl, Gpio._gpio18_base, Gpio._gpio18_base, Gpio._gpio18_base),
        }
    @staticmethod
    def exit():
        Gpio._inited = 0
        pass

    def __init__(self, gpio):
        self.gpio = gpio

        sbank = gpio[:5]
        self.bank = BANK[sbank]
        self.pin = PIN[gpio[5:]]
        self._regs = Gpio._regs[sbank]

    def __str__(self):
        return self.gpio

    def __repr__(self):
        return '%s: bank=%d, pin=%d\n%s' % (self.gpio, self.bank, self.pin, self._regs)


    def set_dir(self, dir):
        """
        set GPIO direction
        :dir: refer to GpioDir
        """
        logging.debug("set_dir: set <%s>=%d" % (self.gpio, dir))
        assert dir in cons_list(GpioDir)

        self.set_mux(GpioMux.MUX_GPIO)   #set iomux=gpio default

        reg = self._regs.ctrl
        val = reg.read(RegCtrl.GPIO_SWPORT_DDR)
        val &= (~(1<<self.pin))
        val |= (dir<<self.pin)
        reg.write(RegCtrl.GPIO_SWPORT_DDR, val)

    def get_level(self):
        """
        Returns the level of the pin for input direction
        or return setting of the DR register for output gpios.
        """

        reg = self._regs.ctrl
        val = reg.read(RegCtrl.GPIO_EXT_PORT)
        val >>=self.pin
        val &=1
        logging.debug("get_level: <%s>=%d" % (self.gpio, val))
        return val

    def set_level(self, level):
        """
        set GPIO output signal
        :level: refer to GpioLevel
        """
        logging.debug("set_level: set <%s>=%d" % (self.gpio, level))
        assert level in cons_list(GpioLevel)

        reg = self._regs.ctrl
        val = reg.read(RegCtrl.GPIO_SWPORT_DR)
        reg.write(RegCtrl.GPIO_SWPORT_DR, (val & (~(1<<self.pin))) | (level<<self.pin))

    def set_mux(self, mux):
        """
        set GPIO mux
        :mux: refer to GpioMux
        """
        logging.debug("set_mux: set <%s>=%d" % (self.gpio, mux))
        assert mux in cons_list(GpioMux)

        try:
            offset,bits = get_mux_offset_bits(self.gpio)
        except:
            logging.warn("set_mux: unknow mux of <%s>" % (self.gpio))
            return None

        set_rk32_iomux(self.bank, self.pin, self._regs.iomux, offset, bits, mux)

    def set_pull(self, pull):
        """
        set GPIO pull
        :pull: refer to GpioPull
        """
        logging.debug("set_pull: set <%s>=%d" % (self.gpio, pull))
        assert pull in cons_list(GpioPull)

        try:
            offset= get_pull_offset_bits(self.gpio)
        except:
            logging.warn("set_pull: unknow pull of <%s>" % (self.gpio))
            return None

        set_rk32_pull(self.pin, self._regs.pull, offset, pull)

    def set_drv(self, drv):
        """
        set GPIO drv
        :drv: refer to GpioDrv
        """
        logging.debug("set_drv: set <%s>=%d" % (self.gpio, drv))
        assert drv in cons_list(GpioDrv)

        try:
            offset= get_drv_offset_bits(self.gpio)
        except:
            logging.warn("set_drv: unknow drv of <%s>" % (self.gpio))
            return None

        set_rk32_drv(self.pin, self._regs.drv, offset, drv)


def get_pull_offset_bits(gpio):
    offset = -1
    offset = getattr(RegPull, "GRF_" + gpio[:6] + "_P")
    return offset

def set_rk32_pull(pin, reg, offset, pull):
    bit = (pin % 8)
    bit *= 2
                
    # enable the write to the equivalent lower bits 
    data = 3 << (bit + 16)
    data |= (pull << bit)

    reg.write(offset, data)

def get_drv_offset_bits(gpio):
    offset = -1
    offset = getattr(RegDrv, "GRF_" + gpio[:6] + "_E")
    return offset

set_rk32_drv = set_rk32_pull

def get_mux_offset_bits(gpio):
    offset = -1
    bits = 0
    try:
        offset = getattr(RegMux, "GRF_" + gpio[:6] + "_IOMUX")
        bits = 2
    except:
        if gpio[6] < 4:
            offset = getattr(RegMux, "GRF_" + gpio[:6] + "L_IOMUX")
        else:
            offset = getattr(RegMux, "GRF_" + gpio[:6] + "H_IOMUX")
        bits=4
    return offset,bits

def set_rk32_iomux(bank, pin, reg, offset, bits, mux):
    if bits == 2:
        bit = (pin % 8) * 2
        mask = 0x3
    elif bits == 4:
        bit = (pin % 4) * 4
        mask = 0xf
    else:
        logging.warn("set_rk32_iomux: unknow bits of <%s-%s>" % (bank, pin, mux))
        return None

    if bank == 0:
        data = reg.read(offset)
        data &= ~(mask<<bit)
        data |= (mux & mask) << bit
    else:
        data = (mask<< (bit + 16))
        data |= (mux & mask) << bit
    reg.write(offset, data)

def gpio_init():
    return gpio()

if __name__ ==  '__main__':
    gpio_init()

import unittest
import logging

class TestGpio(unittest.TestCase):
    '''
    run the follow cmd to auto test:
    python -m unittest rk3288.gpio
    '''
    def test_pull(self):
        '''
        Make sure GPIO5B1(UART1_TX) connect nothing!!
        Make sure GPIO0B5 connect nothing!!
        '''
        def _test_pull(ioname):
            gpio=Gpio(ioname)
            gpio.set_dir(GpioDir.INPUT)

            gpio.set_pull(GpioPull.DOWN)
            self.assertEqual(gpio.get_level(), GpioLevel.LOW)
            gpio.set_pull(GpioPull.UP)
            self.assertEqual(gpio.get_level(), GpioLevel.HIGH)

        _test_pull('GPIO5B1')
        _test_pull('GPIO0B5')

    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        Gpio.init()
        logging.debug("setup gpio")

    def tearDown(self):
        pass

