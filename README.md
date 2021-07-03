# Tunnel-diode-Characterization-and-Modeling


In this repository we try to measure and export the  IV curve of the AI301A tunnel diode.

We use NI MyDAQ and MATLAB softaware for the measurement.

Hardware: NI MyDAQ, RESISTOR, Capasitor, Tunnel DIODE A301A
Software: 
MATLAB script for capture the measurement.
Python scripts for ploting the results and fitting.


Meseurement Setup Connectivity:  
DAQ PINS

AO_0 ====> RESISTOR  
Ao_0 GND ====>  GND  


AI_0+ ====> DIODE Anode  
AI_0- ====> GND  


AI_1+ ====> RESISTOR +  
AI_1- ====> RESISTOR -  

DIODE + (Anode) =====> RESISTOR  
DIODE - (Cathode)=====> GND  
