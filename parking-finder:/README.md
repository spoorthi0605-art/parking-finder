# 🚗 Real-Time Parking Finder Using Crowdsensing  
**Mini Project — Flask + HTML + CSS + JS + SQLite**

This project is a smart parking assistance system that helps users find empty parking spaces around their location or at any manually entered address. It uses crowdsensing data, where users update parking availability, and the system automatically merges and updates nearby reports.

---

## 📌 Features
### ✔ 1. Search by Manual Address  
Users can type a location (home, office, road, landmark) and view parking availability near that point.

### ✔ 2. Search by Current Location  
The user can click **“Use My Current Location”** and the app fetches real-time nearby parking spaces.

### ✔ 3. Shows Status  
The system displays whether a spot is:  
- 🟢 **Free**  
- 🔴 **Occupied**

### ✔ 4. Shows Waiting Time  
Waiting time is calculated based on the number of recent occupied reports.

### ✔ 5. Crowdsensing Data  
Users can add/update:  
- Status (Free/Occupied)  
- Address or coordinates  
- Timestamp is automatically updated  

### ✔ 6. SQLite Database  
All data is stored in a lightweight database `parking.db`.

---

## 📁 Project Structure

# 🚗 Real-Time Parking Finder Using Crowdsensing  
**Mini Project — Flask + HTML + CSS + JS + SQLite**

This project is a smart parking assistance system that helps users find empty parking spaces around their location or at any manually entered address. It uses crowdsensing data, where users update parking availability, and the system automatically merges and updates nearby reports.

---

## 📌 Features
### ✔ 1. Search by Manual Address  
Users can type a location (home, office, road, landmark) and view parking availability near that point.

### ✔ 2. Search by Current Location  
The user can click **“Use My Current Location”** and the app fetches real-time nearby parking spaces.

### ✔ 3. Shows Status  
The system displays whether a spot is:  
- 🟢 **Free**  
- 🔴 **Occupied**

### ✔ 4. Shows Waiting Time  
Waiting time is calculated based on the number of recent occupied reports.

### ✔ 5. Crowdsensing Data  
Users can add/update:  
- Status (Free/Occupied)  
- Address or coordinates  
- Timestamp is automatically updated  

### ✔ 6. SQLite Database  
All data is stored in a lightweight database `parking.db`.

---

## 📁 Project Structure

parking-finder/
│── app.py # Backend (Flask)
│── parking.db # SQLite database
│── README.md # Project documentation
│── templates/
│ └── index.html # Frontend UI
│── static/
├── style.css # Styling
└── script.js # JavaScript logic


---

## 🛠️ Technologies Used
- **Python Flask** (Backend REST API)  
- **HTML & CSS** (Frontend UI)  
- **JavaScript** (Frontend logic)  
- **SQLite Database**  
- **Crowdsensing logic & location-based services**  

---

## 🚀 How to Run the Project

### **1. Open Terminal**
Navigate to the project folder:
cd parking-finder

### **2. Install dependencies**
cd parking-finder

### **3. Run the backend**
python3 app.py


### **4. Open the website**
Open your browser and go to:
http://127.0.0.1:5002


---

## 🎯 Output Features  
- Displays parking spots around entered or current location  
- Shows distance in km  
- Shows waiting time estimate  
- Shows real-time free/occupied status  
- Works with manual address & GPS coordinates  

---

## 📌 Future Enhancements  
- Integration with real map (Google Maps API)  
- Live traffic and congestion display  
- Predictive parking analytics  
- User account system  

---

## 👩‍💻 Developed By  
Spoorthi  
Mini Project – 2025  
Department of Artificial Intelligence and Data Science 

---

# 📎 GitHub Link  

https://github.com/spoorthi0605-art/parking-finder-project.git


---





