### 10th place solution to the ImageCLEF 2019 Tuberculosis - Severity scoring challenge.


This is our contribution to the ImageCLEF 2019 Tuberculosis - Severity scoring solution. 

### Challenge description
This subtask is aimed at assessing TB severity score. The Severity score is a cumulative score of severity of TB case assigned by a medical doctor. Originally, the score varied from 1 (“critical/very bad”) to 5 (“very good”). In the process of scoring, the medical doctors considered many factors like pattern of lesions, results of microbiological tests, duration of treatment, patient’s age and some other. The goal of this subtask is to assess the severity based on the CT image and some additional meta-data, including disability, relapse, comorbidity, bacillary and smoking among others.

### Data

In this edition, both subtasks (SVR and CTR) use the same dataset containing 335 chest CT scans of TB patients along with a set of clinically relevant metadata. 218 patients are used for training and 117 for test. For all patient, provided are 3D CT images with slice size of 512*512 pixels and number of slices varying from about 50 to 400. All the CT images are stored in NIFTI file format with .nii.gz file extension (g-zipped .nii files).


### Results


| Experiment        | Results           | Others  |
| ------------- |:-------------:| -----:|
| 16-layer 3D Convolutional Net | 61.1% AUC, 61.5% ACC | 128x128x32, 300 epochs,10th place solution |
