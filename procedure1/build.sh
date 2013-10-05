#!/bin/bash

mmd_merge.pl index.txt | multimarkdown | tee index.html
