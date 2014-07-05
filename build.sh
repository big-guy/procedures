#!/usr/bin/env bash

declare project=$1
declare dataFile=${project}/data.json
declare templateFile=${project}/template.mustache
declare outdir=${project}/build
declare mainOut=${outdir}/main.md
declare bodyOut=${outdir}/body.html

mkdir -p $outdir

# HTML Template
# -------------

# Create a function for apply the standard [Docco][do] HTML layout, using
# [jashkenas][ja]'s gorgeous CSS for styles. Wrapping the layout in a function
# lets us apply it elsewhere simply by piping in a body.
#
# [ja]: http://github.com/jashkenas/
# [do]: http://jashkenas.github.com/docco/
layout () {
    cat <<HTML
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv='content-type' content='text/html;charset=utf-8'>
    <title>$1</title>
    <link rel=stylesheet href="http://jashkenas.github.com/docco/resources/docco.css">
</head>
<body>
$(cat)
</body>
</html>
HTML
}

pystache $templateFile $dataFile > ${mainOut}

markdown_py -x extra -x toc -x sane_lists -x meta ${mainOut} | layout "test" 


