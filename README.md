
# 📦 Telegram File Stream Bot Configuration

A simple configuration module for linking and managing a Telegram File Stream Bot.  
This script loads all required environment variables to set up your bot seamlessly using the **Telegram Bot API** and **Pyrogram** (or similar frameworks).

---

## 🧠 Overview

This script uses Python’s built-in `os` and `dotenv` libraries to load configuration values from environment variables (or a `.env` file).  
It defines a `Var` class containing all important bot configuration parameters.

---

## ⚙️ Requirements

- Python 3.8 or higher  
- Required packages:
  ```bash
  pip install python-dotenv
````

* A `.env` file or environment variables with the following values (see below)

---

## 📁 Environment Variables

Below are the environment variables used by the bot:

| Variable Name             | Description                                                  | Required | Default / Example                                |
| ------------------------- | ------------------------------------------------------------ | -------- | ------------------------------------------------ |
| `API_ID`                  | Telegram API ID                                              | ✅        | `28405636`                                       |
| `API_HASH`                | Telegram API Hash                                            | ✅        | `52b6dfbaeea988407006cefbea7c2e04`               |
| `BOT_TOKEN`               | Telegram Bot Token from [@BotFather](https://t.me/BotFather) | ✅        | `7902407945:AAFCJidyZ1ELUnQuR41iv6QJkslc8j9SzRI` |
| `name`                    | Bot name (optional)                                          | ❌        | `FileStreamBot`                                  |
| `SLEEP_THRESHOLD`         | Delay threshold for async tasks                              | ❌        | `60`                                             |
| `WORKERS`                 | Number of concurrent workers                                 | ❌        | `4`                                              |
| `BIN_CHANNEL`             | Channel ID to store files                                    | ✅        | `-1002044705664`                                 |
| `PORT`                    | Web server port                                              | ❌        | `3000`                                           |
| `WEB_SERVER_BIND_ADDRESS` | Web server bind address                                      | ❌        | `0.0.0.0`                                        |
| `PING_INTERVAL`           | Ping interval (in seconds)                                   | ❌        | `1200`                                           |
| `OWNER_ID`                | Telegram user ID(s) of bot owner(s)                          | ✅        | `6713397633`                                     |
| `NO_PORT`                 | Disable port binding                                         | ❌        | `False`                                          |
| `APP_NAME`                | Heroku app name (for deployment)                             | ❌        | `None`                                           |
| `OWNER_USERNAME`          | Bot owner’s Telegram username                                | ✅        | `shivamnox`                                      |
| `FQDN`                    | Fully qualified domain name                                  | ❌        | `0.0.0.0:3000`                                   |
| `HAS_SSL`                 | Enable SSL for bot URL                                       | ❌        | `False`                                          |
| `DATABASE_URL`            | MongoDB connection string                                    | ✅        | `mongodb+srv://...`                              |
| `UPDATES_CHANNEL`         | Telegram updates/news channel username                       | ✅        | `hivajoyweb`                                     |
| `BANNED_CHANNELS`         | List of banned channel IDs                                   | ❌        | `-1001362659779`                                 |

---

## 🧾 Example `.env` File

```env
API_ID=28405636
API_HASH=52b6dfbaeea988407006cefbea7c2e04
BOT_TOKEN=your_bot_token_here
BIN_CHANNEL=-1002044705664
DATABASE_URL=your_mongodb_url_here
OWNER_ID=6713397633
OWNER_USERNAME=shivamnox
UPDATES_CHANNEL=hivajoyweb
```

---

## 🚀 Deployment

You can host this bot using:

* **Heroku**
* **Render**
* **Railway**
* **VPS / Local machine**

For Heroku:

1. Fork this repository.
2. Add the necessary config vars in **Settings → Config Vars**.
3. Deploy the app.

---

## 👤 Author

**© ShivamNox**
Telegram: [@shivamnox](https://t.me/shivamnox)

---

## 📝 License

This project is for educational purposes only.
Redistribution or use of API keys shown here publicly is discouraged — replace them with your own credentials.

