# Claude Code Research

## Overview
**Claude Code** is an agentic coding tool developed by Anthropic that runs directly in the terminal. It is designed to understand codebases, automate routine tasks, and handle complex workflows using natural language commands. Unlike standard CLI tools, Claude Code acts as an intelligent assistant that can edit files, run terminal commands, and manage git operations autonomously under user supervision.

## Key Features & Capabilities
*   **Codebase Understanding**: capable of reading and analyzing files within the project directory to provide context-aware assistance.
*   **File Editing**: Can directly modify code files based on instructions.
*   **Terminal Execution**: Can run shell commands to build, test, or deploy applications.
*   **Git Integration**: Handles git workflows, including committing changes and managing branches.
*   **Natural Language Interface**: Users interact with it using plain English (or other languages) directly in the command line.
*   **Plugin System**: Supports plugins to extend functionality with custom commands and agents.

## Installation
Anthropic provides several methods for installation depending on the operating system.

### MacOS / Linux (Recommended)
```bash
curl -fsSL https://claude.ai/install.sh | bash
```
*Alternatively via Homebrew:*
```bash
brew install --cask claude-code
```

### Windows (Recommended)
```powershell
irm https://claude.ai/install.ps1 | iex
```
*Alternatively via WinGet:*
```powershell
winget install Anthropic.ClaudeCode
```

### NPM (Deprecated)
While available as `@anthropic-ai/claude-code` on NPM, the official documentation lists this method as deprecated in favor of the standalone installers.
```bash
npm install -g @anthropic-ai/claude-code
```

## Usage
1.  **Start the Tool**: Navigate to your project directory and run:
    ```bash
    claude
    ```
2.  **Authentication**: On first run, it will likely require authentication with an Anthropic account.
3.  **Interaction**: Type commands or requests in natural language.
    *   *Example:* "Fix the bug in the login function."
    *   *Example:* "Run tests and explain any failures."
    *   *Example:* "Refactor utils.py to improve readability."

## Resources
*   **Official Repository**: [https://github.com/anthropics/claude-code](https://github.com/anthropics/claude-code)
*   **Documentation**: [https://code.claude.com/docs/en/overview](https://code.claude.com/docs/en/overview)
*   **NPM Package**: [https://www.npmjs.com/package/@anthropic-ai/claude-code](https://www.npmjs.com/package/@anthropic-ai/claude-code)
