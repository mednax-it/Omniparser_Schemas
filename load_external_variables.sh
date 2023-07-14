#!/usr/bin/env bash
set -e

declare DEV_PARSER_URL=DEV_PARSER_URL_$1
declare PROD_PARSER_URL=PROD_PARSER_URL_$1

#!/bin/bash

if [ "${CIRCLE_BRANCH}" == "main" ]
then
  echo "export PARSER_URL=$"${PROD_PARSER_URL} >> $BASH_ENV
  echo "loaded prod env variables"
else
  echo "export PARSER_URL=$"${DEV_PARSER_URL} >> $BASH_ENV
  echo "looaded preprod env variables"
fi

echo "load env variables in the project"

exit 0