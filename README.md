# EEG-based-emotion-recognition


## Introduction

This project explores emotion recognition using EEG signals through two deep learning models: a 3-dimensional Convolutional Neural Network (3D CNN) and a 4-dimensional Convolutional Recurrent Neural Network (4D CRNN). Our approach focuses on transforming differential entropy features from various channels into a 4D structure, enabling the training of an intricate deep model.

## Project Structure

- `3D CNN.ipynb`: Implementation of the 3D CNN model for EEG-based emotion recognition.
- `3DCNN model structure.ipynb`: Detailed structure and layers of the 3D CNN model.
- `4D-CRNN.ipynb` and `4D_CRNN.ipynb`: Two versions of the 4D-CRNN model implementation.
- `SEED-IV_analysis.py`: Script for analyzing the SEED-IV dataset used in the project.
- `README.md`: Documentation of the project (this file).

## Research Summary

**Authors:** Yichen Jiao, Siyu Zhang (Lakehead University)

**Abstract:** Our study introduces both traditional 3D CNN and innovative 4D CRNN models for EEG-based emotion recognition. We demonstrate the superior performance of these models in identifying various emotional states compared to existing methods.

### Key Sections

1. **Introduction**: Highlights the significance of EEG in affective computing and emotion recognition.
2. **3D CNN Modeling**: Describes the architecture and functionality of the 3D CNN model.
3. **4D Feature Organization**: Discusses the methodology of organizing EEG signals into a 4D structure.
4. **4D CRNN Modeling**: Details the structure and process of the 4D CRNN model.
5. **Dataset Analysis**: Explains the dataset and its importance for model validation.
6. **Environment Description**: Describes the computational environment used for experiments.
7. **Results and Discussion**: Presents the findings and effectiveness of the models.
8. **Conclusion**: Summarizes the study and discusses potential future research directions.

## Dataset and Analysis

We utilized a comprehensive collection of EEG and eye-tracking data sourced from 15 subjects, focusing on four emotional states. The dataset was structured into 45 sessions, allowing for a robust evaluation of our models' performance.
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


### Data Analysis Highlights

- **EEG Signal Visualization**: Includes time series representation of EEG channels (e.g., FP1).
- **Frequency Band Analysis**: Examines EEG signals across different frequency bands (delta, theta, alpha, beta, gamma).

## Results

Our experimental results showcase the effectiveness of both 3D CNN and 4D CRNN models:

- The 3D CNN model achieved a maximum accuracy of approximately 78%.
- The 4D CRNN model reached an accuracy of up to 95%, with an average of 81.9%.

## Conclusion

The study introduces effective frameworks for EEG-based emotion recognition, demonstrating their potential in various affective computing applications. Future research may focus on model optimization for real-time applications and integration of more diverse data.


## References

- https://github.com/AndreaAmorosini/Emotion-Recognition-On-SEED-IV
- @article
{delvigne2022emotion, title = {Emotion Estimation from EEG--A
Dual Deep Learning Approach Combined with Saliency}, author={Delvigne, Victor and Facchini, Antoine and Wannous, Hazem 
and Dutoit, Thierry and Ris, Laurence and Vandeborre, Jean-Philippe},
journal={arXiv preprint arXiv:2201.03891},year = {2022}}
