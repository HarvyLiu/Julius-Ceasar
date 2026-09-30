# Julius-Ceasar

> Of course you'll want a bot that can help you encode your text mid-chat right? (???)

A Slack bot for encrypting and encoding stuff. Why? Well so that I can send text encoded for no reason. Typo for the name is definitely intended.
## Preview
![Preview, if doesnt work, stardance might have taken it down or been taken down](https://stardance.hackclub.com/rails/active_storage/representations/proxy/eyJfcmFpbHMiOnsiZGF0YSI6NDY5NzM5LCJwdXIiOiJibG9iX2lkIn19--39ee67d81fc824def1a1b7d526c61a50d204cf3f/eyJfcmFpbHMiOnsiZGF0YSI6eyJmb3JtYXQiOiJ3ZWJwIiwicmVzaXplX3RvX2xpbWl0IjpbMTYwMCw5MDBdLCJzYXZlciI6eyJzdHJpcCI6dHJ1ZSwicXVhbGl0eSI6NzV9fSwicHVyIjoidmFyaWF0aW9uIn19--5394ecd620f1b8ee9be71be3f37cd22b8a88953c/image.png)


## What can it do? (For now, only 3 commands, more in future, feel free to contribute!!!)

In any Slack channel, type in:
(btw only you can see it)
**/caesar `<shift> <message>`**
Shift those letters.
```
/caesar 3 hello
> khoor
/caesar -3 khoor
> hello
```

**/rot13 `<message>`**
Caesar with a fixed shift of 13. Why? Since it's sort of an inverse, applying it twice gets you the original raw text, isnt that great? Just like XOR, but much more simpler~
```
/rot13 hello
> uryyb
/rot13 uryyb
> hello
```

**/base64 `<encode|decode> <message>`**
Idk, perhaps you're playing CTFs like me? Well you can use base64 to do a lot of stuffs, including data transfering... but this bot only supports text data for now.
```
/base64 encode hello
> aGVsbG8=
/base64 decode aGVsbG8=
> hello
```

## Setup

Rome wasn't built in a day, same for this bot, however setting it up can be in a day, actually just seconds:

1. Clone this repo:
   ```bash
   git clone https://github.com/HarvyLiu/Julius-Ceasar.git
   cd Julius-Ceasar
   ```

2. Summon dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your Slack tokens (shhh, secret — it's already in `.gitignore` so Brutus can't steal it (????, I'm spitting nonsense atp)):
   ```
   SLACK_BOT_TOKEN=xoxb-...
   SLACK_APP_TOKEN=xapp-...
   ```

   You'll need to create a Slack App with Socket Mode enabled + these slash commands: `/caesar`, `/rot13`, `/base64`.

4. Run it:
   ```bash
   python app.py
   ```

## Project Structure

```
.
├── app.py             # The Emperor himself — Slack handlers live here
├── ciphers/
│   ├── caesar.py      # The ol' shift-a-roo
│   └── b64.py         # Base64 encode/decode wizardry
├── requirements.txt   # Provisions for the journey
└── .env               # Secrets (you supply this, keep it hidden)
```

## Et tu, Contributor?

Found a bug? Stab it 23 times and open a PR. All citizens are welcome.

Ave! 🍇

(Seriously, wtf is wrong with me)
