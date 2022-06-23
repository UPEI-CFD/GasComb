
# GasComb
GasComb is a basic GUI for Cantera libraries and few more tools. It allows calculations of stream mixing and set the gas mixture to a state of chemical equilibrium. Mixing is assumed at constant enthalpy and pressure (HP).

## How to install and run
1) Download and install Miniconda: https://docs.conda.io/en/latest/miniconda.html 
2) Open Anaconda Powershell Prompt and install cantera libraries: conda create --name ct-env --channel cantera cantera matplotlib pyqt
3) Create folder and download provided fiels from this repository.
4) In Anaconda Powershell Prompt navigate to the folder, activate environment: conda activate ct-env
and run: python ./SpalGas_run.py

GUI should open and you can do your calculations.
