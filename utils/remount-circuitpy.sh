#!/bin/bash -eu
# remount-circuitpy.sh -- remount a FAT disk, usually CIRCUITPY, so it works
#
# Works around bug where macOS 14.x causes file corruption on small FAT
# filesystems. The remount apparently causes older kernel FAT driver
# to be loaded. see https://github.com/adafruit/circuitpython/issues/8449
#
# Original author: Tod Kurt @todbot

DISKNAME=${1:-CIRCUITPY}
DISKDEV=`df | grep ${DISKNAME} | cut -d" " -f1`

sudo umount "/Volumes/${DISKNAME}"
sudo mkdir "/Volumes/${DISKNAME}"
sleep 2
sudo mount -v -t msdos "$DISKDEV" "/Volumes/${DISKNAME}"
