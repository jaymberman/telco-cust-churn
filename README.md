<div align="center">
  <h1>Telecommunication Customer Churn</h1>
</div>

<br>

This project is based on a [Kaggle Dataset](https://www.kaggle.com/blastchar/telco-customer-churn). I made this project while learning about Flask and Heroku.
The goal is to deploy a functioning prediction application for a reasonably well performing classificaiton model. 
Check out the [application](http://telco-cust-churn.herokuapp.com/)

## Table of contents

- [Table of contents](#table-of-contents)
- [Model Developpment](#model-development)
- [Replicating Results](#replicating-results)

## Model Development

Check out the jupyter notebook [./jupyter_notebook/EDA.ipynb](https://github.com/jaymberman/telco-cust-churn/tree/master/jupyter_notebook)

## Replicating Results

Recommended to do this in an activated virtual environment:

```sh
$ git clone https://github.com/jaymberman/telco-cust-churn
$ pip install -r requirements.txt
$ cd ml_model
$ python train.py
```
