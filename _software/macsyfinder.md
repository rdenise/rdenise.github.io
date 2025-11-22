---
title: "MacSyFinder & TXSScan"
collection: software
permalink: /software/macsyfinder/
layout: single
author_profile: true
read_time: true
toc: true
---

# MacSyFinder: Modeling and detection of macromolecular systems

**MacSyFinder** is a program designed to model and detect macromolecular systems, genetic pathways, and other complex structures in protein datasets.

![MacSyFinder logo](/assets/images/software/macsyfinder_logo.png)

## What is MacSyFinder?

In prokaryotes, many biological systems (like secretion systems, flagella, or CRISPR-Cas systems) have evolutionarily conserved properties:
*   They are made of **conserved components**.
*   They are encoded in **compact loci** (conserved genetic architecture).

MacSyFinder allows users to model these systems to reflect these conserved features, enabling their efficient detection using Hidden Markov Models (HMMs) and defined decision rules.

## TXSScan: Type IV Secretion Systems Models

A key application of MacSyFinder is **TXSScan**, a set of models dedicated to the identification of **Bacterial Secretion Systems** and **Type IV-filament super-family** systems.

I actively contributed to the development of these models, which allow for the precise annotation of:
*   **Type IV Secretion Systems (T4SS)**
*   **Type IV Pili (T4P)**
*   **Tad pili**
*   **Com systems** (competence)

These models are essential for understanding the distribution, evolution, and diversification of these critical bacterial machineries.

## Resources

### MacSyFinder
*   **Documentation**: [Read the Docs](https://macsyfinder.readthedocs.io/en/latest/)
*   **GitHub**: [gem-pasteur/macsyfinder](https://github.com/gem-pasteur/macsyfinder)
*   **Paper**: [Peer Community Journal](https://peercommunityjournal.org/item/10_24072_pcjournal_250/)
*   **Book Chapter**: [How to use MacSyFinder](https://www.biorxiv.org/content/biorxiv/early/2023/01/06/2023.01.06.522999.full.pdf)

### TXSScan Models
*   **GitHub**: [macsy-models/TXSScan](https://github.com/macsy-models/TXSScan)
*   **MacSy Models Organization**: [macsy-models](https://github.com/macsy-models)
