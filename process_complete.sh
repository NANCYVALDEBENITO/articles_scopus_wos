#!/bin/bash 

echo "Process available"

python process.py

mv /home/nvaldebenito/Descargas/savedrecs.txt /home/nvaldebenito/Documentos/20_articles_process/wos_aff.csv
mv /home/nvaldebenito/Descargas/savedrecs.xls /home/nvaldebenito/Documentos/20_articles_process/wos_cit.xls

python national_inst_wos.py
python national_inst_scopus.py

Rscript master_cr2_articles.R

