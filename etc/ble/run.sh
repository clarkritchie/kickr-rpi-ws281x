#!/usr/bin/env bash
# Determine the MAC of your decide with: sudo hcitool lescan
MAC=${1:-df:7d:9c:da:1b:c5}
./example.py ${MAC}