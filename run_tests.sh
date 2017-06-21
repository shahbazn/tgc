#!/bin/bash

set -e

if [[ "$TEST_TYPE" = "integ" ]]
then
  if curl http://"$DOMAIN"/calculate?x=1 | grep -q 'undefined'; then
    echo "Tests passed!"
    exit 0
  else
    echo "Tests failed!"
    exit 1
  fi
fi

if [[ "$TEST_TYPE" = "unit" ]]
then
  python -m unittest tgc
fi
