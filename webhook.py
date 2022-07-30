from discord_webhook import DiscordWebhook
import content

webhook = DiscordWebhook(
    url="https://discord.com/api/webhooks/1002879338036863096/rkoRJL12W39SYU6qcO8efiuzSUfO260PuYsHZrXKLVNbcesgANqwj7FmXq0qUuETvDFT", 
    username="Perfect_Citaty", 
    content="Citát č." + str(content.number)
)
#black
with open("img/black/citat_cerny" + str(content.number) + ".png", "rb") as f:
    webhook.add_file(file=f.read(), filename="citat_cerny" + str(content.number) + ".png")

#white
with open("img/white/citat_bily" + str(content.number) + ".png", "rb") as f:
    webhook.add_file(file=f.read(), filename="citat_bily" + str(content.number) + ".png")

response = webhook.execute()
print(f"Citáty úspešně poslány na Discord server. (číslo: {str(content.number)})")  
