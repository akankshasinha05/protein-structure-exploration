import matplotlib.pyplot as plt
import numpy as np

def generate_structure_levels_diagram(output_path='figures/protein_structural_levels.png'):
    fig, axes = plt.subplots(1, 4, figsize=(14, 4))

    ax = axes[0]
    ax.set_title('1. Primary Structure', fontsize=11, fontweight='bold', pad=10)
    beads = ['Ala', 'Gly', 'Leu', 'Val', 'Ser', 'Lys']
    colors = ['lightcoral', 'cornflowerblue', 'mediumaquamarine', 'khaki', 'plum', 'lightsalmon']
    for i, (b, c) in enumerate(zip(beads, colors)):
        circle = plt.Circle((0.5, 0.85 - i * 0.14), 0.055, color=c, ec='black', lw=1.2)
        ax.add_patch(circle)
        ax.text(0.5, 0.85 - i * 0.14, b, ha='center', va='center', fontsize=8, fontweight='bold')
        if i < len(beads) - 1:
            ax.plot([0.5, 0.5], [0.85 - i * 0.14 - 0.055, 0.85 - (i + 1) * 0.14 + 0.055], 'k-', lw=1.5)
    ax.text(0.5, 0.05, 'Linear Amino Acid Chain\n(Peptide Bonds)', ha='center', fontsize=9)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    ax = axes[1]
    ax.set_title('2. Secondary Structure', fontsize=11, fontweight='bold', pad=10)
    t = np.linspace(0, 4 * np.pi, 200)
    x = 0.35 + 0.12 * np.sin(t)
    y = np.linspace(0.25, 0.85, 200)
    ax.plot(x, y, color='cornflowerblue', lw=3, label='Alpha Helix')
    ax.arrow(0.7, 0.25, 0, 0.55, head_width=0.06, head_length=0.06, fc='salmon', ec='black', lw=1.2)
    ax.arrow(0.82, 0.85, 0, -0.55, head_width=0.06, head_length=0.06, fc='salmon', ec='black', lw=1.2)
    ax.text(0.35, 0.18, 'Alpha Helix\n(Spiral)', ha='center', fontsize=8)
    ax.text(0.76, 0.18, 'Beta Sheet\n(Strands)', ha='center', fontsize=8)
    ax.text(0.5, 0.05, 'Local Backbone Folding\n(Hydrogen Bonds)', ha='center', fontsize=9)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    ax = axes[2]
    ax.set_title('3. Tertiary Structure', fontsize=11, fontweight='bold', pad=10)
    theta = np.linspace(0, 8 * np.pi, 500)
    r = 0.25 + 0.08 * np.sin(3 * theta)
    tx = 0.5 + r * np.cos(theta) * 0.9
    ty = 0.55 + r * np.sin(theta) * 0.8
    ax.plot(tx, ty, color='mediumpurple', lw=2.5)
    ax.plot([0.42, 0.58], [0.55, 0.55], 'y--', lw=2)
    ax.text(0.5, 0.58, 'S-S bond', ha='center', fontsize=7, color='goldenrod', fontweight='bold')
    ax.text(0.5, 0.05, '3D Spatial Fold\n(Hydrophobic & Disulfides)', ha='center', fontsize=9)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    ax = axes[3]
    ax.set_title('4. Quaternary Structure', fontsize=11, fontweight='bold', pad=10)
    subunits = [
        (0.35, 0.65, 'Alpha 1', 'skyblue'),
        (0.65, 0.65, 'Beta 1', 'lightpink'),
        (0.35, 0.38, 'Beta 2', 'lightpink'),
        (0.65, 0.38, 'Alpha 2', 'skyblue')
    ]
    for cx, cy, label, c in subunits:
        circle = plt.Circle((cx, cy), 0.13, color=c, ec='black', lw=1.2)
        ax.add_patch(circle)
        ax.text(cx, cy, label, ha='center', va='center', fontsize=8, fontweight='bold')
    ax.text(0.5, 0.05, 'Multi-Subunit Complex\n(e.g., Hemoglobin Tetramer)', ha='center', fontsize=9)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

def generate_helix_sheet_diagram(output_path='figures/alpha_helix_vs_beta_sheet.png'):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    ax = axes[0]
    ax.set_title('Alpha Helix Architecture', fontsize=11, fontweight='bold', pad=12)
    t = np.linspace(0, 6 * np.pi, 400)
    x = 0.5 + 0.22 * np.sin(t)
    y = np.linspace(0.15, 0.85, 400)
    ax.plot(x, y, color='royalblue', lw=3.5)
    for i in range(1, 5):
        y_pos = 0.15 + i * 0.14
        ax.plot([0.38, 0.38], [y_pos, y_pos + 0.10], 'r--', lw=1.5)
        ax.text(0.35, y_pos + 0.05, 'H-bond', color='crimson', fontsize=7, ha='right')
    ax.text(0.5, 0.05, '3.6 amino acid residues per turn\nHydrogen bond between C=O(i) and N-H(i+4)', ha='center', fontsize=9)
    ax.set_xlim(0.1, 0.9)
    ax.set_ylim(0, 1)
    ax.axis('off')

    ax = axes[1]
    ax.set_title('Beta Pleated Sheet Architecture', fontsize=11, fontweight='bold', pad=12)
    ax.arrow(0.35, 0.2, 0, 0.6, head_width=0.07, head_length=0.08, fc='coral', ec='black', lw=1.5)
    ax.arrow(0.65, 0.8, 0, -0.6, head_width=0.07, head_length=0.08, fc='coral', ec='black', lw=1.5)
    for y_pos in [0.35, 0.48, 0.61]:
        ax.plot([0.37, 0.63], [y_pos, y_pos], 'b--', lw=1.5)
        ax.text(0.5, y_pos + 0.02, 'H-bond', color='darkblue', fontsize=7, ha='center')
    ax.text(0.35, 0.12, 'Strand A (N to C)', ha='center', fontsize=8)
    ax.text(0.65, 0.12, 'Strand B (C to N)', ha='center', fontsize=8)
    ax.text(0.5, 0.05, 'Antiparallel Beta Strands\nInter-strand backbone hydrogen bonds', ha='center', fontsize=9)
    ax.set_xlim(0.1, 0.9)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

if __name__ == '__main__':
    generate_structure_levels_diagram('figures/protein_structural_levels.png')
    generate_helix_sheet_diagram('figures/alpha_helix_vs_beta_sheet.png')
    print('Diagrams generated successfully.')
