#!/bin/bash
# find ./UI -name '*.ui' -exec python -m PyQt5.uic.pyuic -x {} -o $(basename {}) \;
for ui in $(ls ./UI/*.ui); do
    py=$(basename ${ui} .ui)
    # echo "${ui}"
    python -m PyQt5.uic.pyuic -x ${ui} -o ${py}.py
done
