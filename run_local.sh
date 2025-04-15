#!/bin/bash

set -o allexport
source .env
set +o allexport

source $(poetry env info --path)/bin/activate

cd app

streamlit run home.py