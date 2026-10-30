#!/bin/bash
# usage: build_doc.sh <docdir> <final-name.docx>
set -e
D=$1; OUT=$2; M=${DOCBUILDER:-$(cd $(dirname $0) && pwd)}
SOF=${SOFFICE_PY:-/mnt/skills/public/docx/scripts/office/soffice.py}  # docx skill helper; set SOFFICE_PY if elsewhere
cd $D; rm -f toc_pages.json
for pass in 1 2; do
  DOCDIR=$D node $M/build.js $D/p.docx >/dev/null
  python3 $SOF --headless --convert-to pdf p.docx >/dev/null 2>&1
  python3 $M/pages.py $D p.pdf
done
cp p.docx "$OUT"; pdfinfo p.pdf | grep Pages
python3 /root/.claude/skills/synced/7f8414ae-4694-4385-b1db-e3d7d64c487d_e2e8dd44-bd39-4679-b9a1-45a31a47573f/docx/scripts/office/validate.py "$OUT" 2>&1 | tail -1
