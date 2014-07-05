#!/usr/bin/env bash

declare project=$1
declare dataFile=${project}/data.json
declare mainFile=${project}/template.mustache
declare outdir=${project}/build
declare indexOut=${outdir}/index.md

mkdir -p $outdir

pystache $mainFile $dataFile > ${indexOut}

markdown_py -x extra -x toc -x sane_lists -x meta ${indexOut} --output_format=html5 --file=${outdir}/index.html
