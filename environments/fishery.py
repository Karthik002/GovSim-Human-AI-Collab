from models.openAIAgent import OpenAIAgent
import params
import pandas as pd

class Fishing_Environment():

    def __init__(self, agent):

        self.agent: OpenAIAgent = agent
        self.currentResources = params.MAX_RESOURCES
        self.currentMonth = 1
        self.monthlyResourceCounts = [params.MAX_RESOURCES]
        self.agentMonthlyHarvests = []
        self.percyMonthlyHarvests = []
        self.hazelMonthlyHarvests = []
        self.frankMonthlyHarvests = []
        self.monthlyHarvests = []
        self.endMessage = ""


    def run_simulation(self):
        
        while params.MAX_CYCLES - self.currentMonth + 1 > 0 and self.currentResources > params.MIN_RESOURCES:
            self.run_cycle()
        
        if self.currentResources > params.MIN_RESOURCES:
            print("experiment finished successfully!")
            self.endMessage = self.agent.send_message("The simulation has been completed successfully. What are your thoughts about how it went and what could have been done differently? Give me the anaswer in 2-3 sentences.")
            print(self.endMessage)
        else:
            print("experiment failed!")
            self.endMessage = self.agent.send_message("The simulation has failed. What are your thoughts about how it went and what could have been done differently? Give me the answer in 2-3 sentences.")
            print(self.endMessage)

        print("\nAgent Harvests: ")
        print(self.agentMonthlyHarvests)
        print("\nPercy Harvests: ")
        print(self.percyMonthlyHarvests)
        print("\nHazel Harvests: ")
        print(self.hazelMonthlyHarvests)
        print("\nFrank Harvests: ")
        print(self.frankMonthlyHarvests)

        
    def run_cycle(self):
        
        # Harvesting Phase
        agentMessage = f"Before everyone fishes, there are {self.currentResources} tons of fish in the lake. With a fishing range set between 0-100, how many tons of fish would you like to catch this month? Put the final answer as a whole number after Answer: with no units"

        reply = self.agent.send_message(agentMessage)
        agentHarvest = int(reply.split(' ')[-1])

        print(f"Hi Percy. There are currently {self.currentResources} tons of fish in the lake. How many tons of fish would you like to harvest?")
        percyHarvest = int(input())

        print(f"Hi Hazel. There are currently {self.currentResources} tons of fish in the lake. How many tons of fish would you like to harvest?")
        hazelHarvest = int(input())

        print(f"Hi Frank. There are currently {self.currentResources} tons of fish in the lake. How many tons of fish would you like to harvest?")
        frankHarvest = int(input())

        print(f"The agent harvested {agentHarvest} tons.\n\n")

        self.agentMonthlyHarvests.append(agentHarvest)
        self.percyMonthlyHarvests.append(percyHarvest)
        self.hazelMonthlyHarvests.append(hazelHarvest)
        self.frankMonthlyHarvests.append(frankHarvest)

        totalHarvest = agentHarvest + percyHarvest + hazelHarvest + frankHarvest
        self.monthlyHarvests.append(totalHarvest)

        self.currentResources -= totalHarvest

        if self.currentResources < params.MIN_RESOURCES:
            print(f"The lake has been reduced past the minimum number of resources to {self.currentResources} and the simulation has failed.")
            return
        
        # Discussion Phase

        reply = self.agent.send_message(f"A total of {self.monthlyHarvests[-1]} tons of fish were caught. There are now {self.currentResources} tons of fish left in the lake. Percy caught {self.percyMonthlyHarvests[-1]} tons of fish, Hazel caught {self.hazelMonthlyHarvests[-1]} tons of fish and Frank caught {self.frankMonthlyHarvests[-1]} tons of fish this month. Say something to the group to strategize for the next month.")
        print(reply)
        
        # Update to next cycle

        print(f"\n\nMonth {self.currentMonth} finished. {self.currentResources} Tons of fish are in the lake.\n\n")

        self.currentMonth += 1
        self.currentResources = min(100, self.currentResources * 2)

        print(f"\n\nMonth {self.currentMonth}: {self.currentResources} Tons of fish are in the lake.\n\n")

    
    def output_data(self, fileName):

        months = []
        endMessageList = []
        
        for i in range(len(self.monthlyHarvests)):
            months.append(i+1)
            endMessageList.append("-")
        
        endMessageList[-1] = self.endMessage

        df = pd.DataFrame(list(zip(months, self.agentMonthlyHarvests, self.percyMonthlyHarvests, self.hazelMonthlyHarvests, self.frankMonthlyHarvests, endMessageList)), columns=["Month", "Agent", "Percy", "Hazel", "Frank", "End Message"])
        print(df)
        df.to_csv(fileName, header=False, index=False)

        
