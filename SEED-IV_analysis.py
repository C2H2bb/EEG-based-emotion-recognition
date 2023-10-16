from scipy.io import loadmat
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Labels for each trial within each session for each subject (for eye data, trials correspond to the shown clips)
# 0: neutral, 1: sad, 2: fear, 3: happy
# session1_label = [1, 2, 3, 0, 2, 0, 0, 1, 0, 1, 2, 1, 1, 1, 2, 3, 2, 2, 3, 3, 0, 3, 0, 3];
# session2_label = [2, 1, 3, 0, 0, 2, 0, 2, 3, 3, 2, 3, 2, 0, 1, 1, 2, 1, 0, 3, 0, 1, 3, 1];
# session3_label = [1, 2, 2, 1, 3, 3, 3, 1, 1, 2, 1, 0, 2, 3, 3, 0, 2, 3, 0, 0, 2, 0, 1, 0];

# RAW EEG DATA (Raw EEG signal data)
print('RAW EEG DATA - Subject 1 - Session 1')

channelsEEG = ["FP1", "FPZ", "FP2", "AF3", "AF4", "F7", "F5", "F3", "F1", "FZ", "F2", "F4", "F6", "F8", "FT7", "FC5", "FC3", "FC1",
               "FCZ", "FC2", "FC4", "FC6", "FT8", "T7", "C5", "C3", "C1", "CZ", "C2", "C4", "C6", "T8", "TP7", "CP5", "CP3", "CP1",
               "CPZ", "CP2", "CP4", "CP6", "TP8", "P7", "P5", "P3", "P1", "PZ", "P2", "P4", "P6", "P8", "PO7", "PO5", "PO3", "POZ",
               "PO4", "PO6", "PO8", "CB1", "O1", "OZ", "O2", "CB2"]


rawDataEEGExample = loadmat('SEED_IV/eeg_raw_data/1/1_20160518.mat')
keysRawData = [key for key, values in rawDataEEGExample.items() if key != '__header__' and key != '__version__' and key != '__globals__']

print(keysRawData)
print(type(rawDataEEGExample['cz_eeg1']))
print(rawDataEEGExample['cz_eeg1'].shape)

rawDataEEG_df = pd.DataFrame(rawDataEEGExample['cz_eeg2'], index=channelsEEG)
print("1st Trial")
print(rawDataEEG_df)

print("///////////////////////////////////////////////\n")
# PROCESSED EEG DATA (Features extracted from raw signals)
print('PROCESSED EEG DATA - Subject 1 - Session 1')
columnsFreq = ['delta (1-4 Hz)', 'theta (4-8 Hz)', 'alpha (8-14 Hz)', 'beta (4-31 Hz)', 'gamma (31-50 Hz)']
# Change the path here to the required file
procDataEEGExample = loadmat('SEED_IV/eeg_feature_smooth/1/1_20160518.mat')
keysProcDataEEG = [key for key, values in procDataEEGExample.items() if key != '__header__' and key != '__version__' and key != '__globals__']
print(keysProcDataEEG)

print("Differential Entropy - Moving Average - Trial 1 (de_movingAve1)")
print(type(procDataEEGExample['de_movingAve1']))
print(procDataEEGExample['de_movingAve1'].shape)
procDataEEG_df1 = pd.DataFrame(procDataEEGExample['de_movingAve1'][0], columns=columnsFreq)
print("channel number: 1; rows: time frame; columns: frequency bands")
print(procDataEEG_df1)

print("Differential Entropy - Linear Dynamic System - Trial 1 (de_LDS1)")
print(type(procDataEEGExample['de_LDS1']))
print(procDataEEGExample['de_LDS1'].shape)
procDataEEG_df2 = pd.DataFrame(procDataEEGExample['de_LDS1'][0], columns=columnsFreq)
print("channel number: 1; rows: time frame; columns: frequency bands")
print(procDataEEG_df2)

print("\nPower Spectral Density - Moving Average - Trial 1 (psd_movingAve1)")
print(type(procDataEEGExample['psd_movingAve1']))
print(procDataEEGExample['psd_movingAve1'].shape)
procDataEEG_df3 = pd.DataFrame(procDataEEGExample['psd_movingAve1'][0], columns=columnsFreq)
print("channel number: 1; rows: time frame; columns: frequency bands")
print(procDataEEG_df3)

print("\nPower Spectral Density - Linear Dynamic System - Trial 1 (psd_LDS1)")
print(type(procDataEEGExample['psd_LDS1']))
print(procDataEEGExample['psd_LDS1'].shape)
procDataEEG_df4 = pd.DataFrame(procDataEEGExample['psd_LDS1'][0], columns=columnsFreq)
print("channel number: 1; rows: time frame; columns: frequency bands")
print(procDataEEG_df4)

