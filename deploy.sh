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

ssh russfeld@cslinux.cs.ksu.edu "cd /web/core && git pull"

exit 0
