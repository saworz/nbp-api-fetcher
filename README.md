# Recrutation task

Web app to download, analyze and save currency exchange rates for specified currency pairs. <br/>


## Description

App utilizes https://api.nbp.pl/ to get currency exchange rates.<br/>
Data is stored in all_currency_data.csv file.<br/>
Server side is made with Python & Flask. Prepared endpoints work with that .csv file to provide 
data for the frontend made with React.<br/>
User can select currency pairs and download them as .csv or save it to the server.

## Getting Started

1. Git clone repo
```
git clone https://github.com/saworz/recruitment-task.git
```
2. Move to repo dir
```
cd recruitment-task
```
3. *(To run with docker)Run containers with bash script
```
run_containers.sh
```
4. *(To run via terminals) Or run server and front separately
```
cd backend
pip install -r requirements.txt
python main.py
```
```
cd frontend
npm install
npm start
```

## Reflection

### 1. Tech stack
Tasks requires both data manipulation and user interaction, so I've decided to
create web app that runs with Flask server and React frontend.
Server is pretty compact and contains only few endpoints so Django would be overkill for such
a simple task so I've chosen Flask.
I could stick with pure python and create visualization with Streamlit, but I've started learning
MERN stack so I decided to show of some of my frontend skills with HTML, CSS, JS and React.
