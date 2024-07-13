"""
* WORKING

What this script does:
This script demonstrates the use of Standard Operating Procedures (SOPs) 
in the Swarms framework. It shows how to create, apply, and modify SOPs 
for agents, and explains when SOPs are particularly useful.

Requirements:
- Swarms framework installed
- OpenAI API key in your .env file

Note: 
If you are running playground examples in the project files directly 
(without swarms installed via PIP), make sure to add the project root to 
your PYTHONPATH by running the following command in the project's root 
directory:
  'export PYTHONPATH=$(pwd):$PYTHONPATH'
"""

from swarms import Agent, Task, StandardOperatingProcedure
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def create_customer_service_sop() -> StandardOperatingProcedure:
    """
    Create a Standard Operating Procedure for customer service.

    Returns:
        StandardOperatingProcedure: An SOP for customer service tasks.
    """
    customer_service_sop = StandardOperatingProcedure(
        name="Customer Service SOP",
        description="Guidelines for handling customer inquiries",
        steps=[
            "Greet the customer politely",
            "Listen to the customer's inquiry or concern",
            "Identify the main issue",
            "Provide a clear and concise solution",
            "Confirm if the customer is satisfied with the solution",
            "Thank the customer for their time"
        ]
    )
    return customer_service_sop

def create_customer_service_agent(sop: StandardOperatingProcedure) -> Agent:
    """
    Create a customer service agent with a given SOP.

    Args:
        sop (StandardOperatingProcedure): The SOP to be followed by the agent.

    Returns:
        Agent: A customer service agent configured with the given SOP.
    """
    agent = Agent(
        name="CS_Agent_001",
        role="Customer Service Representative",
        goals=["Resolve customer issues", "Ensure customer satisfaction"],
        sop=sop
    )
    return agent

def handle_customer_inquiry(agent: Agent, inquiry: str) -> str:
    """
    Handle a customer inquiry using an agent with an SOP.

    Args:
        agent (Agent): The customer service agent.
        inquiry (str): The customer's inquiry.

    Returns:
        str: The agent's response to the inquiry.
    """
    task = Task(
        name="Handle Customer Inquiry",
        description="Respond to a customer inquiry following the SOP",
        agent=agent,
        agent_prompt=(
            f"You are a {agent.role}. Follow your SOP to handle this "
            f"customer inquiry: '{inquiry}'"
        ),
        user_prompt=inquiry
    )
    response = task.execute()
    return response

def main():
    # Create and demonstrate the use of an SOP
    customer_service_sop = create_customer_service_sop()
    cs_agent = create_customer_service_agent(customer_service_sop)

    print("Customer Service Agent created with SOP:")
    print(f"Agent Name: {cs_agent.name}")
    print(f"Agent Role: {cs_agent.role}")
    print("SOP Steps:")
    for step in cs_agent.sop.steps:
        print(f"- {step}")

    # Handle a customer inquiry
    inquiry = "I haven't received my order yet. It's been a week since I placed it."
    print(f"\nHandling customer inquiry: '{inquiry}'")
    response = handle_customer_inquiry(cs_agent, inquiry)
    print(f"Agent's response:\n{response}")

    # Demonstrate modifying the SOP
    print("\nModifying the SOP to include a follow-up step:")
    cs_agent.sop.steps.append("Schedule a follow-up if necessary")
    print("Updated SOP Steps:")
    for step in cs_agent.sop.steps:
        print(f"- {step}")

    # Handle another inquiry with the updated SOP
    inquiry = "I'm having trouble using your product. Can you help?"
    print(f"\nHandling another inquiry with updated SOP: '{inquiry}'")
    response = handle_customer_inquiry(cs_agent, inquiry)
    print(f"Agent's response:\n{response}")

if __name__ == "__main__":
    main()

"""
When SOPs are particularly useful:

1. Consistency: SOPs ensure that agents consistently follow a set of 
   predefined steps, which is crucial in scenarios where standardized 
   responses or actions are required.

2. Training: SOPs can be used to quickly train new agents or adapt existing 
   agents to new roles by providing them with a clear set of instructions.

3. Quality Control: By following SOPs, agents can maintain a high standard 
   of quality in their interactions and task completions.

4. Compliance: In regulated industries or sensitive operations, SOPs help 
   ensure that agents comply with necessary rules and regulations.

5. Efficiency: SOPs can streamline processes by providing a clear, 
   step-by-step guide for handling common scenarios, reducing decision-making 
   time and improving overall efficiency.

6. Scalability: As you scale up your swarm of agents, SOPs help maintain 
   consistency across a large number of agents performing similar tasks.

7. Adaptability: SOPs can be easily updated or modified to adapt to changing 
   requirements or to optimize processes based on performance feedback.

8. Complex Task Management: For tasks that involve multiple steps or 
   decision points, SOPs provide a structured approach that helps agents 
   navigate complex processes.

9. Error Reduction: By following a standardized procedure, agents are less 
   likely to make mistakes or overlook important steps in a process.

10. Performance Evaluation: SOPs provide a baseline against which agent 
    performance can be measured and evaluated.
"""