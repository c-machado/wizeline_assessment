#!/usr/bin/env bash

printf "STARTING DOCKER TEST:\n"

pytest tests/ -m "feed-article-date-format1" --html=reports/blog/feed-date-format.html

