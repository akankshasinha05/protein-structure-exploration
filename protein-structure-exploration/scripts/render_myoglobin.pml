reinitialize
load data/1mbn.pdb, 1mbn
hide everything, 1mbn
show cartoon, 1mbn
color marine, 1mbn and ss h
color orange, 1mbn and ss s
color lightblue, 1mbn and ss l+''
select heme, resn HEM
show sticks, heme
color firebrick, heme
select fe_atom, resn HEM and name FE
show spheres, fe_atom
color red, fe_atom
set sphere_scale, 0.6, fe_atom
bg_color white
set ray_shadows, 0
zoom 1mbn
png figures/myoglobin_1mbn_cartoon.png, width=1600, height=1200, dpi=300, ray=1
