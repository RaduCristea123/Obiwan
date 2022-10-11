general_parameters =  \
{'System': '\'Alpha\'',
 'Call sign': 'ino',
 'Laser_Pointing_Angle': 0,
 'Molecular_Calc': 0,
 'Latitude_degrees_north': 44.348,
 'Longitude_degrees_east': 26.029,
 'Altitude_meter_asl': 93.0}  # This should be float

# Change to channel_parameters to use all channels. For testing I define only photon counting channels below.
channel_parameters = \
{ '00355.p_an_p45': {'channel_ID': 1663,
         'Background_Low': 50000,
         'Background_High': 60000,
         'Laser_Shots': 3000,
         'LR_Input': 1,
         'DAQ_Range': 100.0,
         'Depolarization_Factor': 0,
         'Pol_Calib_Range_Min': 1000,
         'Pol_Calib_Range_Max': 3000},
 '00355.p_ph_p45': {'channel_ID': 1662,
         'Background_Low': 50000,
         'Background_High': 60000,
         'Laser_Shots': 3000,
         'LR_Input': 1,
         'DAQ_Range': 0,
         'Depolarization_Factor': 0,
         'Pol_Calib_Range_Min': 1000,
         'Pol_Calib_Range_Max': 3000},
 '00355.s_an_p45': {'channel_ID': 1661 ,
         'Background_Low': 50000,
         'Background_High': 60000,
         'Laser_Shots': 3000,
         'LR_Input': 1,
         'DAQ_Range': 20.0,
         'Pol_Calib_Range_Min': 1000,
         'Pol_Calib_Range_Max': 3000},
 '00355.s_ph_p45': {'channel_ID': 1664,
         'Background_Low': 50000,
         'Background_High': 60000,
         'Laser_Shots': 3000,
         'LR_Input': 1,
         'DAQ_Range': 0,
         'Pol_Calib_Range_Min': 1000,
         'Pol_Calib_Range_Max': 3000},
 '00355.p_an_m45': {'channel_ID': 1667,
         'Background_Low': 50000,
         'Background_High': 60000,
         'Laser_Shots': 3000,
         'LR_Input': 1,
         'DAQ_Range': 100.0,
         'Depolarization_Factor': 0,
         'Pol_Calib_Range_Min': 1000,
         'Pol_Calib_Range_Max': 3000},
 '00355.p_ph_m45': {'channel_ID': 1666,
         'Background_Low': 50000,
         'Background_High': 60000,
         'Laser_Shots': 3000,
         'LR_Input': 1,
         'DAQ_Range': 0,
         'Depolarization_Factor': 0,
         'Pol_Calib_Range_Min': 1000,
         'Pol_Calib_Range_Max': 3000},
 '00355.s_an_m45': {'channel_ID': 1665,
         'Background_Low': 50000,
         'Background_High': 60000,
         'Laser_Shots': 3000,
         'LR_Input': 1,
         'DAQ_Range': 20.0,
         'Pol_Calib_Range_Min': 1000,
         'Pol_Calib_Range_Max': 3000},
 '00355.s_ph_m45': {'channel_ID': 1668,
         'Background_Low': 50000,
         'Background_High': 60000,
         'Laser_Shots': 3000,
         'LR_Input': 1,
         'DAQ_Range': 0,
         'Pol_Calib_Range_Min': 1000,
         'Pol_Calib_Range_Max': 3000},
         }