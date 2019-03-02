#!/bin/bash
echo '参数1: $1'
echo 'pull mcenter'
cd /mnt/hgfs/gopath/src/gsn/mcenter/
git pull
git status
	echo 'pull geesunn'
cd /mnt/hgfs/gopath/src/geesunn.com/
git pull
git status
