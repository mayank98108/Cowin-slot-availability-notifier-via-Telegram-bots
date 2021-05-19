# Cowin-slot-availability-notifier-via-Telegram-bots

## Requirements
To configure Kapacitor with Telegram, the following is needed:

- a Telegram bot
- a Telegram API access token
- a Telegram chat ID

***

**Create a Telegram bot**
1. Search for the @BotFather username in your Telegram application
2. Click Start to begin a conversation with @BotFather
3. Send /newbot to @BotFather.
4. Send your bot’s name to @BotFather. Your bot’s name can be anything.
5. Send your bot’s username to @BotFather.
6. Begin a conversation with your bot. Click on the t.me/<bot-username> link in @BotFather’s response and click Start at the bottom of your Telegram application. Your newly-created bot will appear in the chat list on the left side of the application.
  
***
  
**Get a Telegram API access token**
1. Send /token to @BotFather
2. Select the relevant bot at the bottom of your Telegram application.
  
***
  
**Get your Telegram chat ID**
1. Paste the following link in your browser. Replace <API-access-token> with the API access token that you identified or created in the previous section:

https://api.telegram.org/bot<API-access-token>/getUpdates?offset=0
2. Send a message to your bot in the Telegram application. The message text can be anything. Your chat history must include at least one message to get your chat ID.
3. Refresh your browser.
4. Identify the numerical chat ID by finding the id inside the chat JSON object. In the example below, the chat ID is 123456789.

{  
   "ok":true,
   "result":[  
      {  
         "update_id":XXXXXXXXX,
         "message":{  
            "message_id":2,
            "from":{  
               "id":123456789,
               "first_name":"Mushroom",
               "last_name":"Kap"
            },
            "chat":{  
               "id":123456789,
               "first_name":"Mushroom",
               "last_name":"Kap",
               "type":"private"
            },
            "date":1487183963,
            "text":"hi"
         }
      }
   ]
}
