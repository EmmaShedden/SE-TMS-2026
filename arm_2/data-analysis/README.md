__Summary:__
We include all replication materials for generating our performance analysis (i.e., reaction times and accuracy mixed-effect regression models and statistical analysis).

- _'data-analysis-scripts'_ - Contains all mixed-effects regression model analysis scripts for all N-back factors and all programming tasks. 
  - To run the scripts yourself for a specific analysis, find it by selecting: `[task]-[dependent variable (DV)]-analysis.Rmd`
    - where task = [oneback, twoback, threeback, FITB, LR]
    - where DV = RT (reaction times) or accuracy

  - To view our scripts already run with the result, find it by selecting: `[task]-[dependent variable (DV)]-analysis.html`

  - __NOTE:__ If running scripts, please make sure to unzip all folders in this directory

- _'data-management-scripts'_ - Contains scripts associated with managing data and consolidating it to one data frame for data analysis.
  - We already provide the entire data frame used for analysis in _'preprocessed-data'_ folder for ease. We also indicate which full-data version was used at the top of each data analysis script.
  - We also provide the scripts used to grade accuracy/correctness for FITB and LR problems. As mentioned, these have already been calculated and results are in the _'preprocessed-data'_ folder. If you are interested in looking at test cases, please look at `grading.md`.

- _'preprocessed-data'_ - Contains two CSV sheets, one with programming task data and the other for N-back. These contain all the data together.

- _'raw-data'_ - Contains raw data from each participant from each session. This is useful if you are interested in seeing how data was stored from Psychopy (the software used to conduct the experiment). We also include coding blocks (test forms, but modular) and treatment session - participant mappings. We also provide the accuracy grades for each programming task for each participant.

- _'candidate-models'_ - Contains all the candidate models for all regression testing for all dependent variables and tasks 

