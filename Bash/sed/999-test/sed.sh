#!/bin/bash

echo $'\n----Before----'
cat test.txt
echo $'\n----After-----'
sed '/111/d' test.txt