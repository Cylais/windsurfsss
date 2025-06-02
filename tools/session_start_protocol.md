# Session Start Protocol Reference

> **Onboarding & Automation:**
>
> - See also: README.md, docs/AGENT_GUIDE.md, tools/memory_system_guide.ps1
> - For agent API: tools/agent_interface.py
> - For CLI automation: tools/memory_cli.py, run_tests.py
> - For protocol scripting: tools/session_start_protocol.md (this file)
> - For CI: Use run_tests.py and memory sync checks before session start
>
> **Purpose:** This protocol is for both human contributors and automated agents. It ensures every session begins with a fully analyzed, understood, and synchronized memory system, and a clear commitment to all project rules and protocols.

---

## Step-by-Step Checklist (Manual or Automated)

1. **Discover and read all rules/memory/context files**  
   - Human: Review `rules/`, `memory-bank/`, and docs.
   - Agent: Use agent_interface.py to load all relevant files.
2. **Internalize and commit to rules**  
   - Human: Confirm understanding of all protocols and rules.
   - Agent: Call `acknowledge_protocols()` from agent_interface.py.
3. **Initialize dual-layer memory system**  
   - Human: Confirm file and DB layers are accessible.
   - Agent: Use CLI/API to check both layers.
4. **Synchronize and validate**  
   - Human: Run `python tools/check_memory_sync.py` or use CLI.
   - Agent: Call sync/status check methods.
5. **Load session context**  
   - Human: Review context files.
   - Agent: Use agent memory/context loading methods.
6. **Acknowledge readiness**  
   - Human: Verbally or in writing, confirm all systems go.
   - Agent: Log readiness event (see agent_interface.py).

---

## Usage Examples

- **Manual:**
  - Follow the above checklist before starting any new session.
  - Run: `python tools/check_memory_sync.py` and review output.
  - Run: `python run_tests.py` to ensure all tests pass.
  - Archive a session log (e.g., `logs/session_start.log`).
- **Agent/Automation:**
  - Call `session_start_protocol()` or equivalent API in agent_interface.py:

    ```python
    from agent_interface import AgentMemoryInterface
    agent = AgentMemoryInterface(agent_id="Architect")
    agent.session_start_protocol()
    ```

  - Use CLI: `python tools/memory_cli.py list agent` to confirm agent registry.
  - Add to CI:

    ```sh
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    python run_tests.py --coverage
    python tools/check_memory_sync.py
    # Optionally, log protocol status
    echo "Session start protocol completed" >> logs/session_start.log
    ```

## Automation/Scripting Stub

- To check protocol adherence or trigger the protocol in automation:
  - Use agent_interface.py:

    ```python
    from agent_interface import AgentMemoryInterface
    agent = AgentMemoryInterface(agent_id="Architect")
    agent.session_start_protocol()
    ```

  - Use CLI: `python tools/check_memory_sync.py`
  - Example PowerShell:

    ```powershell
    python tools/check_memory_sync.py
    if ($LASTEXITCODE -eq 0) { Write-Host "Session start protocol succeeded" }
    else { Write-Error "Session start protocol failed" }
    ```

  - Example Bash:

    ```bash
    python tools/check_memory_sync.py
    if [ $? -eq 0 ]; then echo "Session start protocol succeeded"; else echo "Session start protocol failed"; fi
    ```

  - Log the outcome to a session log file for traceability.

## Cross-References

- [Session Start Protocol in rules/session_management.rules.md](../rules/session_management.rules.md)
- [Memory System Documentation in memory-bank/MEMORY_SYSTEM.md](../memory-bank/MEMORY_SYSTEM.md)
- [Agent Interface API](agent_interface.py)
- [CLI Reference](memory_cli.py)
- [Test Runner](../run_tests.py)

---

## Agent/Role Template

To onboard a new agent or role, copy and adapt the following template:

```python
from agent_interface import AgentMemoryInterface

class NewAgent(AgentMemoryInterface):
    def __init__(self, agent_id):
        super().__init__(agent_id=agent_id)
        # Define agent-specific responsibilities or workflows here

    def session_start_protocol(self):
        # Optionally override to add custom startup logic
        super().session_start_protocol()

    def session_end_protocol(self):
        # Optionally override to add custom shutdown logic
        super().session_end_protocol()

# Example usage
agent = NewAgent(agent_id="YourRole")
agent.session_start_protocol()
```

- **Guidance:**
  - Assign a unique `agent_id` for each new agent/role.
  - Override protocol methods only if specialized behavior is needed.
  - Register the new agent in your team/project documentation as needed.

## Protocol Self-Test

You can self-test the protocol to ensure all required files, steps, and integrations are present:

- **Command:**
  - `python tools/session_start_protocol.md --self-test`
- **Stub Implementation:**

```python
# In session_start_protocol.md or a supporting script
def self_test():
    missing = []
    # Check for required files
    for path in ["rules/", "memory-bank/", "agent_interface.py"]:
        if not os.path.exists(path):
            missing.append(path)
    # Check for required methods or hooks
    # ... (add more checks as needed)
    if missing:
        print("Self-test failed. Missing:", missing)
        return False
    print("Self-test passed. All protocol requirements met.")
    return True
```

- **CI Integration:** Add the self-test command to your CI pipeline to catch onboarding/configuration issues early.

## Troubleshooting Tips

- If any step fails (e.g., sync fails or rules are not acknowledged):
  - Review logs in `logs/session_start.log` or CLI output.
  - Consult `tools/check_memory_sync.py` for details.
  - Contact the Architect agent or team lead for resolution.
  - See also: [Session End Protocol](session_end_protocol.md) for full session lifecycle.

```python
# Pseudocode for Session Start Protocol

def session_start_protocol():
    # 1. Discover and read all rules/memory/context files (Agent/Human)
    rules = read_files('rules/')
    context_files = read_files('memory-bank/')
    docs = read_files(['memory-bank/README.md', 'memory-bank/MEMORY_SYSTEM.md'])

    # 2. Internalize and commit to rules (Agent/Human)
    internalize_rules(rules + docs)
    log_session_rules(rules)  # Log to session_start.log

    # 3. Initialize dual-layer system (Agent/Human)
    file_layer_ok = check_file_layer('memory-bank/')
    db_layer_ok = check_db_layer('memory-bank/windsurf_memory.db')
    unified_ok = test_unified_memory_interface()

    # 4. Synchronize and validate (Agent/Human)
    sync_ok = run_sync_and_check()
    conflicts_ok = check_conflicts('_conflicts/')

    # 5. Load context (Agent/Human)
    session_context = load_context(context_files)

    # 6. Acknowledge readiness (Agent/Human)
    if all([file_layer_ok, db_layer_ok, unified_ok, sync_ok, conflicts_ok]):
        log_success('Session Start Protocol Complete: All systems go.', logfile='logs/session_start.log')
        notify_team('Session Start Protocol Complete')
    else:
        log_failure('Session Start Protocol Failed: Issues detected.', logfile='logs/session_start.log')
        notify_team('Session Start Protocol Failed')
```
