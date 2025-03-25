from openai import OpenAI

class OpenAIAgent():

    def __init__(self, model, initialMessage):
        
        self.model = model

        self.conversation = [
            {"role": "user", "content": initialMessage}
        ]

        self.client = OpenAI(

        )
        
        completion = self.client.chat.completions.create(
            model = model,
            store = True,
            messages = self.conversation
        )

        reply = completion.choices[0].message

        self.conversation.append(
            {
                "role": reply.role, "content": reply.content
            }
        )

    def send_message(self, message) -> str:

        self.conversation.append(
            {
                "role": "user", "content": message
            }
        )

        completion = self.client.chat.completions.create(
            model = self.model,
            store = True,
            messages = self.conversation
        )

        reply = completion.choices[0].message

        self.conversation.append(
            {
                "role": reply.role, "content": reply.content
            }
        )

        return reply.content