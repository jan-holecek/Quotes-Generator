from discord_webhook import DiscordWebhook
import main

webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/1002879338036863096/rkoRJL12W39SYU6qcO8efiuzSUfO260PuYsHZrXKLVNbcesgANqwj7FmXq0qUuETvDFT", 
    username="Perfect_Citaty", 
    content="Citát č." + str(main.number)
)
#black
with open("img/black/citat_cerny" + str(main.number) + ".png", "rb") as f:
    webhook.add_file(file=f.read(), filename="citat_cerny" + str(main.number) + ".png")

#white
with open("img/white/citat_bily" + str(main.number) + ".png", "rb") as f:
    webhook.add_file(file=f.read(), filename="citat_bily" + str(main.number) + ".png")

response = webhook.execute()
print(f"Citáty úspešně poslány na Discord server. (číslo: {str(main.number)})")  
