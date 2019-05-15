#!/bin/bash 

echo "Process available"


python 01_process_scopus.py
python 02_process_wos.py

mv /home/nvaldebenito/Descargas/savedrecs.txt /home/nvaldebenito/Documentos/20_articles_process/savedrecs.csv
mv /home/nvaldebenito/Descargas/scopus.csv /home/nvaldebenito/Documentos/20_articles_process/scopus.csv
mv /home/nvaldebenito/Descargas/savedrecs.xls /home/nvaldebenito/Documentos/20_articles_process/wos_cit.xls

python 03_national_inst_scopus.py
python 04_national_inst_wos.py

Rscript master_cr2_articles.R

