@tree.command(name = "enq", description = "My first application Command") 
async def first_command(interaction):
    await interaction.response.send_message("`enq` called!")