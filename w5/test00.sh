#!/bin/dash

# ===================
# Testing pigs-init when run multiple times
# Date:
# Author
# ====================

new_dir=$(mktemp -d)
expected_output=$(mktemp)
actual_output=$(mktemp)

trap 'rm "$expected_output" "$actual_output"' INT QUIT EXIT HUP

echo "Initialized empty pigs repository in .pig" >> $expected_output

PATH=$PATH:$(pwd)

pigs-init > $actual_output

if ! diff $actual_output $expected_output
then
    echo "failed test"
    exit 42
fi

pigs-init > $actual_output

echo "pigs-init: error: .pig already exists" > $expected_output

if ! diff $actual_output $expected_output
then
    echo "failed test"
    exit 42
fi

echo "test passed!"






# diff 