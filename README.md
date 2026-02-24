## Production-Grade AI Newsletter Agent

This project is a small **AI-powered newsletter generator** built with **FastAPI** and **Inngest**. It:

- Listens for `newsletter/generate` events via Inngest
- Searches the web for recent articles on a topic using **Bright Data SERP** (via `langchain-brightdata`)
- Generates a markdown newsletter using **OpenAI** through the Inngest AI adapter
- Saves the result into the local `newsletters/` folder

The file `run.py` is a simple load generator that can send many `newsletter/generate` events to Inngest.

---

## Project structure

- `main.py` – FastAPI app and Inngest function `generate_newsletter`
- `newsletter_service.py` – web search and AI-powered newsletter generation
- `prompts.py` – system and user prompts for the newsletter
- `custom_types.py` – Pydantic model `NewsletterRequest`
- `run.py` – example script to send many `newsletter/generate` events
- `pyproject.toml` – Python project metadata and dependencies
- `uv.lock` – lockfile for the `uv` package manager

---

## Prerequisites

- **Python**: version **3.12+** (see `.python-version`)
- **Package manager**:
  - Recommended: [`uv`](https://docs.astral.sh/uv/) (uses `pyproject.toml` and `uv.lock`)
  - Alternatively: standard `pip` (can install the project via `pyproject.toml`)
- **API keys**:
  - OpenAI API key
  - Bright Data SERP API key
- (Optional but recommended) **Inngest account and CLI** if you want a full Inngest dev setup

---

## Environment variables

Create a `.env` file in the project root with at least:

```env
OPENAI_API_KEY=your-openai-api-key
BRIGHT_DATA_API_KEY=your-bright-data-serp-api-key
```

Do **not** commit real keys to version control.

`python-dotenv` is used, so `main.py` and `run.py` will automatically load `.env`.

---

## Installing dependencies

You can use either **uv (recommended)** or **pip**.

### Option 1: Using uv (recommended)

Install `uv` if you do not have it yet (see official docs for the latest install command), then:

```bash
cd /Users/srimanikandanr/My\ Files/Projects/Production-Grade\ AI-Agent
uv sync
```

This will create and populate a virtual environment based on `pyproject.toml` and `uv.lock`.

### Option 2: Using pip

Create and activate a virtual environment (recommended), then install the project:

```bash
cd "/Users/srimanikandanr/My Files/Projects/Production-Grade AI-Agent"
python -m venv .venv
source .venv/bin/activate  # on macOS / Linux

pip install .  # installs dependencies from pyproject.toml
```

---

## Running the API server

The main FastAPI app is defined in `main.py` and can be started directly.

### With uv

```bash
cd "/Users/srimanikandanr/My Files/Projects/Production-Grade AI-Agent"
uv run main.py
```

### With plain Python

```bash
cd "/Users/srimanikandanr/My Files/Projects/Production-Grade AI-Agent"
python main.py
```

By default, `main.py` starts **uvicorn** on:

- **Host**: `0.0.0.0`
- **Port**: `8000`

So the FastAPI app will be available at `http://localhost:8000`.

---

## Inngest function and events

`main.py` defines an Inngest function:

- **Function ID**: `Generate Newsletter`
- **Trigger event**: `newsletter/generate`

This function:

- Reads the event payload into `NewsletterRequest` (`topic`, `max_articles`)
- Searches the web for recent articles about the topic
- Calls OpenAI (via Inngest AI adapter) to generate newsletter content
- Saves a markdown file into the `newsletters/` directory

To use this with a full Inngest dev setup (CLI + dashboard), point Inngest to the FastAPI app (served by `main.py`) following the Inngest FastAPI integration docs.

### Running the Inngest Dev Server locally

With your FastAPI app running on `http://127.0.0.1:8000` (for example via `uv run main.py`), you can start the Inngest Dev Server in another terminal with:

```bash
npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery
```

This connects the Dev Server to your local Inngest endpoint and lets you see and debug `newsletter/generate` events and function runs.

---

## Sending test events with run.py

`run.py` is an **example event generator** that sends many `newsletter/generate` events using the Inngest Python SDK.


You can run:

### With uv

```bash
cd "/Users/srimanikandanr/My Files/Projects/Production-Grade AI-Agent"
uv run run.py
```

### With plain Python

```bash
cd "/Users/srimanikandanr/My Files/Projects/Production-Grade AI-Agent"
python run.py
```

This script:

- Randomly picks topics from the `topics` list
- Sends many `newsletter/generate` events concurrently
- Prints whether each event send succeeded or failed

As Inngest executes the `Generate Newsletter` function, markdown files will be created in the `newsletters/` directory.

---

## Quick recap

- **Configure env vars** in `.env` (`OPENAI_API_KEY`, `BRIGHT_DATA_API_KEY`)
- **Install deps** via `uv sync` or `pip install .`
- **Start the API**: `uv run main.py` or `python main.py`
- **Integrate with Inngest** (CLI / dashboard) and then
- **Send events** with `run.py` to generate newsletters in `newsletters/`

