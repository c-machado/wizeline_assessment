#!/usr/bin/env bash


printf "STARTING TESTS:\n"

pytest tests/ -m "checkout" --html=reports/checkout.html


