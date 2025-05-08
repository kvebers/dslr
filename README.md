# DSLR

Statisical analysis and logistical regression with Python, from screatch without any libraries that make life easier.
![Screenshot 2025-05-08 205738](https://github.com/user-attachments/assets/0494a40c-d8c2-4929-8d9b-8267da0213c9)

## Task

Make a statical analysis solution and logistical regression algorithm to run the projects.

## Run


Windows:
```
python -m venv venv
venv/scripts/activate
pip install -r requirements.txt
make
```

Mac/Linux
```
python -m venv venv
pip install -r requirements.txt
source venv/bin/activate
make
```

## Run seperate scripts
Train
```
./logreg_train.py
```
Predict
```
./logreg_predict.py
```
Describe, describes the data of the project
```
python3 ./describe.py
```
Describe, describes the data of the project
```
./describe.py
```
Plots a histogram to look for correlations.
```
./histogram.py
```
Plots a histogram and scatter plot
```
./pair_plot.py
```
Plots a scatter plot of houses
```
./scatter_plot.py
```
