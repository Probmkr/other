#!/bin/sh

echo '----Before----';
cat test.txt
echo '----After-----';
sed '2,5d' test.txt