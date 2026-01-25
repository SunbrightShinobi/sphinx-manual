#!/bin/bash

# Save start time
start_total=$(date +%s)

echo "==============================="
echo "Timing Sphinx HTML build"
echo "==============================="
start_html=$(date +%s)
time make clean html
end_html=$(date +%s)
echo "HTML build took $((end_html - start_html)) seconds"

echo "==============================="
echo "Timing Sphinx LaTeX/PDF build"
echo "==============================="
start_pdf=$(date +%s)
time make clean latexpdf
end_pdf=$(date +%s)
echo "LaTeX/PDF build took $((end_pdf - start_pdf)) seconds"

end_total=$(date +%s)
echo "==============================="
echo "Total build time: $((end_total - start_total)) seconds"
echo "==============================="
