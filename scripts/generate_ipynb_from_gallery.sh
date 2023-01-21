#!/bin/bash

cd examples/gallery

# Copy Basic usage example
sphx_glr_python_to_jupyter.py plot_01_basic_usage.py
mv plot_01_basic_usage.ipynb ../Basic\ Usage/Basic\ Usage.ipynb
cp SiO2onSi.ellips.nxs ../Basic\ Usage/

# Copy SiO2 Si Müller Matrix example
sphx_glr_python_to_jupyter.py plot_SiO2_Si_MM.py
mv plot_SiO2_Si_MM.ipynb ../SiO2_Si\ Mueller\ Matrix/SiO2_Si\ Mueller\ Matrix.ipynb
cp Wafer_MM_70.txt ../SiO2_Si\ Mueller\ Matrix/

# Copy TiO2 Multilayer example
sphx_glr_python_to_jupyter.py plot_02_TiO2_multilayer.py
mv plot_02_TiO2_multilayer.ipynb ../TiO2\ Fit/TiO2\ Multilayerfit.ipynb
cp TiO2_400cycles.txt ../TiO2\ Fit/

# Copy Bragg-Mirror
sphx_glr_python_to_jupyter.py plot_bragg_mirror.py
mv plot_bragg_mirror.ipynb ../Bragg-mirror/Bragg-Mirror.ipynb

# Copy Interface Reflection
sphx_glr_python_to_jupyter.py plot_interface_reflection.py
mv plot_interface_reflection.ipynb ../Interfaces/interface-reflection.ipynb

# Copy Cholesteric Liquid
sphx_glr_python_to_jupyter.py plot_cholesteric_lq.py
mv plot_cholesteric_lq.ipynb ../Liquid\ crystals/cholesteric-liquid.ipynb
