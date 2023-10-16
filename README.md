# EEG-based-emotion-recognition


Currently, the loading of the data set, data visualization, and data analysis have been completed, and the model is still under construction.

## Contents

1. [Labels Explanation](#labels-explanation)
2. [Raw EEG Data](#raw-eeg-data)
3. [Processed EEG Data](#processed-eeg-data)
4. [Raw Eye Data](#raw-eye-data)
5. [Processed Eye Data](#processed-eye-data)
6. [Visualization](#visualization)
7. [References](#references)

## Labels Explanation

In the dataset, trials are labeled based on the emotions they are associated with:
- 0: Neutral
- 1: Sad
- 2: Fear
- 3: Happy

Trials are organized into sessions, with each session containing labels for multiple trials.

## Raw EEG Data

- Imports raw EEG data from `.mat` files.
- Displays information about the subject and session.
- Lists EEG channels used in the dataset.
- Extracts data for specific channels (like `cz_eeg1` and `cz_eeg2`).
- Converts the extracted data to a pandas DataFrame for further analysis.

## Processed EEG Data

- Imports processed EEG data (features extracted from raw signals) from `.mat` files.
- Highlights different processing methods such as:
  - Differential Entropy using Moving Average
  - Differential Entropy using Linear Dynamic System
  - Power Spectral Density using Moving Average
  - Power Spectral Density using Linear Dynamic System

The processed data focuses on various frequency bands, like delta, theta, alpha, beta, and gamma.

## Raw Eye Data

The raw eye data section deals with:
- Blinking data: Provides timestamps of when blinks occurred during movie clips.
- Statistical data: Shows statistical data for eye movements during movie clips.
- Eye Fixation data: Gives times when eyes were fixated during movie clips.
- Pupil data: Records features about pupil sizes during movie clips.
- Saccade data: Presents features of every saccade record during movie clips.

Each of the above datasets is loaded from `.mat` files and then converted to pandas DataFrames for easy analysis.

## Processed Eye Data

- Imports processed eye data (features extracted from eye movement) from `.mat` files.
- Displays information about the session.
- Lists features associated with pupils (like diameter, Dispersion), fixations, and saccades.
- Converts the extracted data to a pandas DataFrame, transposing it for better readability and naming columns based on the eye features.

## Visualization

Creates plots to visualize the EEG data for better understanding:
- Time Series for EEG Channel FP1: Represents the EEG signals over time for the `FP1` channel.

## References

- https://github.com/AndreaAmorosini/Emotion-Recognition-On-SEED-IV
- @article
{delvigne2022emotion, title = {Emotion Estimation from EEG--A
Dual Deep Learning Approach Combined with Saliency}, author={Delvigne, Victor and Facchini, Antoine and Wannous, Hazem 
and Dutoit, Thierry and Ris, Laurence and Vandeborre, Jean-Philippe},
journal={arXiv preprint arXiv:2201.03891},year = {2022}}
