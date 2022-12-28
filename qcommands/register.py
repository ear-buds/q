@tree.command(name = "register", description = "My first application Command") 
async def first_command(interaction):
    await interaction.response.send_message("`register` called!")