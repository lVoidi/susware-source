#!/bin/bash
function ignore_ctrlc() {
        echo "ignored"
}

trap ignore_ctrlc SIGINT SIGTERM
while : 
do

  pgrep -x python  && echo "Process found" || echo "Process not found" && exec python3 main__copy.py
  sleep 3

done