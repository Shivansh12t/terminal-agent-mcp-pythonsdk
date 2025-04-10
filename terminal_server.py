import os
import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("terminal")

DEFAULT_WORKSPACE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "workspace")

if not os.path.exists(DEFAULT_WORKSPACE):
    os.makedirs(DEFAULT_WORKSPACE)

@mcp.tool()
async def run_command(command: str) -> str:
    """
    Run a terminal command inside the workspace directory, the system is a windows system

    Args:
        command: The shell command to run
    
    Returns:
        The command output or an error message
    """
    try:
        result = subprocess.run(command, shell=True, cwd=DEFAULT_WORKSPACE, capture_output=True, 
                                text=True)
        return result.stdout or result.stderr
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    mcp.run(transport='stdio')