---
title: "taxmyPHAGE: automated taxonomy of dsDNA phage genomes at the genus and species level"
collection: publications
publication_type: research
permalink: /publication/2025-03-17-taxmyPHAGE
date: 2025-03-17
venue: 'Phage (New Rochelle)'
paperurl: 'https://pubmed.ncbi.nlm.nih.gov/40351403/'
citation: 'A. Millard, R. Denise, M. Lestido, M.T. Thomas, D. Webster, S. D. Turner, T. Sicheritz-Pontén, <b>taxmyPHAGE: automated taxonomy of dsDNA phage genomes at the genus and species level.</b> <i>Phage (New Rochelle)</i>, 2025 Mar 17;6(1):5-11.'
open_access: true
githuburl: https://github.com/amillard/tax_myPHAGE
---
Background: Bacteriophages are classified into genera and species based on genomic similarity, a process regulated by the International Committee on the Taxonomy of Viruses. With the rapid increase in phage genomic data there is a growing need for automated classification systems that can handle large-scale genome analyses and place phages into new or existing genera and species. Materials and Methods: We developed taxMyPhage, a tool system for the rapid automated classification of dsDNA bacteriophage genomes. The system integrates a MASH database, built from ICTV-classified phage genomes to identify closely related phages, followed by BLASTn to calculate intergenomic similarity, conforming to ICTV guidelines for genus and species classification. taxMyPhage is available as a git repository at https://github.com/amillard/tax_myPHAGE, a conda package, a pip-installable tool, and a web service at https://phagecompass.ku.dk. Results: taxMyPhage enables rapid classification of bacteriophages to the genus and species level. Benchmarking on 705 genomes pending ICTV classification showed a 96.7% accuracy at the genus level and 97.9% accuracy at the species level. The system also detected inconsistencies in current ICTV classifications, identifying cases where genera did not adhere to ICTV’s 70% average nucleotide identity (ANI) threshold for genus classification or 95% ANI for species. The command line version classified 705 genomes within 48 h, demonstrating its scalability for large datasets.


