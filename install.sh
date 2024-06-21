#!/bin/bash

set -e
cd "${0%/*}" || exit 1;   # Go to the script location

if test ! -f ppro-po-sat-gas-ff.sif
then
    echo "Compiling panda-pi."
    cd src
    apptainer build ../ppro-po-sat-gas-ff.sif ppro-po-sat-gas-ff.def
else
    echo "panda-pi already compiled."
fi
