import chainlit as cl
from agents import Runner
from agent import agent

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Hello, how can I assist you today?").send()

@cl.on_message
async def on_message(message: cl.Message):
    # Pass the user message to the agent
    result = await Runner.run(agent, input=message.content)

    # The final_output attribute contains the agent's response
    if result.final_output:
        # Check for tool outputs and display them for debugging
        if result.tool_outputs:
            for tool_output in result.tool_outputs:
                await cl.Message(content=f"Tool output: {tool_output}").send()

        await cl.Message(content=result.final_output).send()
    else:
        await cl.Message(content="Sorry, I couldn't process your request.").send()
