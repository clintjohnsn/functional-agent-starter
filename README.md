[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTE3IDE2VjdsLTYgNU0yIDlWOGwxLTFoMWw0IDMgOC04aDFsNCAyIDEgMXYxNGwtMSAxLTQgMmgtMWwtOC04LTQgM0gzbC0xLTF2LTFsMy0zIi8+PC9zdmc+)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/clintjohnsn/functional-langgraph-fastapi-starter)

# 🚀 functional-agent-starter

A production-ready, opinionated starter template for building LangGraph agents with FastAPI, functional programming style. Designed for scalability, observability, and long-running AI workflows using modern Python best practices. All components are fully open-source and deployable anywhere.

## 🎯 Key Features
🦜 **[Functional LangGraph](https://github.com/langchain-ai/langgraph)**: Built with LangGraph's new functional API, enabling deterministic, composable, and stateful AI agent logic. LangGraph is a low-level orchestration framework for building, managing, and deploying long-running, stateful LLM agents and workflows — including agentic and multi-agent systems.

⚡ **[FastAPI](https://github.com/fastapi/fastapi)**: High-performance async web framework to serve your LangGraph server via HTTP endpoints.

📊 **[Langfuse](https://github.com/langfuse/langfuse) Integration**: Monitor, trace, and debug your LLM workflows with Langfuse (fully wired for LLMOps).

🧠 **[Ell](https://docs.ell.so/#)** for LMP-style (Language Model Program) LLM calls - treating prompts as pure functions for lightweight, functional LLM programming OR **[Langchain](https://github.com/langchain-ai/langchain)** for more fine-grained, tool-oriented agent control. Easily separate prompts from code using Ell’s prompt management or externalize them with Langfuse.

🔍 **[Pydantic](https://github.com/pydantic/pydantic)**: Modern data validation, parsing, and settings management using Pydantic BaseModel and Settings.

 💾 **[PostgreSQL](https://www.postgresql.org/) for Checkpointing**: Durable, persistent storage of LangGraph agent state using PostgreSQL as the backing store. Ensures long-running processes can pause/resume deterministically.

🐳 **[Docker](https://www.docker.com/) + Docker Compose**: Containerized for reproducible local dev, CI, and production deployments.


### Developer Experience
- 🧪 **Testing**: Pre-wired [Pytest Test Suite](https://docs.pytest.org/en/stable/) suite with [Coverage.py](https://github.com/nedbat/coveragepy).
- 📦 **[uv](https://github.com/astral-sh/uv)** for packaging and dependency management
- 🤖 **[Poe the Poet](https://github.com/nat-n/poethepoet)** for tasks
- ✅ **[Pre-commit](https://pre-commit.com/), [Mypy](https://github.com/python/mypy)**, and **[Ruff](https://github.com/astral-sh/ruff)** to apease the code linting gods
- 🧰 **[Dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates)** for Dependency updates

## 📁 Project Structure
**Opinionated Project Structure**: A modular, enterprise-ready architecture with clear separation of concerns, ideal for small to medium scale projects and flexible enough to grow into large systems.

```
.
├── src/
│   └── server/
│       ├── clients/             # Clients and integrations         
│       ├── config/              # Application settings and environment config
│       │   └── settings.py
│       ├── models/              # Data models, DTOs, exception schemas, etc.
│       ├── routes/api/v1        # Routes and error handlers
│       │   ├── api.py
│       │   └── errors.py
│       ├── workflows/           # LangGraph workflows and entry point
│       │   └── base.py          # Base Workflow, helper functions
│       ├── services/            # Service Layer for business logic
│       ├── middleware/          # Middleware Layer
│       │   └── rate_limiter.py  # Rate limiter
│       │   └── auth.py          # Auth
│       ├── main.py              # Server / Entry Point
├── tests/                       # Pytest-based test suite
├── .env.example                 # Example environment variables
├── pre-commit-config.yaml       # Pre-commit hooks configuration
├── docker-compose.yml           # Local development stack
├── Dockerfile                   # Production Docker spec
├── pyproject.toml               # Dependency and tooling configuration


```

## 👟 Get Started

To serve this app, run:

```sh
docker compose up app
```

and open [localhost:8000](http://localhost:8000) in your browser.

Within the Dev Container this is equivalent to:

```sh
poe serve
```

## 🛣️ Roadmap
Planned features and improvements:
- 🔐 Authentication via Supabase
- 📡 Advanced Observability using OpenTelemetry
- 🔄 LangGraph Convenience Features like reusable agent templates, dynamic graph modification, and standardized graph IO interfaces
- 🧪 Evaluation with Ragas

## 🌱 Contributing

PRs, feedback, and issues are welcome! This is an open project designed to evolve with the LLM ecosystem.

<details>
<summary>Prerequisites</summary>

1. [Generate an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key) and [add the SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).
1. Configure SSH to automatically load your SSH keys:

    ```sh
    cat << EOF >> ~/.ssh/config
    
    Host *
      AddKeysToAgent yes
      IgnoreUnknown UseKeychain
      UseKeychain yes
      ForwardAgent yes
    EOF
    ```

1. [Install Docker Desktop](https://www.docker.com/get-started).
1. [Install VS Code](https://code.visualstudio.com/) and [VS Code's Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). Alternatively, install [PyCharm](https://www.jetbrains.com/pycharm/download/).
1. _Optional:_ install a [Nerd Font](https://www.nerdfonts.com/font-downloads) such as [FiraCode Nerd Font](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/FiraCode) and [configure VS Code](https://github.com/tonsky/FiraCode/wiki/VS-Code-Instructions) or [PyCharm](https://github.com/tonsky/FiraCode/wiki/Intellij-products-instructions) to use it.

</details>

<details open>
<summary>Development environments</summary>

The following development environments are supported:

1. ⭐️ _VS Code Dev Container (with container volume)_: click on [Open in Dev Containers](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/clintjohnsn/functional-langgraph-fastapi-starter) to clone this repository in a container volume and create a Dev Container with VS Code.
1. ⭐️ _uv_: clone this repository and run the following from root of the repository:

    ```sh
    # Create and install a virtual environment
    uv sync --python 3.12 --all-extras

    # Activate the virtual environment
    source .venv/bin/activate

    # Install the pre-commit hooks
    pre-commit install --install-hooks
    ```

1. _VS Code Dev Container_: clone this repository, open it with VS Code, and run <kbd>Ctrl/⌘</kbd> + <kbd>⇧</kbd> + <kbd>P</kbd> → _Dev Containers: Reopen in Container_.
1. _PyCharm Dev Container_: clone this repository, open it with PyCharm, [create a Dev Container with Mount Sources](https://www.jetbrains.com/help/pycharm/start-dev-container-inside-ide.html), and [configure an existing Python interpreter](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#widget) at `/opt/venv/bin/python`.

</details>

<details open>
<summary>Developing</summary>

- Run `poe` from within the development environment to print a list of [Poe the Poet](https://github.com/nat-n/poethepoet) tasks available to run on this project.
- Run `uv add {package}` from within the development environment to install a run time dependency and add it to `pyproject.toml` and `uv.lock`. Add `--dev` to install a development dependency.
- Run `uv sync --upgrade` from within the development environment to upgrade all dependencies to the latest versions allowed by `pyproject.toml`. Add `--only-dev` to upgrade the development dependencies only.

</details>
