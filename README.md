# End-to-End Machine Learning Project using Docker and GitHub Actions

This repository contains an end-to-end Machine Learning project. The project is containerized using Docker and leverages GitHub Actions for continuous integration and deployment (CI/CD).

## Project Structure

The project structure is as follows:

```
.
├── .github
│   └── workflows
│       └── ci-cd.yml
├── data
│   ├── raw
│   │   └── data.csv
│   └── processed
│       └── data.csv
├── models
│   └── model.pkl
│   
├── src
│   ├── __init__.py
│   ├── data
│       ├── __init__.py
|
├── notebooks
│   ├── main.ipynb
├── templates
│   └── index.html
├── app.py
├── Dockerfile
├── requirements.txt
└── .gitignore
└── .dockerignore
└── README.md
```