#!/bin/sh
echo "Prepping App!"
black .
isort --profile=black .
flake8 --config=./.flake8 .
echo "Running App!"
exec "$@"
