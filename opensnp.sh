#!/bin/bash

BASE='https://www.opensnp.org'
basepage="${BASE}/genotypes?page="
# List file names and begin a crude crawl
function filelister {
  for i in `seq 1 10 226`; do
    next=$(( i + 9 ))
    if [[ $next -gt 226 ]]; then
      next=226
    fi
    curl -s "${basepage}""[$i-$next]" | sed -n 's/.*href="\(.*\)">Download.*/\1/ p'
  done
}
# Grab output, sort it and update links
filelister | sort -u | sed 's#\.\.#'$BASE'#g' > genelinks.cfg
