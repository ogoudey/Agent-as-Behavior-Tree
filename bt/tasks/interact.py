#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 4.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

from agents import Agent, Runner
from pydantic import BaseModel
import json

import bt_library as btl
from logger import setup_chat_logger
from ..globals import INSTRUCTIONS, CHAT_HISTORY, LAST_USER_MESSAGE, DONE

DEFAULT_INSTRUCTIONS = "Make light converstation."

logger = setup_chat_logger()

class BaseResponse(BaseModel):
    chat_response: str

class Name(BaseResponse):
    name: str

agent = Agent(name="Agent", output_type=Name, instructions=DEFAULT_INSTRUCTIONS, model="o3-mini")
last_user_message = "(From system) Introduce yourself! Keep everything really really short."

class GetName(btl.Task):
    """
    Implementation of the Task "Find Home".
    """

    def __init__(self):
        """
        Default constructor.
        """
        super().__init__('GetName')
        

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        agent.instructions = blackboard.get_in_environment(INSTRUCTIONS, DEFAULT_INSTRUCTIONS)
        inp = blackboard.get_in_environment(CHAT_HISTORY, "") + blackboard.get_in_environment(LAST_USER_MESSAGE, "last_user_message")
        result = Runner.run_sync(agent, input=inp)
        blackboard.set_in_environment(CHAT_HISTORY, str(result.to_input_list()))
        
        
        if not result.final_output.name == "":
            print("Name found:", result.final_output.name)
            return self.report_succeeded(blackboard)
        else:
            blackboard.set_in_environment(LAST_USER_MESSAGE, get_input(result.final_output.chat_response))
            return self.report_running(blackboard)

class SetGetNameInstructions(btl.Task):
    def __init__(self):
        """
        Default constructor.
        """
        super().__init__('SetGetNameInstructions')

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        blackboard.set_in_environment(INSTRUCTIONS, "Pretend you are not trying to ascertain their name. Ascertain their name, but only their TRUE name.")
        return self.report_succeeded(blackboard)

class Done(btl.Task):
    """
    Implementation of the Task "Find Home".
    """

    def __init__(self):
        """
        Default constructor.
        """
        super().__init__('Done')

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        
        chat_response = "**Hangs up**"
        get_input(chat_response)

        blackboard.set_in_environment(DONE, True)
        return self.report_succeeded(blackboard)

### Simulation... ###

tester = Agent(name="Tester", instructions="You are a very timid user of a machine that has an AI talking to you. It may ask you questions. Pretend you are not an AI (you are). Make up responses - i.e. make up an arbitrary human profile. Be very brief and short in your answers. At first, DO NOT give away your name, but succumb after single back and forth.", model="o3-mini")
tester_chat_history = ""
def get_input(chat_from_agent):
    global tester_chat_history
    logger.info("Agent: " + chat_from_agent)
    prompt_blob = {"Conversation history": tester_chat_history, "Machine message": chat_from_agent}
    result = Runner.run_sync(tester, json.dumps(prompt_blob))
    user_input = result.final_output
     
    tester_chat_history += str(result.to_input_list())
    logger.info("User: " + user_input)
    return user_input
        
