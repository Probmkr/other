#!/bin/sh

echo '----Before----';
cat test.txt
echo '----After-----';
sed '2~2d' test.txt