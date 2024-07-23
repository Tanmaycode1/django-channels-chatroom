# Chat Application

This repository contains the code for a simple chat application using Django and Django Channels. Users can join a single chat room, and all connected users are displayed with real-time chat functionality.

## Features

- **Login**: Users must log in to join the chat room.
- **Single Chat Room**: Join a shared chat room.
- **User Display**: See all currently connected users.
- **Real-Time Chat**: Messages are sent and received in real-time.

## Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/chat-app.git
   cd chat-app
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

6. **Access the application:**

   Open your browser and go to `http://127.0.0.1:8000`

## Usage

- **Login**: Use your credentials to log in.
- **Join the Chat Room**: Enter the chat room to start chatting with others.
- **Real-Time Updates**: Enjoy instant messaging with all connected users displayed.

## License

This project is licensed under the MIT License.
