# DISCORD
import discord
from discord import app_commands
from discord.ext import commands

class events_and_commands(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_presence_update(self, _, member_after: discord.Member):
        if hasattr(member_after, "activity") and hasattr(member_after, "large_image_text") and "Rammus" in member_after.activity.large_image_text:
            for channel in member_after.guild.text_channels:
                    if "atrapa-gays" in channel.name:
                        await channel.send(f"Jugador de Rammus detectado, {member_after.mention} {channel.topic}.")


    @app_commands.command(name="setup", description="Usar este comando para el setup del bot.")
    async def setup(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        for channel in interaction.guild.text_channels:
            if channel.name == "atrapa-gays":
                await interaction.followup.send(f"Ya hay un canal llamado {channel.mention}.")
                return
        
        channel = await interaction.guild.create_text_channel(name="atrapa-gays")

        await interaction.followup.send(f"El canal {channel.mention} fue creado exitosamente, los mensajes del bot se mandaran aqui. Edita la descripcion del canal para cambiar el mensaje que sera enviado al detectar a un jugador de Rammus")
        await channel.send("Edita la descripcion del canal para cambiar el mensaje que el bot manda.")


    @app_commands.command(name="ejemplo", description="Ejemplo de como se ve el mensaje.")
    async def ejemplo(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Jugador de Rammus detectado, {interaction.user.mention} **Aqui va la descripcion del canal en el cual el bot manda el aviso, usala para personalizar tu mensaje. Este ya tiene un punto al final por defecto**.")


    @app_commands.command(name="mandar_mensaje", description="Ejemplo de como se ve el mensaje.")
    async def mandar_mensaje(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        for channel in interaction.guild.text_channels:
                if "atrapa-gays" in channel.name:
                    await channel.send(f"Jugador de Rammus detectado, {interaction.user.mention} {channel.topic if channel.topic != None else 'el canal no tiene descripcion, edita la descripcion para personalizar el mensaje'}.")
                    await interaction.followup.send(f"Mensaje enviado en {channel.mention}.")
                    return

        await interaction.followup.send(f"No encontre un canal llamado atrapa-gays, utiliza el comando /setup para crearlo.")
                    

                    
async def setup(client: commands.Bot) -> None:
    await client.add_cog(
        events_and_commands(client)
    )
    print(f"Module events_and_commands.py was loaded succesfully.")
