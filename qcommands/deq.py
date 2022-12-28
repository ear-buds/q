@tree.command(name = "deq", description = "My first application Command") 
async def first_command(interaction):
    await interaction.response.send_message("`deq` called!")