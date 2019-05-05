#!/bin/bash
adafruit-io camera config --username USERNAME --key KEY
adafruit-io camera start -f camera_feed -m false -r 2
