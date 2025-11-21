---
title: "TaxMyPhage"
collection: software
permalink: /software/taxmyphage/
layout: single
author_profile: true
read_time: true
toc: true
---

# TaxMyPhage: Workflow to assign Taxonomy to a bacteriophage genome isolate

**TaxMyPhage** is a tool designed to assign taxonomy to bacteriophage genomes at the genus and species level.

## Overview

TaxMyPhage identifies the most similar genomes in the set of currently classified ICTV genomes that are present in the **VMR (Virus Metadata Resource)**. It compares the query genome against these genomes and runs a **VIRIDIC-like analysis** on the closest relatives to determine if the phage falls within a current genus or species, or represents a new one.

## Key Features

*   **Taxonomic Classification**: Classifies dsDNA phage genomes at the Genus and/or Species level against ICTV genomes.
*   **New Genus Detection**: Identifies if your genome represents a new genus based on current ICTV cutoffs.
*   **Automated Workflow**: Takes a single genome sequence as input and automates the comparison and classification process.
*   **Multiple Inputs**: Can accept multiple inputs at the same time.

## How it Works

1.  **Similarity Search**: Identifies the closest relatives in the VMR database.
2.  **VIRIDIC-like Analysis**: Calculates intergenomic similarities using the same formula as VIRIDIC.
3.  **Classification**: Applies ICTV cutoffs to assign taxonomy or flag potential new genera.

## Resources

*   **GitHub Repository**: [amillard/tax_myPHAGE](https://github.com/amillard/tax_myPHAGE)
*   **Web Version**: [ptax.ku.dk](https://ptax.ku.dk/)
*   **Paper**: [Phage Article](https://www.liebertpub.com/doi/10.1089/phage.2024.0050)

**Developed by**: Andrew Millard, Thomas Sicheritz-Ponten, and **Remi Denise**.
