#!/bin/bash
#-------------------------------------------------------------------
#
#-------------------------------------------------------------------



# Change into the project root directory
SCRIPTDIR=$(readlink -f $(dirname "$0"))
pushd "${SCRIPTDIR}" > /dev/null

python3 -u generateDoc.py 2>&1 | tee -a generateDoc.log
feedback=${PIPESTATUS[1]}

# Back to the original location
popd > /dev/null

exit ${feedback}
