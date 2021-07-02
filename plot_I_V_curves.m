%#######################################################
%#     Spiros Daskalakis--Ricardo Mota                 #
%#     Last Revision: 01/07/2021                       #
%#     Python Version:  3.9                            #
%#     Matlab Version:  R2019b Edu                     #    
%#     Email: Daskalakispiros@gmail.com                #
%#######################################################



clc;
clear all;
close all;


A301A_1=load('V_I_A301A_1','v_reading','i_reading')



% Display the results
figure1= figure;
axes1  = axes('Parent',figure1,'YGrid','on','XGrid','on','FontSize',18);
plot(A301A_1.v_reading, A301A_1.i_reading, 'LineWidth',1.5,'Color',[0 0 0]);
hold on

set(axes1,'FontSize',18)
title('AI301A  I V curve');
grid(axes1,'on');
xlabel('Voltage (mV)', 'FontSize',18); 
ylabel('Current (mA)', 'FontSize',18);
legend('Diode 1');
set(0, 'DefaultAxesFontName', 'Arial'); 
print(figure1,'-depsc', '-tiff', '-r300', 'A301A_IV.eps');
print(figure1,'-dpdf', 'A301A_IV.pdf');

 








