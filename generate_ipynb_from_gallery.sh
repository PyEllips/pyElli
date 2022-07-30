#!/bin/bash

cd examples/gallery

# Copy Basic usage example
sphx_glr_python_to_jupyter.py plot_01_basic_usage.py
mv plot_01_basic_usage.ipynb ../Basic\ Usage/Basic\ Usage.ipynb
cp SiO2onSi.ellips.nxs ../Basic\ Usage/
cp Si_Aspnes.mat ../Basic\ Usage/

# Copy SiO2 Si Müller Matrix example
sphx_glr_python_to_jupyter.py plot_SiO2_Si_MM.py
mv plot_SiO2_Si_MM.ipynb ../SiO2_Si\ Mueller\ Matrix/SiO2_Si\ Mueller\ Matrix.ipynb
cp Si_Aspnes.mat ../SiO2_Si\ Mueller\ Matrix/
cp Wafer_MM_70.txt ../SiO2_Si\ Mueller\ Matrix/

# Copy TiO2 Multilayer example
sphx_glr_python_to_jupyter.py plot_02_TiO2_multilayer.py
mv plot_02_TiO2_multilayer.ipynb ../TiO2\ Fit/TiO2\ Multilayerfit.ipynb
cp TiO2_400cycles.txt ../TiO2\ Fit/
cp Si_Aspnes.mat ../TiO2\ Fit/