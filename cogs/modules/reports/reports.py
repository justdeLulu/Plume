from config import *
from utils import *
from bot import Bot
from nextcord import Activity, ActivityType
from nextcord.ext.commands import Cog
from nextcord.ext import commands

import os
import nextcord

allowedChannel: int = 1345173935741865994
subjectId: int = 476762767207170048
reportChannel: int = 1344820579626258464

questions = [
    "Quand as-tu fait tes besoins ? (Format : JJ/MM/AAAA ; HH :MM)",
    "Quel est ton nom ?",
    "Quel est le nom de ton propriétaire ?",
    "Quand as-tu fait tes besoins pour la dernière fois ? (JJ/MM/AAAA HH:MM)",
    "À quelle heure as-tu bu pour la dernière fois ? (Format : HH:MM)",
    "Comment évalues-tu la fréquence de tes demandes depuis la dernière fois que tu as fait tes besoins ?",
    "Quel est ton niveau d’hydratation actuellement ?",
    "À quelle heure as-tu fait ta première demande pour faire tes besoins ? (Format : HH:MM)",
    "Quel type de besoin as-tu effectué ? (Répondre par : Urinaire ou Fécale)",
    "Quelle était la quantité approximative ? (Quelques gouttes / Normal / Importante)",
    "Quelle était l’odeur détectée ? (Répondre par : Faible, Moyenne ou Forte)",
    "Quelle était la couleur observée ? (Répondre par : Claire, Normale ou Concentrée)",
    "As-tu ressenti un picotement ou une sensation particulière après l’acte ? (Oui / Non)",
    "Dans quelle position devais-tu être pour ton élimination ?",
    "As-tu demandé correctement l’autorisation avant de te soulager ?",
    "Combien de temps d’attente t’a été imposé avant l’autorisation ?",
    "As-tu éprouvé des tremblements ou des spasmes avant d’être autorisée ?",
    "As-tu ressenti une pression abdominale insoutenable avant l’autorisation ?",
    "As-tu essayé de presser tes jambes ou d’adopter une posture pour retenir ton besoin ?",
    "As-tu eu un accident avant l’autorisation ?",
    "As-tu fourni une preuve visuelle de ton acte ?",
    "Si oui, la preuve a-t-elle été jugée satisfaisante par ton Maître ?"
]

class OnMessage(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        
        self.retryOfThePuppy = 0
        self.creatingReport = False
        self.answers = []

    @commands.Cog.listener("on_message")
    async def on_message(self, message: nextcord.Message):
        
        # Is Subject in the good channel
        if (message.channel.id == allowedChannel and message.author.id == subjectId): 
            
            # If she retry to write it 3 times -> should beg to have it again. c: <3
            if (self.retryOfThePuppy == 3):
                await message.channel.send("Tu sais pas rediger un rapport??? T'es si conne?")
                
                return
            
            # Start the report thanks my princess for the Trigger <3
            if (message.content == "Awrf ! Awrf !"):
                self.creatingReport = True
                self.answers = []
                
                # await message.channel.send("Je t'écoute Chienne. Dis moi tout!")
                await message.channel.send(questions[0])
                
                return 
            
            # Reset the Report. 
            if (message.content == "Awrf...Woof!WoofWoof!!!"):
                self.answers = []
                self.retryOfThePuppy = self.retryOfThePuppy + 1
                await message.channel.send("J'ai compris, ta gueule! Tu peux recommencer")
                await message.channel.send(questions[0])
                
                return
            
            # Send Report
            if (message.content == "Woouaf!Woof!Woof!!!"):
                self.creatingReport = False
                await message.channel.send("Bravo! Le rapport a ete generer par LANA.")
                
                response = "───────────────────────────── ౨ৎ ─────────────────────────────\n"
                
                for idx in range(len(self.answers)):
                    response += f"{questions[idx]}\n"
                    response += f"> {self.answers[idx]}\n"
                
                response += "                                                         ｡ﾟ•┈୨♡୧┈• ｡ﾟ\n"
                response += f":small_blue_diamond: Rapport généré par LANA pour Chienne"
                
                channel = self.bot.get_channel(reportChannel)
                await channel.send(response)
                return 
            
            if (self.creatingReport == True):
                self.answers.append(message.content)
                await message.channel.send(questions[len(self.answers)])
                
            
            
        
        # self.bot.logger.info("We have logged in as", self.bot.user)

def setup(bot: Bot):
    bot.add_cog(OnMessage(bot))
