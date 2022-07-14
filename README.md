
# GasComb
GasComb is a basic GUI for Cantera libraries and few more tools. It allows calculations of stream mixing and set the gas mixture to a state of chemical equilibrium. Mixing is assumed at constant enthalpy and pressure (HP).
All calculations are based on two simple examples from Cantera:
1) Mixing: https://cantera.org/examples/python/thermo/mixing.py.html
2) Getting Started for Chemical Equilibrium: https://cantera.org/tutorials/python-tutorial.html

My goal besides the reactions were also material properties of gases. It is often difficult to get correct properties for various flue gas concentrations. Cantera and underliyng mechanism files with transport properties offers great source of gas properties:
- Specific heat capacity
- Density
- Viscosity
- Mean molecular Weight
- Enthalpy
- Entropy

... all pressure and temperature dependent.

## Download
- Standard windows installation: https://drive.google.com/file/d/1n8N4ozoeHgXyfXaJMtfWfqpS_Nl9MXkZ/view?usp=sharing
- Portable windows installation: https://drive.google.com/file/d/1zfaSSp_Zqo0gVQqGXGhVFANOs2Gys_lY/view?usp=sharing

## How to install and run with Python from source code
1) Download and install Miniconda: https://docs.conda.io/en/latest/miniconda.html 
2) Open Anaconda Powershell Prompt and install cantera libraries: 

```conda create --name ct-env --channel cantera cantera matplotlib pyqt```

3) Create folder and download provided files from this repository.
4) In Anaconda Powershell Prompt navigate to the folder, activate environment: 

```conda activate ct-env```

and run: 

```python ./GasComb_run.py```
        
GUI should open and you can do your calculations.

## Video
Introduction 1: https://youtu.be/EJFUkNUmSRU

Introduction 2: https://youtu.be/e_cZFs-iPAw

Material Properties: https://youtu.be/HktMvOGQKXY

## Screenshot

![GasComb screenshot](/help/images/GasComb_example1.PNG)

