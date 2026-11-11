# Basic Protein Structure Exploration

A structural biology and bioinformatics exploration of three-dimensional macromolecular architectures using the RCSB Protein Data Bank (PDB), Python, and PyMOL.

## Overview

Proteins carry out nearly all biochemical activities in living cells. Their biological functions depend directly on their precise three-dimensional conformations. This project examines structural hierarchies across representative proteins, focusing on:

1. Identification of primary amino acid chains and sequence length.
2. Characterization of secondary structure elements (alpha helices and beta sheets).
3. Inspection of tertiary spatial folds, prosthetic groups, and stabilizing disulfide bridges.
4. Quaternary multi-subunit assembly in oligomeric complexes.

## Four Levels of Protein Architecture

* **Primary Structure**: Linear sequence of amino acid residues joined by covalent peptide bonds.
* **Secondary Structure**: Periodic local conformations of the polypeptide backbone stabilized by hydrogen bonding between amide protons and carbonyl oxygens.
  * **Alpha Helix**: Right-handed spiral with 3.6 residues per turn and a pitch of 5.4 Angstroms. Hydrogen bonds form between residue $i$ and residue $i+4$.
  * **Beta Pleated Sheet**: Lateral association of extended polypeptide strands (parallel or antiparallel) with inter-strand backbone hydrogen bonding.
* **Tertiary Structure**: Full three-dimensional fold of a single polypeptide chain, driven by hydrophobic collapse, salt bridges, hydrogen bonds, and covalent disulfide crosslinks.
* **Quaternary Structure**: Non-covalent association of multiple folded polypeptide subunits into a functional multimer (e.g., hemoglobin $\alpha_2\beta_2$ heterotetramer).

## Publicly Available Structures Explored

Three representative macromolecular structures were downloaded from the Protein Data Bank (RCSB PDB):

| PDB ID | Protein Name | Source Organism | Resolution | Key Structural Features |
| :--- | :--- | :--- | :--- | :--- |
| **1CRN** | Crambin | *Crambe hispanica* | 1.50 Å | 46 residues, mixed $\alpha/\beta$ fold, 3 disulfide bonds |
| **1MBN** | Deoxymyoglobin | *Physeter catodon* | 2.00 Å | 153 residues, globin fold (8 $\alpha$-helices, 0 $\beta$-sheets), heme group |
| **1HHO** | Oxyhemoglobin | *Homo sapiens* | 2.10 Å | 287 residues, $\alpha_2\beta_2$ tetramer, cooperativity, 4 heme groups |

## Project Structure

```text
protein-structure-exploration/
|
|-- data/
|   |-- 1crn.pdb
|   |-- 1hho.pdb
|   |-- 1mbn.pdb
|-- figures/
|   |-- alpha_helix_vs_beta_sheet.png
|   |-- protein_structural_levels.png
|   |-- secondary_structure_composition.png
|-- scripts/
|   |-- render_crambin.pml
|   |-- render_hemoglobin.pml
|   |-- render_myoglobin.pml
|-- explore_structure.py
|-- generate_diagrams.py
|-- requirements.txt
|-- .gitignore
|-- README.md
```

## Running the Python Structure Explorer

Parse local PDB coordinate files, print sequence properties, count secondary structure elements, and generate comparative composition charts:

```bash
git clone https://github.com/your-username/protein-structure-exploration.git
cd protein-structure-exploration
pip install -r requirements.txt
python explore_structure.py
```

### Script Output Summary

```text
PDB ID: 1CRN
Chains: A | Total Residues: 46
Alpha Helices: 2 (21 residues, 45.7%)
Beta Sheets: 2 (8 residues, 17.4%)
Disulfide Bonds: 3 (Cys3-Cys40, Cys4-Cys32, Cys16-Cys26)

PDB ID: 1MBN
Chains: A | Total Residues: 153
Alpha Helices: 8 (118 residues, 77.1%)
Beta Sheets: 0 (0.0%)
Ligands: Heme (HEM)

PDB ID: 1HHO
Chains: A, B | Total Residues: 287
Alpha Helices: 16 (224 residues, 78.0%)
Beta Sheets: 0 (0.0%)
Ligands: Heme (HEM), Phosphate (PO4), Molecular Oxygen (OXY)
```

## Visualizing with PyMOL

PyMOL command scripts are provided in the `scripts/` directory for automated visualization and rendering.

### Method 1: Running inside the PyMOL GUI

Open PyMOL, select **File -> Run Script...**, and pick any script:
* `scripts/render_myoglobin.pml`
* `scripts/render_crambin.pml`
* `scripts/render_hemoglobin.pml`

### Method 2: Running via Command Line

```bash
pymol -qc scripts/render_myoglobin.pml
pymol -qc scripts/render_crambin.pml
pymol -qc scripts/render_hemoglobin.pml
```

### Essential PyMOL Command Reference

| Command | Action |
| :--- | :--- |
| `load data/1mbn.pdb, myoglobin` | Load structure coordinates from disk |
| `hide everything, myoglobin` | Clear default wireframe display |
| `show cartoon, myoglobin` | Render secondary structure ribbon |
| `color marine, ss h` | Color alpha helices marine blue |
| `color orange, ss s` | Color beta sheets orange |
| `color lightblue, ss l+''` | Color loops and coils light blue |
| `select heme, resn HEM` | Select prosthetic group |
| `show sticks, heme` | Display heme cofactor as sticks |
| `bg_color white` | Set crisp white background |
| `ray 1600, 1200` | Perform ray tracing |
| `png myoglobin_render.png` | Export high-resolution image |

## License

This project is open source and available under the MIT License.
