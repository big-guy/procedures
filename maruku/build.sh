#!/bin/bash

maruku -b index.md -o - | tee index.html
