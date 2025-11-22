# Learnemon (Codemon) 🎮📚

**Learnemon** is an interactive, gamified learning platform designed to make learning to code fun and engaging. It combines educational content with mini-games, quizzes, and a reward system to motivate users.

##  Features

*   **Gamified Learning**: Earn XP and coins by completing lessons and challenges.
*   **Interactive Lessons**: Structured learning paths for Beginner, Intermediate, and Advanced levels.
*   **Mini-Games**:
    *   **Bug Buster**: Find and fix bugs in code snippets.
    *   **Code Patcher**: Fill in the missing code logic.
    *   **Memory Card**: Test your memory of coding concepts.
*   **Practice Tools**:
    *   **Flashcards**: Quick revision of key concepts.
    *   **Terminal**: A simulated terminal environment to practice commands.
*   **User Dashboard**: Track your progress, view your profile, and manage your backpack.
*   **Leaderboard**: Compete with other learners and see where you stand.
*   **Secure Authentication**: User registration and login system to save your progress.

##  Tech Stack

*   **Backend**: Python, Flask
*   **Database**: SQLite, SQLAlchemy
*   **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
*   **Templating**: Jinja2

## ⚙️ Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Snarendra16/Learnemon.git
    cd Learnemon
    ```

2.  **Create a virtual environment (Optional but recommended)**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialize the Database**
    The application automatically creates the database (`instance/db.db`) on the first run if it doesn't exist.

##  Running the Application

1.  **Start the server**
    ```bash
    python run.py
    ```

2.  **Access the app**
    Open your web browser and go to:
    `http://127.0.0.1:5000`

##  Project Structure

```
Learnemon/
├── App/
│   ├── static/          # CSS, Images, JS assets
│   ├── templates/       # HTML templates
│   ├── __init__.py      # App initialization & config
│   ├── forms.py         # WTForms definitions
│   ├── models.py        # Database models
│   └── routes.py        # Application routes & logic
├── instance/            # SQLite database location
├── run.py               # Entry point
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

