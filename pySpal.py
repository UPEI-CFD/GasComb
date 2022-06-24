# -*- coding: utf-8 -*-

"""
File is part of GasComb software. See licence file of the project.
Copyright 2022 Jiri Vondal
"""

import cantera as ct
import glob
import os.path as p

def ratio_vzduch(tpalivo, tvzduch, tpouzite_prvky, teplota, tlak):
    q_palivo = ct.Quantity(tpalivo, moles=1)
    q_vzduch = ct.Quantity(tvzduch, moles=1)

    q_smes = q_palivo + q_vzduch
    test_smes = ct.Solution(thermo='IdealGas', species=tpouzite_prvky)
    test_smes.TPX = teplota, tlak, q_smes.mole_fraction_dict()

    ratio = test_smes.get_equivalence_ratio(ignore=['NO'])
    return ratio


def set_water_X(gas, water_X):
    '''
    Changes water content in a gas to specified value (molar fraction).

    Parameters
    ----------
    gas : Object of type cantera.Solution() with water species included.
    water_X : Molar concentration of water to be set to: e.g. 0.05.

    Returns
    -------
    None.

    '''
    x = gas.X
    t, p = gas.TP
    i = gas.species_index('H2O')
    x = x*(1-water_X)/(1-x[i])  # Recalculates all species concentration.
    x[i] = water_X  # Sets final water molar fraction value as required.
    gas.X = x  # Assigns back species concentration to the gas.
    gas.TP = t, p


def set_water_phi(gas, water_phi):
    '''
    Changes water content in a gas to specified value of relative humidity. 
    It is reasonable to use only for temperature less then 100°C. 
    For higher temperature you might want Humidity ratio instead of Relative humidity.

    Parameters
    ----------
    gas : Object of type cantera.Solution() with water species included.
    water_phi : Relative humidity.

    Returns
    -------
    None.

    '''
    w = ct.Water()
    t, p = gas.TP
    w.TP = gas.TP
    p_sat = w.P_sat
    water_Y = 0.622*water_phi*p_sat/(gas.P-water_phi*p_sat)
    set_water_X(gas, 0)
    y = gas.Y
    i = gas.species_index('H2O')
    y[i] = water_Y  # Sets final water molar fraction value as required.
    y = y/(1+water_Y)  # Recalculates all species concentration.

    gas.Y = y  # Assigns back species concentration to the gas.
    gas.TP = t, p


def set_water_mw(gas, water_mw):
    '''
    Changes water content in a gas to specified value given by mass concentration [kg/m3] at standard condition.

    Parameters
    ----------
    gas : Object of type cantera.Solution() with H2O species included.

    water_mw : Mass concentration of water [kg/m3] at standard state conditions (0°C, 101325 Pa).

    Returns
    -------
    None.

    '''

    w = ct.Solution('gri30.yaml')
    w.TPX = 273.15, 101325, 'H2O:1'

    water_X = water_mw/w.density

    t, p = gas.TP
    x = gas.X
    i = gas.species_index('H2O')
    x = x*(1-water_X)/(1-x[i])  # Recalculates all species concentration.
    x[i] = water_X  # Sets final water molar fraction value as required.
    gas.X = x  # Assigns back species concentration to the gas.
    gas.TP = t, p


def set_O2_ref_X(gas, o2_X):
    '''
    Changes oxygen content in a gas to specified reference value (molar fraction).
    It is not correct method!!! Only correct way is to use iterative procedure
    with variable air flow rate to find proper match.

    Parameters
    ----------
    gas : Object of type cantera.Solution() with oxygen species included.
    o2_X : Molar concentration of oxygen to be set to: e.g. 0.03.

    Returns
    -------
    None.

    '''
    t, p = gas.TP
    x = gas.X
    i = gas.species_index('O2')
    x = x*(1-o2_X)/(1-x[i])  # Recalculates all species concentration.
    x[i] = o2_X  # Sets final water molar fraction value as required.
    # gas.X=x #Assigns back species concentration to the gas.
    gas.TPX = t, p, x


def calc_ref(gas, c_real, OR=10):
    """
    Parameters
    ----------
    gas : Object Quantity from Cantera.
    c_real : Concentration which should be converted to standard conditions according legislative conversion equation.
    OR : Reference Oxygen in units [%]!! Check the units before use!!!

    Returns
    -------
    Converted concentration for reference oxygen, dry gas and standard conditions.

    """
    pN = 101325
    tN = 273.15
    # OR = 10 #Reference oxygen

    O = gas.mole_fraction_dict()["O2"]*100
    t = gas.T
    p = gas.P
    try:
        W = gas.mole_fraction_dict()["H2O"]*100
    except KeyError:
        W = 0

    return c_real*pN*t/(tN*p)*100/(100-W)*(21-OR)/(21-O)


def getMechanisms():
    
    drs = ct.get_data_directories()
    mnms = []
    for d in drs:
        mnms += glob.glob(p.join(d, '*.yaml'))

    mnms = [m.split("\\")[-1] for m in mnms]

    return mnms

license_description="""<p>GasComb v0.1</p>
<p>GasComb is a basic GUI for Cantera libraries and few more tools. It allows calculations of stream mixing and set the gas mixture to a state of chemical equilibrium. Mixing is assumed at constant enthalpy and pressure (HP).</p>

============================================
<p>Author: Jiří Vondál, vondal@fme.vutbr.cz, Institute of Process Engineering, Faculty of Mechanical Engineering, Brno University of Technology</p>
---------------
<p>License: BSD license</p>
---
<p>Copyright 2022 Jiri Vondal</p>
<p>Copyright (c) 2001-2009, California Institute of Technology
All rights reserved.</p>

<p>Copyright (c) 2009 Sandia Corporation. Under the terms of
Contract AC04-94AL85000 with Sandia Corporation, the U.S. Government
retains certain rights in this software.</p>

<p>Copyright (c) 2011-2022, Cantera Developers.
All rights reserved.</p>

<p>Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
    Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
    Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.</p>

<p>THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</p>
"""
