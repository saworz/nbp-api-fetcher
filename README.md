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
3. *(To run with docker) Run containers with bash
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
Task requires both data manipulation and user interaction, so I've decided to
create web app that runs with Flask server and React frontend.
Server is pretty compact and contains only few endpoints and Django would be overkill for such
a simple task so I've chosen Flask.
I could stick with pure Python and create visualization with Streamlit, but I've started learning
MERN stack so I decided to show of some of my frontend skills with HTML, CSS, JS and React.

### 2. Fetching currency data
I have created NbpFetcher class that handles fetching data from nbp api. Requests are made for
specified list of currencies named with Currency Codes ISO 4217 convention.<br/>
Fetched data is passed to CsvConverter class that saves it to .csv file. It utilizes pandas
because it makes handling column data and .csv converting easy.

### 3. Data selection
User can select currency pairs he wishes to get exchange rates for by clicking checkbox on the right
side of the currency pairs. Each currency pair div is created by mapping list of 
available currencies fetched from the /api/get_currency_types/ endpoint.<br/>
![data-selection-image](https://github.com/saworz/images/blob/main/nbp-fetcher-1.png?raw=true)

### 4. Saving data
CsvConverted mentioned in paragraph 2 saves the data to .csv file named "all_currency_data.csv" file.
By selecting data with checkboxes user can choose currency pairs exchange rates to save, either locally
or to the server. <b>Download as .csv</b> button downloads .csv file with selected pairs and 
<b>Save to server</b> saves the same file to the server.
![data-saving-image](https://github.com/saworz/images/blob/main/nbp-fetcher-2.png?raw=true)

### 5. User interaction
Success messages, errors and info are displayed for the user with react-toastify library.
It makes creating popup messages pretty simple and it's easy to customize them.
![user-interaction-image](https://github.com/saworz/images/blob/main/nbp-fetcher-3.png?raw=true)

### 6. Error handling
Errors occurring while fetching data or communicating with backend are displayed with react-toastify.
They appear in the upper-right corner and provide simple error description. More precise error messages are displayed
with Python's logging module and in browser's console.
![error-handling-image](https://github.com/saworz/images/blob/main/nbp-fetcher-5.png?raw=true)


### 7. Data analysis
/api/analyze_data/ endpoint analyzes data for provided list of currency pairs. It also utilizes pandas library
to find average, median, min and max values easily. They are returned to the frontend and displayed
as info popups in the upper-left side of the screen. Results are visible on the image above.

### 8. Cyclic fetching
APScheduler takes care of fetching nbp exchange rates data once a day at 00:00. <b>fetch_nbp_api</b>
function is used as a cyclic job and the scheduler is started by running main.py script.
![cyclic-task-image](https://github.com/saworz/images/blob/main/nbp-fetcher-4.png?raw=true)
