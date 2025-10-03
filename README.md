# 🗳️ Online Voting System for Elections

A secure, transparent, and user-friendly **Online Voting Platform** built using **Python (Flask Framework)**.  
This project aims to modernize traditional voting by enabling **digital participation** while ensuring **security, integrity, and accessibility** for all users.

---

## 🌟 Why Online Voting?
Elections are the backbone of democracy, but manual voting often suffers from:
- Long queues & delays in counting
- Possibility of human error
- Limited accessibility for remote voters
- Security challenges like ballot tampering

This project addresses these challenges with a **digital-first solution** that is:
- 🛡️ **Secure** – Encrypted data, no duplicate voting  
- ⚡ **Efficient** – Real-time result computation  
- 🌍 **Accessible** – Remote voting for registered users  
- 📊 **Transparent** – Admin dashboard for monitoring  

---

## ✨ Key Features

### 👤 Voter Module
- Voter **registration & authentication**
- Passwords stored securely with **bcrypt hashing**
- **One vote per user** validation
- Intuitive voting interface

### 🗳️ Voting Process
- Cast vote digitally with one click
- Automatic confirmation message
- Real-time update of voting records

### 👨‍💼 Admin Module
- Manage elections (start/end sessions)
- Add/remove voters
- View live results with candidate-wise breakdown
- Export data for auditing

### 🔐 Security
- Encrypted password storage (bcrypt)
- Plans for AES encryption of vote data
- Duplicate voting prevention
- Blockchain integration (future scope) for immutable logs

### 🌐 Accessibility
- Simple, mobile-friendly web interface
- Can be deployed on cloud for remote access
- Language localization support (planned)

---

## 📂 Project Structure

```
.
├── admFunc.py          # Admin functionalities
├── Admin.py            # Admin logic (login, results)
├── dframe.py           # Data management using pandas
├── homePage.py         # Homepage routing
├── LICENSE             # Open-source license
├── Project Report.pdf  # Project documentation
├── README.md           # Documentation file
├── registerVoter.py    # Registration logic
├── Server.py           # Flask server entry point
├── voter.py            # Voter-related logic
├── VotingPage.py       # Voting page logic
├── static/             # CSS, JS, images
└── templates/          # HTML templates
```

---

## 🚀 Getting Started

### 🔧 Prerequisites
Make sure the following are installed:
- Python 3.8+
- pip (Python package manager)
- Git

### 📥 Clone the Repository
```bash
git clone https://github.com/your-username/online-voting-system.git
cd online-voting-system
```

### 📦 Install Dependencies
```bash
pip install flask bcrypt pandas
```

(Optional) Use a **virtual environment**:
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

---

## ▶️ Running the Application

1. Start the Flask server:
   ```bash
   python Server.py
   ```
2. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```
3. Register as a voter, log in, and cast your vote.  
4. Admin can log in via the admin route and view live results.

---

## 🧪 Example Workflow

1. **Registration** → User signs up with secure credentials.  
2. **Login** → Authentication via username & password.  
3. **Voting** → User casts vote for their candidate.  
4. **Confirmation** → System acknowledges successful vote.  
5. **Admin Monitoring** → Admin views live tally in dashboard.  

---

## 📊 Results Management
- Votes stored securely in `votes.csv`  
- Admin can generate reports & export data  
- Results update in **real-time**  

---

## 🛡️ Security Details
- **bcrypt hashing** for password security  
- Planned: **AES encryption** for sensitive data  
- Planned: **Blockchain-based storage** for immutable voting records  
- Role-based access (Voter vs Admin)  

---

## 🛠️ Tech Stack
- **Frontend**: HTML, CSS, Bootstrap (templates)  
- **Backend**: Python (Flask Framework)  
- **Database**: Pandas (CSV-based), extendable to MySQL/PostgreSQL  
- **Authentication**: bcrypt hashing  
- **Deployment Options**: Localhost / Cloud (Heroku, AWS, etc.)  

---

## 🤝 Contribution Guidelines (for GSSoC 2025)

We welcome contributions from **GSSoC contributors** and the open-source community!

### Steps to Contribute:
1. **Fork** this repository  
2. **Clone** your fork:
   ```bash
   git clone https://github.com/your-username/online-voting-system.git
   ```
3. Create a **new branch**:
   ```bash
   git checkout -b feature-name
   ```
4. **Commit** your changes:
   ```bash
   git commit -m "Added feature: X"
   ```
5. **Push** to your fork:
   ```bash
   git push origin feature-name
   ```
6. Open a **Pull Request (PR)** with:
   - Clear description of changes  
   - Screenshots (if applicable)  

---

## 📜 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 📖 Future Enhancements
- ✅ Integration with SQL/NoSQL database  
- ✅ Blockchain-based vote recording  
- ✅ Multi-factor authentication (OTP/Email)  
- ✅ Support for large-scale elections with load balancing  
- ✅ Deployment on cloud platforms (AWS/Heroku/DigitalOcean)  

---

## 🙌 Acknowledgements
- Developed as part of **CSE Dept, CIT Mandya (2024–25)**  
- Open for contributions via **GirlScript Summer of Code (GSSoC) 2025**  
- Inspired by the need for **transparent, digital elections**  
