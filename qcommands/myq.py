@tree.command(name = "myq", description = "My first application Command") 
async def first_command(interaction):
    await interaction.response.send_message("`myq` called!")