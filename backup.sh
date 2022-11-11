fechaprev=`date -d "-1 days" +%d-%m-%y`
fechaact=`date +%d-%m-%y`
rsync -av --link-dest=/var/tmp/Backups/$fechaprev /home/ruben/Escritorio/Seguridad/ /var/tmp/Backups/$fechaact
