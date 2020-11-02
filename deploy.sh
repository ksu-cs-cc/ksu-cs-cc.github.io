#!/bin/bash

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

#ssh russfeld@cslinux.cs.ksu.edu "cd /web/core && git pull"
ssh russfeld@cslinux.cs.ksu.edu "cd /home/r/russfeld/cc-website-html && git pull && rsync -aP --exclude='.git' /home/r/russfeld/cc-website-html/ /web/core && chmod 755 -R /web/core/*"

exit 0
