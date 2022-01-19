#!/bin/bash

LOG_FILE=/home/textbooks/cc-website.log
DISCORD="discord://910933777826578502/KhKKD2A8GmgmsWwCVLIx6hb0PPsPqlDi4PDB2HrWR3XJiPOAUntOQWK1qWMx-q_Ob-VC"

echo "=========================================="
echo `date` >> ${LOG_FILE}
echo "Started Deploying cc-website" >> ${LOG_FILE}
apprise -vv -b "Started Deploying cc-website" ${DISCORD} >> ${LOG_FILE} 2>&1

cd ../cc-website-html
git pull
git rm -rf .
git clean -fxd

cd ../cc-website
git pull --recurse-submodules

hugo
cd ../cc-website-html
git add .
git commit -m "Automatic Deploy on `date +'%Y-%m-%d %H:%M:%S'`"
git push -u origin master

apprise -vv -b "Started rsync for cc-website" ${DISCORD} >> ${LOG_FILE} 2>&1
echo "Started rsync for cc-website" >> ${LOG_FILE}

#ssh russfeld@cslinux.cs.ksu.edu "cd /web/core && git pull"
ssh russfeld@cslinux.cs.ksu.edu "cd /home/r/russfeld/cc-website-html && git pull && rsync -aP --exclude='.git' /home/r/russfeld/cc-website-html/ /web/core && chmod -R a+rx /web/core/*"

apprise -vv -b "Finished Deploying cc-website" ${DISCORD} >> ${LOG_FILE} 2>&1
echo "Finished Deploying cc-website" >> ${LOG_FILE}

echo "=========================================="

exit 0
