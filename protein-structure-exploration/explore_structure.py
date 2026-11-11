import sys
import os
import matplotlib.pyplot as plt

AA_3TO1 = {
    'ALA': 'A', 'CYS': 'C', 'ASP': 'D', 'GLU': 'E', 'PHE': 'F',
    'GLY': 'G', 'HIS': 'H', 'ILE': 'I', 'LYS': 'K', 'LEU': 'L',
    'MET': 'M', 'ASN': 'N', 'PRO': 'P', 'GLN': 'Q', 'ARG': 'R',
    'SER': 'S', 'THR': 'T', 'VAL': 'V', 'TRP': 'W', 'TYR': 'Y'
}

def parse_pdb_file(filepath):
    data = {
        'title': '',
        'sequences': {},
        'helices': [],
        'sheets': [],
        'disulfides': [],
        'ligands': set(),
        'num_atoms': 0
    }

    with open(filepath, 'r') as f:
        for line in f:
            record = line[:6].strip()

            if record == 'HEADER':
                data['header'] = line[10:50].strip()
            elif record == 'TITLE':
                data['title'] += line[10:70].strip() + ' '
            elif record == 'SEQRES':
                chain = line[11]
                residues = line[19:70].split()
                if chain not in data['sequences']:
                    data['sequences'][chain] = []
                data['sequences'][chain].extend(residues)
            elif record == 'HELIX':
                helix_id = line[11:14].strip()
                chain = line[19]
                start_res = int(line[21:25].strip())
                end_res = int(line[33:37].strip())
                length = int(line[71:76].strip()) if len(line) >= 76 else (end_res - start_res + 1)
                data['helices'].append({'id': helix_id, 'chain': chain, 'start': start_res, 'end': end_res, 'length': length})
            elif record == 'SHEET':
                sheet_id = line[11:14].strip()
                chain = line[21]
                start_res = int(line[22:26].strip())
                end_res = int(line[33:37].strip())
                data['sheets'].append({'id': sheet_id, 'chain': chain, 'start': start_res, 'end': end_res})
            elif record == 'SSBOND':
                chain1 = line[15]
                res1 = line[17:21].strip()
                chain2 = line[29]
                res2 = line[31:35].strip()
                data['disulfides'].append((chain1, res1, chain2, res2))
            elif record == 'HETATM':
                resname = line[17:20].strip()
                if resname not in ['HOH', 'WAT']:
                    data['ligands'].add(resname)
            elif record == 'ATOM':
                data['num_atoms'] += 1

    return data

def get_amino_acid_counts(res_list):
    counts = {}
    for res in res_list:
        one_letter = AA_3TO1.get(res, 'X')
        counts[one_letter] = counts.get(one_letter, 0) + 1
    return counts

def plot_secondary_structures(results, output_path='figures/secondary_structure_composition.png'):
    names = list(results.keys())
    helix_pcts = []
    sheet_pcts = []
    loop_pcts = []

    for name in names:
        tot_res = results[name]['total_residues']
        helix_res = results[name]['helix_residues']
        sheet_res = results[name]['sheet_residues']
        loop_res = max(0, tot_res - (helix_res + sheet_res))

        helix_pcts.append((helix_res / tot_res) * 100 if tot_res > 0 else 0)
        sheet_pcts.append((sheet_res / tot_res) * 100 if tot_res > 0 else 0)
        loop_pcts.append((loop_res / tot_res) * 100 if tot_res > 0 else 0)

    fig, ax = plt.subplots(figsize=(8, 5))
    bar_width = 0.55
    x = range(len(names))

    ax.bar(x, helix_pcts, width=bar_width, label='Alpha Helix (%)', color='cornflowerblue', edgecolor='black')
    ax.bar(x, sheet_pcts, width=bar_width, bottom=helix_pcts, label='Beta Sheet (%)', color='salmon', edgecolor='black')
    ax.bar(x, loop_pcts, width=bar_width, bottom=[i + j for i, j in zip(helix_pcts, sheet_pcts)], label='Coil / Loop (%)', color='lightgray', edgecolor='black')

    ax.set_title('Secondary Structure Composition Across Explored Proteins', fontsize=12, pad=12)
    ax.set_xlabel('PDB Entry', fontsize=10)
    ax.set_ylabel('Percentage of Residues (%)', fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=10)
    ax.legend(loc='upper right', frameon=True)
    ax.grid(axis='y', linestyle='--', alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

def main():
    pdb_dir = 'data'
    pdb_files = [f for f in os.listdir(pdb_dir) if f.endswith('.pdb')]

    if not pdb_files:
        print("No PDB files found in data directory.")
        return

    results = {}

    for pdb_file in sorted(pdb_files):
        entry_name = pdb_file.replace('.pdb', '').upper()
        filepath = os.path.join(pdb_dir, pdb_file)
        data = parse_pdb_file(filepath)

        total_residues = sum(len(res_list) for res_list in data['sequences'].values())
        helix_res_count = sum(h['length'] for h in data['helices'])
        sheet_res_count = sum(s['end'] - s['start'] + 1 for s in data['sheets'])

        results[entry_name] = {
            'total_residues': total_residues,
            'helix_residues': helix_res_count,
            'sheet_residues': sheet_res_count,
            'num_helices': len(data['helices']),
            'num_sheets': len(data['sheets']),
            'num_disulfides': len(data['disulfides']),
            'ligands': list(data['ligands']),
            'chains': list(data['sequences'].keys())
        }

        print("=" * 60)
        print(f"PDB ID: {entry_name}")
        print(f"Title: {data['title'].strip()[:65]}")
        print(f"Chains: {', '.join(data['sequences'].keys())}")
        print(f"Total Residues: {total_residues}")
        print(f"Alpha Helices: {len(data['helices'])} ({helix_res_count} residues)")
        print(f"Beta Sheets: {len(data['sheets'])} ({sheet_res_count} residues)")
        print(f"Disulfide Bonds: {len(data['disulfides'])}")
        print(f"Ligands / Heteroatoms: {', '.join(data['ligands']) if data['ligands'] else 'None'}")

        for chain, residues in data['sequences'].items():
            one_letter_seq = ''.join([AA_3TO1.get(r, 'X') for r in residues])
            print(f"Chain {chain} Sequence ({len(residues)} aa): {one_letter_seq[:40]}...")

    plot_secondary_structures(results, 'figures/secondary_structure_composition.png')
    print("\nGenerated comparative chart: figures/secondary_structure_composition.png")

if __name__ == '__main__':
    main()
