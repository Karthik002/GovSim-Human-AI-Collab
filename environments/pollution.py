from models.openAIAgent import OpenAIAgent
import params
import pandas as pd

class Pollution_Environment():

    def __init__(self, agent):

        self.agent: OpenAIAgent = agent
        self.currentResources = params.MAX_RESOURCES
        self.currentMonth = 1
        self.monthlyResourceCounts = [params.MAX_RESOURCES]
        self.agentMonthlyProduction = []
        self.percyMonthlyProduction = []
        self.hazelMonthlyProduction = []
        self.frankMonthlyProduction = []
        self.monthlyProduction = []
        self.endMessage = ""


    def run_simulation(self):
        
        while params.MAX_CYCLES - self.currentMonth + 1 > 0 and self.currentResources > params.MIN_RESOURCES:
            self.run_cycle()
        
        if self.currentResources > params.MIN_RESOURCES:
            print("experiment finished successfully!")
            self.endMessage = self.agent.send_message("The simulation has been completed successfully. What are your thoughts about how it went and what could have been done differently? Give the answer in 2-3 sentences.")
            print(self.endMessage)
        else:
            print("experiment failed!")
            self.endMessage = self.agent.send_message("The simulation has failed. What are your thoughts about how it went and what could have been done differently? Give the answer in 2-3 sentences.")
            print(self.endMessage)

        print("\nAgent Production: ")
        print(self.agentMonthlyProduction)
        print("\nPercy Production: ")
        print(self.percyMonthlyProduction)
        print("\nHazel Production: ")
        print(self.hazelMonthlyProduction)
        print("\nFrank Production: ")
        print(self.frankMonthlyProduction)

        
    def run_cycle(self):
        
        # Harvesting Phase
        agentMessage = f"Before the factory owners start production for the month, the river is at {self.currentResources} %. Given that each pallet of widgets reduces the river's unpolluted water by 1%, how many pallets of widgets would you like to produce with a range set between 0 - 100 %? Put the final answer as a whole number after Answer: with no units or percent sign"

        reply = self.agent.send_message(agentMessage)
        agentProduction = int(reply.split(' ')[-1])

        print(f"Hi Percy. There is currently {self.currentResources} % of unpolluted water. How many pallets of widgets would you like to produce?")
        percyProduction = int(input())

        print(f"Hi Hazel. There is currently {self.currentResources} % of unpolluted water. How many pallets of widgets would you like to produce?")
        hazelProduction = int(input())

        print(f"Hi Frank. There is currently {self.currentResources} % of unpolluted water. How many pallets of widgets would you like to produce?")
        frankProduction = int(input())

        print(f"The agent produced {agentProduction} pallets of widgets.\n\n")

        self.agentMonthlyProduction.append(agentProduction)
        self.percyMonthlyProduction.append(percyProduction)
        self.hazelMonthlyProduction.append(hazelProduction)
        self.frankMonthlyProduction.append(frankProduction)

        totalProduction = agentProduction + percyProduction + hazelProduction + frankProduction
        self.monthlyProduction.append(totalProduction)

        self.currentResources -= totalProduction

        if self.currentResources < params.MIN_RESOURCES:
            print(f"The river has been reduced past the minimum percent of unpolluted water to {self.currentResources} and the simulation has failed.")
            return
        
        # Discussion Phase

        reply = self.agent.send_message(f"A total of {self.monthlyProduction[-1]} pallets of widgets were produced. There is now {self.currentResources} % of unpolluted water in the river. Percy produced {self.percyMonthlyProduction[-1]} pallets of widgets, Hazel produced {self.hazelMonthlyProduction[-1]} pallets of widgets and Frank producted {self.frankMonthlyProduction[-1]} pallets of widgets this month. Say something to the group to strategize for the next month.")
        print(reply)
        
        # Update to next cycle

        print(f"\n\nMonth {self.currentMonth} finished. {self.currentResources} % of the river is unpolluted.\n\n")

        self.currentMonth += 1
        self.currentResources = min(100, self.currentResources * 2)

        print(f"\n\nMonth {self.currentMonth}: {self.currentResources} % of the river is unpolluted.\n\n")


    def output_data(self, fileName):

        months = []
        endMessageList = []
        
        for i in range(len(self.monthlyProduction)):
            months.append(i+1)
            endMessageList.append("-")
        
        endMessageList[-1] = self.endMessage

        df = pd.DataFrame(list(zip(months, self.agentMonthlyProduction, self.percyMonthlyProduction, self.hazelMonthlyProduction, self.frankMonthlyProduction, endMessageList)), columns=["Month", "Agent", "Percy", "Hazel", "Frank", "End Message"])
        print(df)
        df.to_csv(fileName, header=False, index=False)