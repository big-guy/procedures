#!/bin/bash

if [ $# -ne 1 ] ; then
   echo "$0 procedure-dir"
   exit -1
fi

declare PROCEDURE=$1
declare BUILDDIR="build/${PROCEDURE}"

echo "Building $PROCEDURE"

echo "Build attributes:"
source ${PROCEDURE}/meta.info 

rm -rf ${BUILDDIR}
mkdir -p $BUILDDIR
m4 -I${PROCEDURE} -Icommon common/index.m4 > ${BUILDDIR}/index.md

maruku -b ${BUILDDIR}/index.md -o - | tee ${BUILDDIR}/index.html

cp -r common/{css,lib} ${BUILDDIR}/
