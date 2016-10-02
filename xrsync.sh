#!/bin/bash

rsync -av \
	--delete \
	--exclude .htaccess \
	$(pwd)/build/ \
	ccsm.radicalcadence.com:/var/www/vhosts/ccsm.radicalcadence.com/htdocs/

