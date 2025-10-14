# 🧠 Telegram Problem-Solver Bot

This is a simple **Telegram bot** that responds to user messages with solutions loaded from an **Excel file**.  
It uses the **python-telegram-bot** and **pandas** libraries.

---

## 📋 Features

- Loads a list of *problems and solutions* from an Excel file (`problems.xlsx`).
- Responds to any text message by looking up the matching problem.
- Includes a `/start` command for greetings.
- Easy to customize and extend with additional commands.

---

## 📂 Project Structure

```
telegram_bot/
│
├── bot.py             # Main Python script
├── problems.xlsx      # Excel file containing problems and solutions
└── README.md          # Project documentation
```

---

## 🧩 Excel Format

Make sure your `problems.xlsx` file has these two columns:

| Problem | Solution |
|----------|-----------|
| WiFi not connecting | Restart your router and try again. |
| Cannot log in | Check your username and password. |

The bot matches the **Problem** column (case-insensitive) and replies with the corresponding **Solution**.

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/msalharbi/telegram_bot.git
   cd telegram_bot
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install pandas python-telegram-bot==20.3
   ```

4. **Add your bot token**
   - Open `bot.py`
   - Replace:
     ```python
     app = Application.builder().token("TOKEN_HERE").build()
     ```
     with your actual Telegram bot token from [@BotFather](https://t.me/BotFather).

---

## ▶️ Run the Bot

```bash
python bot.py
```

You should see:
```
INFO:telegram.ext._application:Application started successfully
```

Then open Telegram, find your bot, and send a message like:
> wifi not connecting

The bot will reply with the corresponding solution from `problems.xlsx`.

---

## 🧠 Example Interaction

**User:**  
`wifi not connecting`  

**Bot:**  
`Restart your router and try again.`

---

## 🪄 Future Enhancements

- Add fuzzy matching for similar problem names.  
- Integrate with Google Sheets instead of Excel.  
- Add logging for frequently asked issues.  
- Deploy on a cloud service (e.g., Render, Heroku, or AWS Lambda).

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
