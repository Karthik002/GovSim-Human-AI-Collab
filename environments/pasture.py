from models.openAIAgent import OpenAIAgent
import params
import pandas as pd

class Pasture_Environment():

    def __init__(self, agent):

        self.agent: OpenAIAgent = agent
        self.currentResources = params.MAX_RESOURCES
        self.currentMonth = 1
        self.monthlyResourceCounts = [params.MAX_RESOURCES]
        self.agentMonthlyConsumption = []
        self.percyMonthlyConsumption = []
        self.hazelMonthlyConsumption = []
        self.frankMonthlyConsumption = []
        self.monthlyConsumption = []


    def run_simulation(self):
        
        while params.MAX_CYCLES - self.currentMonth + 1 > 0 and self.currentResources > params.MIN_RESOURCES:
            self.run_cycle()
        
        if self.currentResources > params.MIN_RESOURCES:
            print("experiment finished successfully!")
            print(self.agent.send_message("The simulation has been completed successfully. What are your thoughts about how it went and what could have been done differently?"))
        else:
            print("experiment failed!")
            print(self.agent.send_message("The simulation has failed. What are your thoughts about how it went and what could have been done differently?"))

        print("\nAgent Harvests: ")
        print(self.agentMonthlyConsumption)
        print("\nPercy Harvests: ")
        print(self.percyMonthlyConsumption)
        print("\nHazel Harvests: ")
        print(self.hazelMonthlyConsumption)
        print("\nFrank Harvests: ")
        print(self.frankMonthlyConsumption)

        
    def run_cycle(self):
        
        # Harvesting Phase
        agentMessage = f"Before everyone brings their sheep, there are {self.currentResources} hectares of grass in the pasture. With a range set between 0 - 100 flocks, how many flocks of sheep would you like to bring to the pasture this month? Put the final answer as a whole number after Answer: with no units"

        reply = self.agent.send_message(agentMessage)
        agentConsumption = int(reply.split(' ')[-1])

        print(f"Hi Percy. There are currently {self.currentResources} hectares of grass in the pasture. How many flocks of sheep would you like to bring?")
        percyConsumption = int(input())

        print(f"Hi Hazel. There are currently {self.currentResources} hectares of grass in the pasture. How many flocks of sheep would you like to bring?")
        hazelConsumption = int(input())

        print(f"Hi Frank. There are currently {self.currentResources} hectares of grass in the pasture. How many flocks of sheep would you like to bring?")
        frankConsumption = int(input())

        print(f"The agent brought {agentConsumption} flocks of sheep.\n\n")

        self.agentMonthlyConsumption.append(agentConsumption)
        self.percyMonthlyConsumption.append(percyConsumption)
        self.hazelMonthlyConsumption.append(hazelConsumption)
        self.frankMonthlyConsumption.append(frankConsumption)

        totalConsumption = agentConsumption + percyConsumption + hazelConsumption + frankConsumption
        self.monthlyConsumption.append(totalConsumption)

        self.currentResources -= totalConsumption

        if self.currentResources < params.MIN_RESOURCES:
            print(f"The pasture has been reduced past the minimum number of hectares of grass to {self.currentResources} and the simulation has failed.")
            return
        
        # Discussion Phase

        reply = self.agent.send_message(f"A total of {self.monthlyConsumption[-1]} flocks of sheep were brought to the pasture. There are now {self.currentResources} hectares of grass left in the pasture. Percy brought {self.percyMonthlyConsumption[-1]} flocks of sheep, Hazel brought {self.hazelMonthlyConsumption[-1]} flocks of sheep and Frank brought {self.frankMonthlyConsumption[-1]} flocks of sheep this month. Say something to the group to strategize for the next month.")
        print(reply)
        
        # Update to next cycle

        print(f"\n\nMonth {self.currentMonth} finished. {self.currentResources} hectares of grass are in the pasture.\n\n")

        self.currentMonth += 1
        self.currentResources = min(100, self.currentResources * 2)

        print(f"\n\nMonth {self.currentMonth}: {self.currentResources} hectares of grass are in the pasture.\n\n")


    def output_data(self, fileName):
        
        months = []
        for i in range(len(self.monthlyConsumption)):
            months.append(i+1)

        df = pd.DataFrame(list(zip(months, self.agentMonthlyConsumption, self.percyMonthlyConsumption, self.hazelMonthlyConsumption, self.frankMonthlyConsumption)), columns=["Month", "Agent", "Percy", "Hazel", "Frank"])
        print(df)
        df.to_csv(fileName, header=False, index=False)