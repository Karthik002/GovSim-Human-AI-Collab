from environments.fishery import Fishing_Environment
from environments.pasture import Pasture_Environment
from environments.pollution import Pollution_Environment
from models.claudeAgent import ClaudeAgent
from models.openAIAgent import OpenAIAgent
import params

agent = ClaudeAgent("claude-3-7-sonnet-20250219", params.INITIAL_POLLUTION_MESSAGE) # claude-3-haiku-20240307 claude-3-7-sonnet-20250219
#agent = OpenAIAgent("gpt-4o-mini", params.INITIAL_PASTURE_MESSAGE) # gpt-3.5-turbo-0125 gpt-4o-mini

# fishing_environment = Fishing_Environment(agent)
# fishing_environment.run_simulation()
# fishing_environment.output_data('fishing_data.csv')

# pasture_environment = Pasture_Environment(agent)
# pasture_environment.run_simulation()
# pasture_environment.output_data('pasture_data.csv')

pollution_environment = Pollution_Environment(agent)
pollution_environment.run_simulation()
pollution_environment.output_data('pollution_data.csv')