print("///////////////////////////////////////////////\n")
# RAW EYE DATA (Raw eye tracking data)
print('\nRAW EYE DATA - Subject 1 - Session 1')
print("Blinking Data")

rawDataEyesExample = loadmat('SEED_IV/eye_raw_data/1_20160518_blink.mat')
keysRawDataEyes = [key for key, values in rawDataEyesExample.items() if key != '__header__' and key != '__version__' and key != '__globals__']
print(keysRawDataEyes)
print(type(rawDataEyesExample['Eye_Blink']))
print(rawDataEyesExample['Eye_Blink'].shape)
print(type(rawDataEyesExample['Eye_Blink'][0]))
rawDataEyes_df = pd.DataFrame(rawDataEyesExample['Eye_Blink'], columns=['Blinking Time'])
print("Rows: movie clips; Number of Elements in Row: number of blinks in the movie clip; Data in row: time of the blink")
print(rawDataEyes_df)

print("\nStatistical Data")
rawDataEyesExample = loadmat('SEED_IV/eye_raw_data/1_20160518_event.mat')
keysRawDataEyes = [key for key, values in rawDataEyesExample.items() if key != '__header__' and key != '__version__' and key != '__globals__']
print(keysRawDataEyes)
print(type(rawDataEyesExample['Eye_Event']))
print(rawDataEyesExample['Eye_Event'].shape)
print(type(rawDataEyesExample['Eye_Event'][0]))
rawDataEyes_df = pd.DataFrame(rawDataEyesExample['Eye_Event'], columns=["Statistics"])
print("Rows: movie clips; Data in row: Statistical Data")
print(rawDataEyes_df)

print("\nEye Fixation Data")
rawDataEyesExample = loadmat('SEED_IV/eye_raw_data/1_20160518_fixation.mat')
keysRawDataEyes = [key for key, values in rawDataEyesExample.items() if key != '__header__' and key != '__version__' and key != '__globals__']
print(keysRawDataEyes)
print(type(rawDataEyesExample['Eye_Fixation']))
print(rawDataEyesExample['Eye_Fixation'].shape)
print(type(rawDataEyesExample['Eye_Fixation'][0]))
rawDataEyes_df = pd.DataFrame(rawDataEyesExample['Eye_Fixation'], columns=['Fixation Time'])
print("Rows: movie clips; Number of Elements in Row: number of fixations in the movie clip; Data in row: time of the fixation")
print(rawDataEyes_df)

print("\nPupil Data")
rawDataEyesExample = loadmat('SEED_IV/eye_raw_data/1_20160518_pupil.mat')
keysRawDataEyes = [key for key, values in rawDataEyesExample.items() if key != '__header__' and key != '__version__' and key != '__globals__']
print(keysRawDataEyes)
print(type(rawDataEyesExample['Eye_Pupil']))
print(rawDataEyesExample['Eye_Pupil'].shape)
print(type(rawDataEyesExample['Eye_Pupil'][0]))
rawDataEyes_df = pd.DataFrame(rawDataEyesExample['Eye_Pupil'])
print("Rows: movie clips; Number of Elements in Row: number of pupil recordings in the movie clip; Data in row: Four Features for every pupil recording")
print("Average Pupil Size [px] X, Average Pupils Size [px] Y, Dispersion X, Dispersion Y")
print(rawDataEyes_df)

print("\nSaccade Data")
rawDataEyesExample = loadmat('SEED_IV/eye_raw_data/1_20160518_saccade.mat')
keysRawDataEyes = [key for key, values in rawDataEyesExample.items() if key != '__header__' and key != '__version__' and key != '__globals__']
print(keysRawDataEyes)
print(type(rawDataEyesExample['Eye_Saccade']))
print(rawDataEyesExample['Eye_Saccade'].shape)
print(type(rawDataEyesExample['Eye_Saccade'][0]))
rawDataEyes_df = pd.DataFrame(rawDataEyesExample['Eye_Saccade'])
print("Rows: movie clips; Number of Elements in Row: number of saccades in the movie clip; Data in row: Feature of every saccade record")
print("Saccade Duration [ms], Amplitude[°]")
print(rawDataEyes_df)



print("///////////////////////////////////////////////\n")
# PROCESSED EYE DATA (Features extracted from eye movement)
print('PROCESSED EYE DATA - Subject 1')
rows = []
procDataEyesExample = loadmat('SEED_IV/eye_feature_smooth/1/1_20160518.mat')
keysProcDataEyes = [key for key, values in procDataEyesExample.items() if key != '__header__' and key != '__version__' and key != '__globals__']
print("These are for each session")
print(keysProcDataEyes)
print(type(procDataEyesExample['eye_1']))
print(procDataEyesExample['eye_1'].shape)
procDataEyes_df = pd.DataFrame(procDataEyesExample['eye_1'])
print("Session 1")
print("Rows: type of feature; Columns: data samples")
print("Features: 1-12: Pupil diameter (X and Y); 13-16: Dispersion (X and Y); 17-18: Fixation duration (ms); 19-22: Saccade; 23-31: Event statistics")

