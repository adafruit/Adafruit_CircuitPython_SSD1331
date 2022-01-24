Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-ssd1331/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/ssd1331/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_SSD1331/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_SSD1331/actions/
    :alt: Build Status

displayio drivers for SSD1331 Displays


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

.. code-block:: python

    import board
    import displayio
    import terminalio
    from adafruit_display_text import label
    from adafruit_ssd1331 import SSD1331

    spi = board.SPI()
    tft_cs = board.D5
    tft_dc = board.D6

    displayio.release_displays()
    display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D9)

    display = SSD1331(display_bus, width=96, height=64)

    # Make the display context
    splash = displayio.Group()
    display.show(splash)

    color_bitmap = displayio.Bitmap(96, 64, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x00FF00 # Bright Green

    bg_sprite = displayio.TileGrid(color_bitmap,
                                   pixel_shader=color_palette,
                                   x=0, y=0)
    splash.append(bg_sprite)

    # Draw a smaller inner rectangle
    inner_bitmap = displayio.Bitmap(86, 54, 1)
    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0xAA0088 # Purple
    inner_sprite = displayio.TileGrid(inner_bitmap,
                                      pixel_shader=inner_palette,
                                      x=5, y=5)
    splash.append(inner_sprite)

    # Draw a label
    text = "Hello World!"
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=12, y=32)
    splash.append(text_area)

    while True:
        pass

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/ssd1331/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_SSD1331/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
