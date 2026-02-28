# Multi-Agent Orchestrator Implementation

class MultiAgentOrchestrator:
    def __init__(self):
        # Initialize agents
        self.agents = []

    def add_agent(self, agent):
        # Add an agent to the orchestrator
        self.agents.append(agent)

    def coordinate_agents(self):
        # Coordinate actions among agents
        for agent in self.agents:
            agent.perform_task()

    def get_overall_status(self):
        # Get status of all agents
        status = {agent.name: agent.status for agent in self.agents}
        return status

# Usage example
if __name__ == '__main__':
    orchestrator = MultiAgentOrchestrator()