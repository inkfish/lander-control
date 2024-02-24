This directory contains simple scripts for testing functionality of individual board components.

To load a script, attach the Raspberry Pi Pico to a PC using a USB cable. The volume "CIRCUITPY" should appear. Copy the demo script to this drive.

> [!IMPORTANT]  
> An issue with the userspace FAT driver on macOS prevents copying to the CIRCUITPY volume ([issue #8449](https://github.com/adafruit/circuitpython/issues/8449)). The script `./utils/remount-circuitpy.sh` works around this bug.

Open a serial connection to the Pico and press Ctrl-C to break into the REPL. Enter `import scriptname` (omitting the `.py` extension) to run the code.
