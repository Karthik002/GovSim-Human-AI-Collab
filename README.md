# Human-AI Collaboration in Cooperative Resource Management Simulations

## Project Overview

This project extends the GovSim simulation framework to investigate how AI agents collaborate with human participants in strategic resource management scenarios. While the original GovSim research focused on multiple AI agents competing against each other, this implementation introduces a novel twist: one AI agent collaborating with multiple human players in a shared resource environment.

The research paper is also included in the repository as a pdf file.

### Key Features

- Simulates three distinct resource management scenarios: fishery, pasture, and pollution
- Tests collaboration between human participants and various AI language models
- Compares performance of multiple AI models (ChatGPT 3.5, ChatGPT 4o-mini, Claude 3 Haiku, Claude 3.7 Sonnet)
- Measures quantitative and qualitative aspects of human-AI collaboration
- Built from the ground up to facilitate seamless human-AI interactions

## Research Findings

The project revealed fascinating insights into how different AI models collaborate with humans:

- **Performance Gap**: Significant differences in AI models' ability to collaborate effectively
- **Communication Consistency**: Some models showed discrepancies between stated intentions and actions
- **Trust Formation**: Human trust in AI varies based on perceived reliability and consistency
- **Advanced Reasoning**: More advanced models demonstrated superior mathematical reasoning and adaptive strategies
- **Human Decision-Making**: Human participants showed more complex decision patterns influenced by emotions and social dynamics

## Technical Details

### Simulation Architecture

- **Trial Structure**: Each trial consists of multiple cycles (months)
- **Cycle Phases**:
 - **Harvesting**: Agents request resources without knowledge of others' decisions
 - **Discussion**: Agents collaborate and strategize for future cycles
 - **Update**: Resources regenerate according to predefined rules

### Implementation

- **Language**: Python 3.9+
- **Libraries**:
 - `openai` - For ChatGPT API integration
 - `anthropic` - For Claude API integration
 - `pandas` & `matplotlib` - For data analysis and visualization
 - `flask` - For web interface facilitating human interaction
- **Architecture**: Event-driven simulation with modular components

### Resource Dynamics

Resources follow consistent rules across all environments:

- Initial resource pool of 100 units
- Doubling of resources after each cycle (up to max of 100)
- Minimum resource threshold must be maintained
- Simulation fails if resources fall below threshold

## Citation
If you use this code in your research, please cite Karthik Prasad.

## License
This project is licensed under the MIT License
