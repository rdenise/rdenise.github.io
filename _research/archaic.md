---
title: "ARCHAIC: Diversity of bacteriophages in the ancient human microbiome"
collection: research
permalink: /research/archaic/
layout: single
author_profile: true
read_time: true
toc: true
---

# Strategies for the successful discovery and identification of bacteriophages from ancient DNA

**ARCHAIC** is a Marie Skłodowska-Curie Actions (MSCA) Postdoctoral Fellowship project [Grant agreement ID: 101111040](https://cordis.europa.eu/project/id/101111040) dedicated to uncovering the hidden world of ancient bacteriophages.

Ancient DNA (aDNA) provides an invaluable window into past ecosystems, offering insights
into microbial communities and their viral components, including bacteriophages. Detecting
phages in aDNA samples is critical for reconstructing ancient microbiomes and understanding
host-phage dynamics over evolutionary timescales. However, phage identification remains
challenging due to degradation, contamination, and methodological biases inherent to ancient
samples. In this study, we compare multiple complementary techniques for phage detection,
including taxonomic profiling, reads mapping, and de novo assembly. Our findings reveal that
taxonomic profiling enables the identification of broad viral categories, while reads mapping
provides higher-resolution insights into which phages are present in the samples. De novo
assembly proves essential for uncovering novel and fragmented phage genomes. These
approaches, when used in combination, offer a robust and comprehensive framework for
characterizing phage diversity and dynamics in ancient microbiomes, paving the way for new
discoveries in aDNA.

## Methodology

To address these challenges, we developed a hierarchical workflow for viral detection, abundance estimation, and discovery from ancient biological samples. This integrative approach combines multiple bioinformatic strategies:

1.  **Taxonomic Profiling**: Initial screening of reads using tools like Centrifuge.
2.  **Reference Mapping**: Mapping reads to identified viral genomes to assess breadth of coverage.
3.  **De Novo Assembly**: Assembling reads into contigs to recover longer viral sequences.
4.  **Viral Detection**: Using machine learning tools (e.g., geNomad, Jaeger) to identify viral signals in contigs.
5.  **Discovery**: Identifying potential novel viral sequences from the assembled contigs.

![Hierarchical workflow for viral detection](/assets/images/archaic/image1.png)
*Figure 1: Hierarchical workflow for viral detection, abundance estimation, and discovery from ancient biological samples.*

## Key Findings

Our study systematically evaluated these strategies using both simulated and empirical ancient metagenomic datasets (from palaeofaeces and dental calculus).

### Taxonomic Profiling vs. Genome Mapping
We found that while taxonomic profiling provides a useful starting point, it often overestimates viral diversity. Rigorous validation through genome mapping and assessment of ancient DNA damage patterns (C→T transitions) is essential for confirming the authenticity of ancient phages.

### The Power of Contig Assembly
Assembling reads into contigs significantly improved the detection of viral genomes. We observed that:
*   **Longer reads** improve taxonomic classification accuracy.
*   **Contig assembly** helps bridge the gap caused by DNA fragmentation, allowing for the recovery of more complete viral genomes.
*   **Binning** tools like taxVAMB can cluster fragmented viral contigs into high-quality viral metagenome-assembled genomes (vMAGs).

![Taxonomic profiling and validation](/assets/images/archaic/image3.png)
*Figure 2: Taxonomic profiling and validation of viral species from ancient samples. The process highlights the reduction in potential viral species after rigorous validation.*

## Conclusion

Our findings demonstrate that a multi-faceted approach—combining taxonomic profiling, genome mapping, and *de novo* assembly—is required to accurately reconstruct ancient viral communities. This framework not only enhances our ability to detect known phages but also opens the door to discovering novel viral diversity in the archaeological record.

**Funding**: This project is supported by the European Union’s Horizon 2021-2027 research and innovation programme under the Marie Skłodowska Curie grant agreement N° [101111040](https://cordis.europa.eu/project/id/101111040).
