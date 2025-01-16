#!/bin/bash

echo "BUILD START"

# Install dependencies using Python
python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput

echo "BUILD END"
