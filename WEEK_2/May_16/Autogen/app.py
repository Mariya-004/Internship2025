import autogen
import os



config_list = [
    {
        'model': 'gemini-2.0-flash',
        'api_key': os.getenv("api_key"),  # Use os.getenv and import os
        'api_type':'google'
    }
]  

llm_config={
    "seed": 42,
    "config_list": config_list,
    "temperature": 0,  #lower the temperature for less creative and less unique replies higher temperature for more creative and unique replies
     
}

assistant=autogen.AssistantAgent(
    name="assistant",     #we can also  add more number of agents
    llm_config=llm_config
    #if adding more than one agent we have to define system message to specify the roles
)

user_proxy=autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": ".", "use_docker": False},  # Use "." for current directory
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction. Otherwise, reply CONTINUE or the reason why the task is not solved yet."""
)
                      #agent that acts on behalf of the user

task="""
tell me a joke
"""

user_proxy.initiate_chat(
    assistant,
    message=task,
)