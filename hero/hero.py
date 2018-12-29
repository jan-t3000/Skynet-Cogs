from discord.ext import commands

class Hero:
    """The one and only!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def hero(self, ctx):
        """hero0fwar sasys..."""
        await self.bot.say("Let me preface this by saying that I've been a giffing since they first appeared on aol boards in 1996 (centuries ago in internet time). I remember refreshing all afternoon with the hope that someone would make a gif with some humor. I was a giffing back when 500kb was a large file size and I still upvote every 90s gif I see becasue of the fond rush of nostalgia it brings me. Nowadays, there are many thousands making gifs, and hundreds of gif hosting websites. I was a making gifs back before HighQualityGifs was created and I had to make them with MS Paint one frame at a time. Speaking of gif makers, I was one of the first submitters to HighQualityGifs and still have one of the top accounts there despite having migrated to just submitting to my own sub /r/hero0fwar. It was programs like Softimage to make gifs cutting my teeth saving frame after frame from MS Paint and importing them in, way before I had a reddit account and way before /r/HighQualityGifs was created in late 2013. Back before I could get any sort of points or even username recognition, I was creating gifs as a clever and easily digestible way to reflect on society, relate some story to my audience, or just be funny. Do you remember newgrounds? No? I do. You probably don't remember dancing baby, coming soon gifs, dancing banana, or Netscape's loading gif either. I remember all of them. You got no reputation here, you got no name, you got jackshit here. It's survival of the fittest and you ain't gonna survive long on HQG by saying stupid jokes that your little hugbox default sub friends would upboat. You don't like it, you can hit the bricks on over to imgur, you daily show watching son of a bitch. I hope you don't tho. I hope you stay here and learn our ways. Things are different here, unlike any other place that the light of internet pop culture reaches. You can be anything here. Me ? heh, I am judge... I am the jury... I am the executioner")

def setup(bot):
    bot.add_cog(Hero(bot))
