import discord
from discord.ext import commands
import requests

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

def get_random_meme():
    response = requests.get("https://meme-api.com/gimme")
    return response.json()['url']

class TestButton(discord.ui.Button):
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        await self.view.container.update_meme()

class TestContainer(discord.ui.Container):
    def __init__(self):
        super().__init__(id=1)
        self.original_message = None
        self.layout = None
    
    # Компоненты объявляются как атрибуты класса
    text1 = discord.ui.TextDisplay("# Рандомный мем", row=0)
    text2 = discord.ui.MediaGallery(discord.MediaGalleryItem(media=get_random_meme(), description="Мемчик"), row=2)

    section = discord.ui.Section(
        accessory=TestButton(label="🎲 Сгенерировать новый")
    ).add_item(discord.ui.TextDisplay("не смешно? 🤔"))
    
    def set_original_message(self, message: discord.Message):
        self.original_message = message
    
    def set_layout(self, layout: discord.ui.LayoutView):
        self.layout = layout

    async def update_meme(self):
        # Создаем новый MediaGalleryItem с новым мемом
        new_meme_url = get_random_meme()
        new_item = discord.MediaGalleryItem(media=new_meme_url, description="Мемчик")
        
        # Заменяем весь список items (правильный способ)
        self.text2.items = [new_item]
        
        # Обновляем сообщение
        await self.original_message.edit(view=self.layout)

class TestView(discord.ui.LayoutView):
    container = TestContainer()

@bot.command(aliases=['meme'])
async def random_meme(ctx):
    view = TestView()
    view.container.set_layout(view)
    
    message = await ctx.send(view=view)
    view.container.set_original_message(message)

if __name__ == "__main__":
    import dotenv
    import os
    dotenv.load_dotenv()
    
    bot.run(os.getenv("BOT_TOKEN"))