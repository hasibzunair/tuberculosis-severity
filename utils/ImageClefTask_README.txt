The dataset files for the Tuberculosis task are structured as follows:


Training:
---------
"TrainingSet" contains the 218 CT images for training and it is divided in 2 zip files:
 - TrainingSet_1_of_2.zip (100 NIFTI files)
 - TrainingSet_2_of_2.zip (118 NIFTI files)

"TrainingSet_Masks.zip" contains the 218 lung masks for the training CT images.

"TrainingSet_metaData.csv" contains the metadata for the training images:

 - Metadata: Selected meta-data for more precise prediction of TB Severity scores
    + Columns:
	md_Disability
	md_Relapse
	md_SymptomsOfTB
	md_Comorbidity
	md_Bacillary
	md_DrugResistance
	md_HigherEducation
	md_ExPrisoner
	md_Alcoholic
	md_Smoking
	md_Severity

 - SVR task class: Binarization of the column md_Severity in classes "LOW" and "HIGH"
    + Columns:
	SVR_Severity

 - CTR task disorders: Binary features constituting the CT report:
    + Columns:
	CTR_LeftLungAffected
	CTR_RightLungAffected
	CTR_LungCapacityDecrease
	CTR_Calcification
	CTR_Pleurisy
	CTR_Caverns 


Test:
---------
"TestSet.zip" contains the 117 CT images for training

"TestSet_Masks.zip" contains the 117 lung masks for the test CT images.

"TestSet_metaData.csv" contains the metadata for the test images:

 - Metadata: Selected meta-data for more precise prediction of TB Severity scores
    + Columns:
	md_Disability
	md_Relapse
	md_SymptomsOfTB
	md_Comorbidity
	md_Bacillary
	md_DrugResistance
	md_HigherEducation
	md_ExPrisoner
	md_Alcoholic
	md_Smoking
	md_Severity
