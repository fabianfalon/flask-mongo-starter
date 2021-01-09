#!/bin/bash

while ! nc -z rabbit 5672; do sleep 3; done
python subscriber.py
