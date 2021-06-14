#!/bin/bash

while true; do

  pgrep -x python3 && python3 src/main__copy.py  || echo "Process not found" && python3 src/main__copy.py
  sleep 3
  $SHELL
done