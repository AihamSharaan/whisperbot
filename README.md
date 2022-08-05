# Whisper Bot [@HMA2BOT](https://t.me/HMA2BOT)

> A star ⭐ from you means a lot to us!

<p align="center"><a href="https://www.github.com/ANES0H/WhisperBot"><img src="https://telegra.ph/file/a5d76c485067c810400eb.jpg" width="5000"></a></p>

Telegram bot for Whisper Message.

## Usage

### Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ANES0H/WhisperBot)

1. Tap on above button and fill `API_ID`, `API_HASH`, `BOT_TOKEN`.
2. Then tap "Deploy App" below it. Wait till deploying is complete (will take atmost 2 minutes).
3. After deploying is complete, tap on "Manage App"
4. Check the logs to see if your bot is ready!
5) **IMPORTANT** : You need to do two things on [@BotFather](https://t.me/BotFather).
   1) Turn on Inline Mode in your bot settings.
   2) Now go back to settings, Tap on `Inline Feedback` and then on `100%` (without this your bot is nothing.)

### Local Deploying

1. Clone the repo
   ```markdown
   git clone https://github.com/ANES0H/WhisperBot
   ```
   
2. Get a DATABASE_URL. If you don't know how, deploy using Heroku Button only.
   
3. Edit `Config.py` and fill the needed variables

4. Enter the directory
   ```markdown
   cd WhisperBot
   ```
5. Run the file
   ```markdown
   python3 whisper.py
   ```

## Environment Variables

#### Mandatory Vars

- `API_ID` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `API_HASH` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)
- `DATABASE_URL` - Will be automatically added by Heroku.




