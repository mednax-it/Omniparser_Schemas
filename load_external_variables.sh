#!/usr/bin/env bash
set -e

declare PARSER_URL=PARSER_URL_$1

#!/bin/bash
echo "export PARSER_URL=$"${PARSER_URL} >> $BASH_ENV

exit 0