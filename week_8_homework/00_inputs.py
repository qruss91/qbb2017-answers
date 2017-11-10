hifive 5c-complete express -P NORA -C Nora_ESC_male_E14.counts Nora_Primers.bed 

hifive 5c-heatmap NORA.fcp Out_fragment.heat -i Out_fragment.png -d fragment

hifive 5c-heatmap NORA.fcp Out_enrichment.heat -i Out_enrichment.png -d enrichment

./01_itried.txt ctcf_peaks.tsv Nora_Primers.bed > top_ctcf_ixns.txt
