#!/bin/bash
# Script to run a single test case

if [ -z "$1" ]; then
    echo "Usage: bash run_single_test.sh <test_case_name>"
    echo "Example: bash run_single_test.sh TestLevel1.test_create_account"
    exit 1
fi

python3 -m unittest test_banking_system."$1" -v

