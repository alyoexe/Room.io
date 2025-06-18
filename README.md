
# 🔵 Room.io – Real-Time Video Chat Rooms

**Room.io** is a web-based video conferencing platform that lets users create and join public or private rooms, similar to Zoom. It supports real-time audio and video communication using the **Agora SDK** and is powered by a **Django** backend.

---

## ✨ Features

- 🔐 Create **public** or **private** video chat rooms  
- 🎥 Real-time **video and audio** powered by Agora  
- 🎙 Mute microphone, disable camera, or leave the call  
- 👥 View number of participants in a room  
- 🧑‍💼 Display room **host information**  
- 📜 Discover and join ongoing **public rooms**  
- 💻 Clean and responsive web interface  

---

## ⚙️ Tech Stack

| Technology     | Role                                     |
|----------------|------------------------------------------|
| **Django**     | Backend logic, room/user management      |
| **Agora SDK**  | Real-time video & audio communication    |
| **JavaScript** | Frontend logic and media control         |
| **HTML + CSS** | Structure and styling of frontend        |

---

## 📸 Screenshots

> _Add your screenshots here_  
- Create Room Page  
- Public Rooms List  
- Video Call Interface  

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x  
- Agora account with a valid **App ID**

---

### 🖥 Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Room.io.git
cd Room.io
```

#### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Python Requirements

```bash
pip install -r requirements.txt
```

#### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```env
AGORA_APP_ID=your_agora_app_id_here
```

#### 5. Apply Migrations

```bash
python manage.py migrate
```

#### 6. Run the Development Server

```bash
python manage.py runserver
```

---

## 🌐 How to Use

1. Visit `https://room-io.onrender.com/` [click](https://room-io.onrender.com/)
2. Create or join a room (choose public/private)  
3. Share the room name to let others join  
4. Use video/audio controls to manage the call  
5. View public rooms on the homepage and join them  

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Contributing

Contributions are welcome!  
Please fork the repo and submit a pull request.

---

## 📬 Contact

💬[Linkedin](https://www.linkedin.com/in/alexeyo-mathew-alexander/)

---

## ⭐️ Show Your Support

If you like this project, give it a ⭐️ on GitHub and share it with others!