procDataEyes_df = procDataEyes_df.transpose()
eye_features_index = ["Mean Pupil Diameter X", "Mean Pupil Diameter Y", "STD Pupil Diameter X", "STD Pupil Diameter Y", "DE (0-0.2Hz) Pupil Diameter X",
                      "DE (0-0.2) Pupil Diameter Y", "DE (0.2-0.4Hz) Pupil Diameter X", "DE (0.2-0.4Hz) Pupil Diameter Y", "DE (0.4-0.6Hz) Pupil Diameter X",
                      "DE (0.4-0.6Hz) Pupil Diameter Y", "DE (0.6-1Hz) Pupil Diameter X", "DE (0.6-1Hz) Pupil Diameter Y", "Mean Dispersion X", "Mean Dispersion Y",
                      "STD Dispersion X", "STD Dispersion Y", "Mean Fixation Duration", "STD Fixation Duration", #"Mean Blink Duration", "STD Blink Duration",
                      "Mean Saccade Duration", "Mean Saccade Amplitude", "STD Saccade Duration", "STD Saccade Amplitude", "Blink Frequency", "Fixation Frequency",
                      "Maximum Fixation duration", "Total Fixation Dispersion", "Maximum Fixation Dispersion", "Saccade Frequency", "Average Saccade Duration",
                      "Average Saccade Amplitude", "Average Saccade Latency"]
procDataEyes_df.columns = eye_features_index
print(procDataEyes_df)



# Visualization for Raw EEG data
plt.figure(figsize=(14,7))
plt.title("EEG Time Series for Channel FP1")
plt.plot(rawDataEEG_df.loc["FP1", :])
plt.xlabel("Time Points")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# Visualization for Processed EEG data (heatmap for frequency bands)
plt.figure(figsize=(10,6))
sns.heatmap(procDataEEG_df1.transpose(), cmap="YlGnBu", linewidths=.5)
plt.title("Differential Entropy - Moving Average - Trial 1")
plt.xlabel("Time Points")
plt.ylabel("Frequency Bands")
plt.show()



#print(rawDataEyesExample.keys())
# Visualization for Raw Eye Data (Blinking Data)
blinks_per_clip = [len(blink) for blink in rawDataEyesExample['Eye_Saccade'][0]]
plt.figure(figsize=(12,6))
plt.bar(range(len(blinks_per_clip)), blinks_per_clip)
plt.title("Number of Blinks per Movie Clip")
plt.xlabel("Movie Clip Index")
plt.ylabel("Number of Blinks")
plt.grid(True, axis='y')
plt.show()



# Visualization for Processed Eye Data
plt.figure(figsize=(12,6))
plt.title("Mean Pupil Diameter X across different samples")
plt.plot(procDataEyes_df["Mean Pupil Diameter X"])
plt.xlabel("Sample Index")
plt.ylabel("Mean Pupil Diameter X Value")
plt.grid(True)
plt.show()



plt.figure(figsize=(15, 10))
sns.violinplot(data=procDataEEG_df1)
plt.title("Distribution of EEG Data Features (Differential Entropy - Moving Average - Trial 1)")
plt.ylabel("Value")
plt.xlabel("Frequency Bands")
plt.show()

plt.figure(figsize=(15, 10))
sns.boxplot(data=rawDataEyes_df.iloc[:, :4])  # Plotting only the four columns related to pupil data
plt.title("Distribution of Pupil Data Features")
plt.ylabel("Value")
plt.xlabel("Feature")
plt.show()

plt.figure(figsize=(15, 10))
sns.heatmap(procDataEEG_df1.T, cmap="YlGnBu", cbar_kws={'label': 'Differential Entropy'})
plt.title("Differential Entropy - Moving Average - Trial 1")
plt.ylabel("Frequency Bands")
plt.xlabel("Time Frames")
plt.show()


# reference
# Based on code by AndreaAmorosini, retrieved from https://github.com/AndreaAmorosini/Emotion-Recognition-On-SEED-IV
# @article
# {delvigne2022emotion, title = {Emotion Estimation from EEG--A
# Dual Deep Learning Approach Combined with Saliency}, author={Delvigne, Victor and Facchini, Antoine and Wannous, Hazem
# and Dutoit, Thierry and Ris, Laurence and Vandeborre, Jean-Philippe},
# journal={arXiv preprint arXiv:2201.03891},year = {2022}}
