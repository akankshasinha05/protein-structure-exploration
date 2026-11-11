reinitialize
load data/1crn.pdb, 1crn
hide everything, 1crn
show cartoon, 1crn
color skyblue, 1crn and ss h
color warmpink, 1crn and ss s
color palegreen, 1crn and ss l+''
select ss_bonds, elem S
show sticks, ss_bonds
color yellow, ss_bonds
bg_color white
set ray_shadows, 0
zoom 1crn
png figures/crambin_1crn_cartoon.png, width=1600, height=1200, dpi=300, ray=1
