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
3. Run containers with bash script
```
run_containers.sh
```
4. *(Optional) Or run server and front separately
```
cd backend
pip install -r requirements.txt
python main.py
cd ..
cd frontend
npm install
npm start
```

### Reflection
