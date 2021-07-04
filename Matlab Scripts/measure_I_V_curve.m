%#######################################################
%#     Spiros Daskalakis                               #
%#     Last Revision: 03/07/2021                       #
%#     Matlab Version:  R2019b Edu                     #    
%#     Email: Daskalakispiros@gmail.com                #
%#######################################################

clc;
clear all;
close all;

daq.getDevices
s = daq.createSession('ni');

s.addAnalogInputChannel('myDAQ1', 'ai0', 'Voltage');
s.addAnalogInputChannel('myDAQ1', 'ai1', 'Voltage');
s.addAnalogOutputChannel('myDAQ1','ao0','Voltage');  
s.Rate = 2;
s.Channels(1).Range = [-2 2];


counter=1;
Resistor =52.4;

% Display the results
figure(1);



vout=0:0.005:0.7;

v_reading=zeros(1,length(vout));
i_reading=zeros(1,length(vout));


 while counter<= length(vout)
    value=vout(counter);
    %setup the output channel with voltage value 
    queueOutputData(s,value);
    s.startForeground;
    
    pause(1) %wait in seconds
    % read the two analog Channels
    [singleReading, triggerTime] = s.inputSingleScan;
    % read the volgate across the diode
    VOLT=singleReading(1);
    v_reading(counter)=VOLT*1000;
    % read the volgate across the resistor
    VOLT_res=singleReading(2);
    current=VOLT_res/50;
    
    %prompt = 'What is the current value for ?';
    %curr = input(prompt)/1000
    
    % convert current to mA
    i_reading(counter)=current*1000;
    counter = counter + 1;
    
    %plot the I V values
    plot(v_reading, i_reading, 'o'); 
    drawnow
    title('AI301A  I V curve');
    xlabel('Voltage (mV)'); 
    ylabel('Current (mA)');
 end
 


save('V_I_A301A_4b','v_reading','i_reading')






