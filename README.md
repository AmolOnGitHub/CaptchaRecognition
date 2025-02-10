# CaptchaRecognition

I could not upload the dataset and trained models to this repository, so you can find them in these Kaggle datasets:

- [Dataset]()
- [Trained Models]()


### Task 0 

The code for the dataset generation is present in the [task-0](/CaptchaRecognition/task-0_dataset-creation.py) python file.
This will generate the images for task 1, and the Attention-based Encoder-Decoder model approach to task 2.

### Task 1

This is present as a Jupyter Notebook in the [task-1](/CaptchaRecognition/task-1_classification.ipynb) file.

This notebook is just exported from kaggle, so it doesn't run locally. You can view the [kaggle notebook](https://www.kaggle.com/code/amolvijayachandran/task1-precog).

### Task 2

There are two parts to this. My initial attempt was with an Attention-based Encoder-Decoder model, which you can find [here](/CaptchaRecognition/task-2_generation.ipynb).

I reattempted the task with a Transformer-based model, which you can find [here](/CaptchaRecognition/task-2_generation_new.ipynb).

The reattempt has a seperate dataset, which the notebook contains code to generate at the top.

### Bonus

Done in a Jupyter Notebook, present [here](/CaptchaRecognition/bonus.ipynb).


## Files

### Dataset

The dataset (available on kaggle) has 5 subfolders:
- `task1`: The dataset for task 1, with 100 words.
- `task2_600`: The dataset for the initial attempt for task 2.
- `task2`: The dataset for the reattempt for task 2.
- `bonus`: The dataset for the bonus task.
- `exclude`: some samples with random sequences of characters, not english words.

### Models

There are 5 trained models:
- `classification_complete`: A fully trained model for Task 1, achieving results as per mentioned in the presentation.
- `generation_complete_prev-arc_prev-data`: The Attention-based Encoder-Decoder model, trained on the `task2_600` dataset.
- `generation_complete_prev-arc_new-data`: The Attention-based Encoder-Decoder model, trained on the `task2` dataset.
- `generation_complete_new-arc_new-data`: The Transformer-based model, trained on the `task2` dataset.
- `bonus_complete`: Transformer-based model trained on the `bonus` dataset.

### Fonts

Contains all the fonts used to generate the samples.

### Others

- `general.py` contains the initial word list used to make the datasets for task 0, task 1, and the initial task 2.
- `word-100k.txt` contains the word list to make the datasets for the reattempt task 2, and the bonus task.