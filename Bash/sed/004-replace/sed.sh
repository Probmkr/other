#!/bin/bash

echo $'
----Before----'
cat test.txt
echo $'
----After-----'
sed 's/aaa/zzz/g' test.txt