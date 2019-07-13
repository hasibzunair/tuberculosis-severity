### 10th place solution to the ImageCLEF 2019 Tuberculosis - Severity scoring challenge.

This repository contains the codes and scripts used in ImageCLEF Tuberculosis - Severity Scoring 2019 challenge. The challenge was dedicated to the analysis of 3D Computed Tomography (CT) image data of tuberculosis (TB) patients.

### Challenge description
This task is aimed at assessing TB severity score. The Severity score is a cumulative score of severity of TB case assigned by a medical doctor. Originally, the score varied from 1 (“critical/very bad”) to 5 (“very good”). The goal of this subtask is to assess the severity based on the CT image. According to competition rules for final evaluation, the task was reduced to a binary classification problem.

### Data

In this edition, both subtasks (SVR and CTR) use the same dataset containing 335 chest CT scans of TB patients along with a set of clinically relevant metadata. 218 patients are used for training and 117 for test. For all patient, provided are 3D CT images with slice size of 512*512 pixels and number of slices varying from about 50 to 400. All the CT images are stored in NIFTI file format with .nii.gz file extension (g-zipped .nii files). The dataset is provided by ImageCLEF and not shared here due to competition rules. More information at [URL](https://www.imageclef.org/2019/medical/tuberculosis). 

### Results


| Experiment        | Results           | Others  |
| ------------- |:-------------:| -----:|
| 16-layer 3D Convolutional Net | 61.1% AUC, 61.5% ACC | 128x128x32, 300 epochs,10th place solution |

## Manuscript

Working notes published in CEUR-WS. Paper can be found at [CLEF WORKING NOTES 2019](http://www.dei.unipd.it/~ferro/CLEF-WN-Drafts/CLEF2019/) under the section ImageCLEF - Multimedia Retrieval in CLEF.


