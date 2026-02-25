# Agentic AI AutoGen POC: Multi-MCP Integration

![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green) 

## Overview

This project serves as a Proof of Concept (POC) for building advanced Agentic AI systems using the Microsoft AutoGen framework. It demonstrates the integration of AutoGen agents with multiple Model Context Protocol (MCP) servers, enabling sophisticated interactions with diverse data sources and services. This setup allows agents to query structured databases, fetch real-time external data, and perform dynamic file system operations.

## High-Level Architecture

The architecture revolves around Microsoft AutoGen agents orchestrating tasks by interacting with specialized Model Context Protocol (MCP) servers.

-   **AutoGen Agents**: The core intelligent entities that process requests, make decisions, and delegate tasks. They communicate with the MCP servers to fulfill their objectives.
-   **Orchestration Layer**: This layer facilitates the seamless interaction between AutoGen agents and the various MCP servers. It handles routing, context management, and ensures that agents can leverage the capabilities of each MCP.
-   **Model Context Protocol (MCP) Servers**:
    *   **MySQL MCP Server**: Provides agents with the ability to perform structured data queries against a MySQL database. This enables agents to retrieve, analyze, and manipulate data stored in relational databases.
    *   **Rest API MCP Server**: Allows agents to interact with external RESTful APIs to fetch real-time data, integrate with third-party services, or trigger actions in external systems.
    *   **File System MCP Server**: Grants agents capabilities for file manipulation, including reading, writing, and listing files. This is crucial for local data persistence, logging, and dynamic content generation.

The agents, through the orchestration layer, can dynamically select and utilize the appropriate MCP server based on the task requirements, enabling a highly flexible and powerful agentic system.

## Prerequisites

Before setting up the project, ensure you have the following installed:

-   **Python 3.9+**: Recommended for compatibility with AutoGen and other libraries.
-   **pip**: Python package installer (usually comes with Python).
-   **Git**: For cloning the repository.

## Setup and Installation

Follow these steps to get the project up and running on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/AgenticAIAutoGen.git
    cd AgenticAIAutoGen
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment:**
    *   **On Windows:**
        ```bash
        .venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure environment variables:**
    Create a `.env` file in the root directory of the project. This file will store sensitive information like database credentials and API keys.

    Example `.env` file:
    ```dotenv
    MYSQL_MCP_SERVER_URL="http://localhost:8001"
    REST_API_MCP_SERVER_URL="http://localhost:8002"
    FILE_SYSTEM_MCP_SERVER_URL="http://localhost:8003"
    
    # Example: Database Credentials (adjust as per your MySQL setup)
    DB_HOST="localhost"
    DB_PORT="3306"
    DB_USER="your_db_user"
    DB_PASSWORD="your_db_password"
    DB_NAME="your_database_name"

    # Example: External API Key (if needed by your Rest API MCP)
    EXTERNAL_API_KEY="your_external_api_key"

    # Other relevant environment variables...
    ```
    **Note**: Replace placeholder values with your actual configuration. Ensure your MCP servers are running and accessible at the specified URLs.

## Usage

This project contains several scripts demonstrating different aspects of AutoGen and MCP integration.

To run a specific example:

```bash
python your_script_name.py
```

For instance:

-   `python agentwithmcptooling.py`: Demonstrates an agent utilizing MCP tools.
-   `python multiagent.py`: Showcases multi-agent conversations.
-   `python selectorgroupchat.py`: Illustrates a group chat with selective agent participation.
-   `python scenario1.py`: Runs a specific agentic scenario.
-   `python framework/scenario2.py`: Runs another agentic scenario within the framework.

Refer to the individual script files for more details on their specific functionality and expected outputs.

## Project Structure

```
.
├── agentwithmcptooling.py        # Example script: Agent using MCP tools
├── algebra_help_simple_addition.txt  # Auxiliary file (contextual for agents)
├── basics1.py                    # Basic AutoGen example
├── homepage.png                  # UI asset
├── humaninloop.py                # Example script: Human-in-the-loop interaction
├── imageProcessing.py            # Example script: Image processing with agents
├── landing-page.png              # UI asset
├── multiagent.py                 # Example script: Multi-agent conversation
├── requirements.txt              # Project dependencies
├── savestate.py                  # Example script: Agent state saving
├── scenario1.py                  # Agentic scenario 1
├── selectorgroupchat.py          # Example script: Group chat with selective agents
├── .env.example                  # Example environment variables file (create .env from this)
├── assets/                       # Static assets
│   └── samplepic.png             # Sample image asset
└── framework/                    # Core framework components
    ├── __init__.py               # Python package initializer
    ├── agentFactory.py           # Factory for creating agents
    ├── mcp_config.py             # MCP server configuration
    └── scenario2.py              # Agentic scenario 2
```

*(Note: `.git`, `.idea`, and `.venv` directories are omitted for brevity in the project structure overview.)*

## Contributing

Contributions are welcome! Please follow standard practices: fork the repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
