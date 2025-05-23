#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import ResearcherWriterAgents

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Artificial Intelligence in 2025'
    }
    
    try:
        ResearcherWriterAgents().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


run()