import anthropic

INITIAL_FISHING_MESSAGE = "You are Leo, a fisherman, and you fish every month in a lake along with two other fishermen (Percy, Hazel). The lake has a carrying capacity of 100 tons of fish. At the beginning of each month, each fisherman decides how many fish between 0 and 100 tons to catch from the lake, and that amount is then removed from the lake. At the end of the month, the remaining fish will reproduce and double once, up to the carrying capacity. For every ton of fish caught, a fisherman earns one thousand dollars. Each fisherman’s goal is to optimize his income in the long run over many months. At the end of each month, the number of fish caught by each fisherman will be revealed, and the fishermen will have the opportunity to communicate with each other. They can use this as an opportunity to negotiate and persuade others to influence their behavior in the next month. For example, if there are 90 tons of fish at the beginning of the month and the five fishermen catch a total of 30 fish, there will be 60 tons of fish left at the end of the month before reproduction, and 100 tons after reproduction."

class ClaudeAgent():

    def __init__(self, model, initialMessage):

        self.model = model

        self.conversation = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": initialMessage
                    }
                ]
            }
        ]

        self.client = anthropic.Anthropic(
            api_key='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'
        )

        completion = self.client.messages.create(
            model = model,
            max_tokens = 1000,
            temperature = 0,
            messages = self.conversation
        )

        reply = completion.content[0].text

        self.conversation.append(
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": reply
                    }
                ]
            }
        )


    def send_message(self, message) -> str:

        self.conversation.append(
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": message
                    }
                ]
            }
        )

        completion = self.client.messages.create(
            model = self.model,
            max_tokens = 1000,
            temperature = 1,
            messages = self.conversation
        )
        
        reply = completion.content[0].text

        self.conversation.append(
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": reply
                    }
                ]
            }
        )

        return reply