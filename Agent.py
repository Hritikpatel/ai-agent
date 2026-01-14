from config import model
class Agent:
    def __init__(self, client, name, model=model, role="Actor", system_prompt="Just act human"):
        self.name = name
        self.system_prompt = system_prompt
        self.clint = client
        self.model = model
        self.messages = [{
                    'role': 'system',
                    'content': self.system_prompt,
                }]
        
    def run(self, message=None):
        if message:
            self.messages.append({
                'role': 'user',
                'content': message,
            })

        # print("[Sending to Agent]")
        response = self.clint.chat(
            model=self.model,
            messages=self.messages
            )

        
        self.messages.append({
            'role': 'ai',
            'content': response.message.content,
        })
        
        # print("[Response from Agent]")
        return json.loads(response.message.content)