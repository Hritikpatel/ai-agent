from config import client
from Agent import Agent
from prompts.prompts import ORCHESTRATOR_PROMPT
import json




class OrchestratorAgent(Agent):
    def __init__(self, client, name, system_prompt=ORCHESTRATOR_PROMPT):
        super().__init__(client, name, role="Orchestrator", system_prompt=system_prompt)
    
    def run(self, message=None):
        if message:
            self.messages.append({
                'role': 'user',
                'content': message,
            })

        # print("[Sending to Agent]")
        response = self.clint.chat(
            model=self.model,
            messages=self.messages,
            format={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string"
                    },
                    "language": {
                        "type": "string"
                    },
                    "current_level": {
                        "type": "string"
                    },
                    "goal": {
                        "type": "string"
                    },
                    "weekly_time_commitment_hours": {
                        "type": "number"
                    },
                    "duration_weeks": {
                        "type": "number"
                    },
                    "prerequisites": {
                        "type": ["string", "null"]
                    },
                    "constraints": {
                        "type": "object",
                        "properties": {
                            "assumptions": {
                                "type": "string"
                            },
                            "curriculum_planner_instructions": {
                                "type": "object",
                                "properties": {
                                    "start_point": {
                                        "type": "string"
                                    },
                                    "foundational_concepts": {
                                        "type": "string"
                                    },
                                    "major_concept_areas": {
                                        "type": "string"
                                    },
                                    "optional_advanced_subtopics": {
                                        "type": "string"
                                    },
                                    "skill_domains": {
                                        "type": "array",
                                        "items": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "required": [
                                    "start_point",
                                    "foundational_concepts",
                                    "major_concept_areas",
                                    "optional_advanced_subtopics",
                                    "skill_domains"
                                ],
                                "additionalProperties": False
                            }
                        },
                        "required": [
                            "assumptions",
                            "curriculum_planner_instructions"
                        ],
                        "additionalProperties": False
                    }
                },
                "required": [
                    "topic",
                    "language",
                    "current_level",
                    "goal",
                    "weekly_time_commitment_hours",
                    "duration_weeks",
                    "prerequisites",
                    "constraints"
                ],
                "additionalProperties": False
             },
            options={"temperature": 1}
            )

        
        self.messages.append({
            'role': 'ai',
            'content': response.message.content,
        })
        
        # print("[Response from Agent]")
        return json.loads(response.message.content)


agent = OrchestratorAgent(client=client, name="TestAgent", system_prompt=ORCHESTRATOR_PROMPT)

agent_response = agent.run(message=''' 
Topic: Learn Python Programming, 
Language: English, 
Current Level: Beginner, 
Goal: Build my own AI-Owned OS based on Linux, 
Weekly Time Commitment: 5 hours, 
Duration (weeks): 8, 
Prerequisites: Basic understanding of programming concepts. 
''')



print("Agent Response:")
print(json.dumps(agent_response, indent=2))