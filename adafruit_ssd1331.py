# The MIT License (MIT)
#
# Copyright (c) 2019 Melissa LeBlanc-Williams for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_ssd1331`
================================================================================

displayio Driver for SSD1331 Displays


* Author(s): Melissa LeBlanc-Williams

Implementation Notes
--------------------

**Hardware:**

* OLED Breakout Board - 16-bit Color 0.96" w/microSD holder:
  https://www.adafruit.com/product/684

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

import displayio

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_SSD1331.git"

_INIT_SEQUENCE = (
    b"\xAE\x00"  # _DISPLAYOFF
    b"\xA0\x01\x72"  # _SETREMAP (RGB)
    b"\xA1\x01\x00"  # _STARTLINE
    b"\xA2\x01\x00"  # _DISPLAYOFFSET
    b"\xA4\x00"  # _NORMALDISPLAY
    b"\xA8\x01\x3F"  # _SETMULTIPLEX (1/64 duty)
    b"\xAD\x01\x8E"  # _SETMASTER
    b"\xB0\x01\x0B"  # _POWERMODE
    b"\xB1\x01\x31"  # _PRECHARGE
    b"\xB3\x01\xF0"  # _CLOCKDIV 7:4 = Osc Freq, 3:0 = CLK Div Ratio
    b"\x8A\x01\x64"  # _PRECHARGEA
    b"\x8B\x01\x78"  # _PRECHARGEB
    b"\x8C\x01\x64"  # _PRECHARGEC
    b"\xBB\x01\x3A"  # _PRECHARGELEVEL
    b"\xBE\x01\x3E"  # _VCOMH
    b"\x87\x01\x06"  # _MASTERCURRENT
    b"\x81\x01\x91"  # _CONTRASTA
    b"\x82\x01\x50"  # _CONTRASTB
    b"\x83\x01\x7D"  # _CONTRASTC
    b"\xAF\x00"  # _DISPLAYON
)

# pylint: disable=too-few-public-methods
class SSD1331(displayio.Display):
    """SSD1331 driver"""

    def __init__(self, bus, **kwargs):
        super().__init__(
            bus,
            _INIT_SEQUENCE,
            **kwargs,
            set_column_command=0x15,
            set_row_command=0x75,
            single_byte_bounds=True,
            data_as_commands=True,
        )
