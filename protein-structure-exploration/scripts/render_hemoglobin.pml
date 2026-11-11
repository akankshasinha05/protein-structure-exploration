reinitialize
load data/1hho.pdb, 1hho
hide everything, 1hho
show cartoon, 1hho
color cyan, chain A
color lightmagenta, chain B
select all_hemes, resn HEM
show sticks, all_hemes
color red, all_hemes
select iron_atoms, resn HEM and name FE
show spheres, iron_atoms
color ruby, iron_atoms
set sphere_scale, 0.7, iron_atoms
bg_color white
set ray_shadows, 0
zoom 1hho
png figures/hemoglobin_1hho_cartoon.png, width=1600, height=1200, dpi=300, ray=1
