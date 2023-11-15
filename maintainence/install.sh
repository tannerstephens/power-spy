#!/usr/bin/env bash

apt update
apt install -y python3-pip

python -m pip install --upgrade pip
python -m pip install pipenv
PIPENV_VENV_IN_PROJECT=1 pipenv install --skip-lock --python "$(python --version)"

cp power-spy.service /etc/systemd/system/power-spy.service

systemctl daemon-reload
systemctl enable power-spy
systemctl restart power-spy
