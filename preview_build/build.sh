#!/bin/sh

pip install -r requirements.txt

rm -rf ./build && \
cp ./preview_configuration.py ./conf.py && \

# sphinx-build -b html -d build/doctrees ../docs/it/ build
sphinx-build -b html -d build/en/doctrees ../docs/en/ build/en
sphinx-build -b html -d build/it/doctrees ../docs/it/ build/it
