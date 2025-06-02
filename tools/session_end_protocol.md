# Session End Protocol Reference

> **Onboarding & Automation:**
>
> - See also: README.md, docs/AGENT_GUIDE.md, tools/memory_system_guide.ps1
> - For agent API: tools/agent_interface.py
> - For CLI automation: tools/memory_cli.py, run_tests.py
> - For protocol scripting: tools/session_end_protocol.md (this file)
> - For CI: Use run_tests.py and memory sync checks after session end
>
> **Purpose:** This protocol is for both human contributors and automated agents. It ensures every session ends with all memory, logs, and context saved, and a clear record of protocol adherence and session outcome.

---

## Step-by-Step Checklist (Manual or Automated)

1. **Log all final activities and decisions**  
   - Human: Summarize key actions and decisions in session log.
   - Agent: Use agent_interface.py to log final activities.
2. **Sync and save memory state**  
   - Human: Run `python tools/check_memory_sync.py` and resolve any issues.
   - Agent: Call sync/status check and commit methods.
3. **Archive session context and outputs**  
   - Human: Save session notes, outputs, and artifacts to designated location.
   - Agent: Use context archiving methods if available.
4. **Acknowledge protocol completion**  
   - Human: Confirm all protocols followed and session is complete.
   - Agent: Log protocol completion event (see agent_interface.py).
5. **Trigger post-session automation (optional)**  
   - Human: Notify team or trigger next workflow step.
   - Agent: Send notification or trigger next agent/task.

---

## Usage Examples

- **Manual:**
  - Follow the above checklist before ending any session.
  - Run: `python tools/check_memory_sync.py` and resolve issues.
  - Archive session notes and outputs (e.g., `logs/session_end.log`).
- **Agent/Automation:**
  - Call `session_end_protocol()` or equivalent API in agent_interface.py:

    ```python
    from agent_interface import AgentMemoryInterface
    agent = AgentMemoryInterface(agent_id="Architect")
    agent.session_end_protocol()
    ```

  - Use CLI: `python tools/memory_cli.py` to log final entity updates.
  - Add to CI:

    ```sh
    python tools/check_memory_sync.py
    python run_tests.py
    # Archive logs/artifacts here
    echo "Session end protocol completed" >> logs/session_end.log
    ```

## Automation/Scripting Stub

- To check protocol adherence or trigger the protocol in automation:
  - Use agent_interface.py:

    ```python
    from agent_interface import AgentMemoryInterface
    agent = AgentMemoryInterface(agent_id="Architect")
    agent.session_end_protocol()
    ```

  - Use CLI: `python tools/check_memory_sync.py`
  - Example PowerShell:

    ```powershell
    python tools/check_memory_sync.py
    if ($LASTEXITCODE -eq 0) { Write-Host "Session end protocol succeeded" }
    else { Write-Error "Session end protocol failed" }
    ```

  - Example Bash:

    ```bash
    python tools/check_memory_sync.py
    if [ $? -eq 0 ]; then echo "Session end protocol succeeded"; else echo "Session end protocol failed"; fi
    ```

  - Log the outcome to a session log file for traceability.

## Cross-References

- [Session End Protocol in rules/session_management.rules.md](../rules/session_management.rules.md)
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
agent.session_end_protocol()
```

- **Guidance:**
  - Assign a unique `agent_id` for each new agent/role.
  - Override protocol methods only if specialized behavior is needed.
  - Register the new agent in your team/project documentation as needed.

## Protocol Self-Test

You can self-test the protocol to ensure all required files, steps, and integrations are present:

- **Command:**
  - `python tools/session_end_protocol.md --self-test`
- **Stub Implementation:**

```python
# In session_end_protocol.md or a supporting script
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

- If any step fails (e.g., sync fails, archiving fails, or protocol completion not logged):
  - Review logs in `logs/session_end.log` or CLI output.
  - Consult `tools/check_memory_sync.py` for details.
  - Contact the Architect agent or team lead for resolution.
  - See also: [Session Start Protocol](session_start_protocol.md) for full session lifecycle.

```python
# Pseudocode for Session End Protocol

def session_end_protocol():
    # 1. Log all final activities and decisions (Agent/Human)
    log_final_activities()  # Log to session_end.log

    # 2. Sync and save memory state (Agent/Human)
    sync_ok = run_sync_and_check()

    # 3. Archive session context and outputs (Agent/Human)
    archive_session_context()  # Save outputs to logs/session_end.log

    # 4. Acknowledge protocol completion (Agent/Human)
    log_protocol_completion(logfile='logs/session_end.log')

    # 5. Trigger post-session automation (optional, Agent/Human)
    trigger_next_workflow()

    if sync_ok:
        log_success('Session End Protocol Complete: All systems logged.', logfile='logs/session_end.log')
        notify_team('Session End Protocol Complete')
    else:
        log_failure('Session End Protocol Failed: Issues detected.', logfile='logs/session_end.log')
        notify_team('Session End Protocol Failed')
```
