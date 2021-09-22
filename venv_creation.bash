#!/usr/bin/env bash

cd "$(dirname "$0")"

rm -rf venv || true
virtualenv -p /usr/bin/python3 venv
venv/bin/pip3 install --upgrade pip
venv/bin/pip3 install -r requirements.txt
