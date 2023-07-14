#!/usr/bin/env node

process.env.PARSER_URL = ( process.env.CIRCLE_BRANCH === 'main' )
    ? process.env.DEV_PARSER_URL,
    : process.env.PROD_PARSER_URL;