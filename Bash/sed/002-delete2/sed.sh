#!/bin/sh

echo '----Before----';
cat test.txt
echo '----After-----';
sed '/^$/d' test.txt
