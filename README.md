# Tunnel-diode-Characterization-and-Modeling


In this repository we try to measure and export the  IV curve of the AI301A tunnel diode.

Tunnel DIODES catalogue:
https://w140.com/tekwiki/wiki/Russian_tunnel_diodes

We use NI MyDAQ hardware and MATLAB software for the measurement.


Hardware: NI MyDAQ, RESISTOR, Capasitor, Tunnel DIODE A301A
Software: 
MATLAB script for capture the measurement.
Python scripts for ploting the results and fitting.


<p align="center">
  <img width="460" height="300" src="https://github.com/daskals/Tunnel-diode-Characterization-and-Modeling/blob/main/MyDAQ_setup.png">
</p>

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


Results:

<p align="center">
  <img width="460" height="300" src="https://github.com/daskals/Tunnel-diode-Characterization-and-Modeling/blob/main/Python%20Scripts/My_diodes_data.png">
</p>


<p align="center">
  <img width="460" height="300" src="https://github.com/daskals/Tunnel-diode-Characterization-and-Modeling/blob/main/Python%20Scripts/My_diode_model.png">
</p>
