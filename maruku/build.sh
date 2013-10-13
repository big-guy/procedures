#!/bin/bash

m4 -I. -DLASTAUTHOR=SGreene -DLASTMODDATE=2013/10/13 index.m4 > index.md
maruku -b index.md -o - | tee index.html
