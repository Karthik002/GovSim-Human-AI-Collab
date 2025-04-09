from openai import OpenAI

class OpenAIAgent():

    def __init__(self, model, initialMessage):
        
        self.model = model

        self.conversation = [
            {"role": "user", "content": initialMessage}
        ]

        self.client = OpenAI(
            api_key="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"
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