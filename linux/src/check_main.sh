#!/bin/bash

while true; do

  pgrep -x python  && echo "Process found" || echo "Process not found" && python3 src/main__copy.py
  sleep 3
  $SHELL
done