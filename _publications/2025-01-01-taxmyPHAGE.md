---
title: "taxmyPHAGE: automated taxonomy of dsDNA phage genomes at the genus and species level"
collection: publications
permalink: /publication/2025-01-01-taxmyPHAGE
date: 2025-01-01
venue: 'Phage (New Rochelle)'
paperurl: 'https://www.liebertpub.com/doi/abs/10.1089/phage.2024.0050'
citation: 'A. Millard, R. Denise, M. Lestido, M.T. Thomas, D. Webster, S. O''Toole, A. Shkoporov, C. Hill, <b>taxmyPHAGE: automated taxonomy of dsDNA phage genomes at the genus and species level.</b> <i>Phage (New Rochelle)</i>, 2024.'
open_access: true
githuburl: https://github.com/amillard/tax_myPHAGE
---
Background: Bacteriophages are classified into genera and species based on genomic similarity, a process regulated by the International Committee on the Taxonomy of Viruses. With the rapid increase in phage genomic data there is a growing need for automated classification systems that can handle large-scale genome analyses and place phages into new or existing genera and species. Materials and Methods: We developed taxMyPhage, a tool system for the rapid automated classification of dsDNA bacteriophage genomes. The system integrates a MASH database, built from ICTV-classified phage genomes to identify closely related phages, followed by BLASTn to calculate intergenomic similarity, conforming to ICTV guidelines for genus and species classification. taxMyPhage is available as a git repository at https://github.com/amillard/tax_myPHAGE, a conda package, a pip-installable tool, and a web service at https://phagecompass.ku.dk. Results: taxMyPhage enables rapid classification of bacteriophages to the genus and species level. Benchmarking on 705 genomes pending ICTV classification showed a 96.7% accuracy at the genus level and 97.9% accuracy at the species level. The system also detected inconsistencies in current ICTV classifications, identifying cases where genera did not adhere to ICTV’s 70% average nucleotide identity (ANI) threshold for genus classification or 95% ANI for species. The command line version classified 705 genomes within 48 h, demonstrating its scalability for large datasets.

<i class="ai ai-open-access ai-2x"></i> [Access paper here]({{ page.paperurl }}){:target="_blank"} <br>
{% if page.halurl %} <i class="ai ai-hal ai-2x"></i> [HAL version]({{ page.halurl }}){:target="_blank"} <br> {% endif %}
{% if page.githuburl %} <i class="fab fa-github ai-2x"></i> [GitHub repository]({{ page.githuburl }}){:target="_blank"} {% endif %}
