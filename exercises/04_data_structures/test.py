

string = ["10.255.160.245 3d_ex1",
"10.255.160.1 3d_l1",
"10.255.160.2 3d_l2",
"10.255.160.3 3d_l3",
"10.255.160.4 3d_l4",
"10.255.160.5 3d_l5",
"10.255.160.6 3d_l6",
"10.255.160.7 3d_l7",
"10.255.160.8 3d_l8",
"10.255.160.9 3d_l9",
"10.255.160.241 3d_s1",
"10.255.160.242 3d_s2",
"10.20.97.1 dl_edge",
"10.20.97.8 dl_ex4200",
"10.20.96.4 dl_fg1-1",
"10.20.97.17 dl_fg_ssl",
"10.255.64.10 dl_l10",
"10.255.64.11 dl_l11",
"10.255.64.12 dl_l12",
"10.255.64.13 dl_l13",
"10.255.64.14 dl_l14",
"10.255.64.15 dl_l15",
"10.255.64.16 dl_l16",
"10.255.64.17 dl_l17",
"10.255.64.18 dl_l18",
"10.255.64.19 dl_l19",
"10.255.64.23 dl_l23",
"10.255.64.24 dl_l24",
"10.255.64.25 dl_l25",
"10.255.64.26 dl_l26",
"10.255.64.27 dl_l27",
"10.255.64.3 dl_l3",
"10.255.64.4 dl_l4",
"10.255.64.5 dl_l5",
"10.255.64.6 dl_l6",
"10.255.64.7 dl_l7",
"10.255.64.8 dl_l8",
"10.255.64.9 dl_l9",
"10.20.97.33 dl_r1",
"10.255.64.241 dl_s1",
"10.255.64.242 dl_s2",
"10.255.128.1 dll_l1",
"10.255.128.2 dll_l2",
"10.255.128.3 dll_l3",
"10.255.128.4 dll_l4",
"10.255.128.254 dll_s1",
"10.255.128.255 dll_s2",
"10.10.97.1 dp_edge",
"10.10.97.26 dp_ex2",
"10.10.97.25 dp_fg1-1",
"10.255.32.1 dp_l1",
"10.255.32.10 dp_l10",
"10.255.32.11 dp_l11",
"10.255.32.12 dp_l12",
"10.255.32.13 dp_l13",
"10.255.32.14 dp_l14",
"10.255.32.15 dp_l15",
"10.255.32.16 dp_l16",
"10.255.32.17 dp_l17",
"10.255.32.18 dp_l18",
"10.255.32.19 dp_l19",
"10.255.32.2 dp_l2",
"10.10.97.7 dp_l2_kvm",
"10.255.32.4 dp_l4",
"10.255.32.5 dp_l5",
"10.255.32.6 dp_l6",
"10.255.32.7 dp_l7",
"10.255.32.8 dp_l8",
"10.255.32.9 dp_l9",
"10.10.97.33 dp_r1",
"10.255.32.241 dp_s1",
"10.255.32.242 dp_s2",
"10.41.255.3 dpl_l1",
"10.41.255.4 dpl_l2",
"10.41.255.5 dpl_l3",
"10.255.96.4 dpl_l4",
"10.41.255.1 dpl_s1",
"10.41.254.8 dpl_s2",
"10.255.160.10 3d_l10",
"10.255.160.11 3d_l11",
"10.20.97.14 dl_core1",
"10.20.97.18 dl_core2",
"10.10.97.18 dp_core1",
"10.10.97.17 dp_core2",
"10.40.223.221 3d_core1",
"10.40.223.222 3d_core2"]

for name in string: 
    host = name.split()
    print(host [1])
