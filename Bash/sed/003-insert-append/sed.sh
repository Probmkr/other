#!/bin/bash

echo $'\n----Before----'
cat test.txt
echo $'\n----After-----'
sed 'ixxx' test.txt
echo $'\n----After2----'
sed 'axxx' test.txt