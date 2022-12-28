@tree.command(name = "getq", description = "My first application Command") 
async def first_command(interaction):
    await interaction.response.send_message("`getq` called!")