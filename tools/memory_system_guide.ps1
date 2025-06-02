<#
.SYNOPSIS
    Interactive guide for using the Windsurf Unified Memory System.
.DESCRIPTION
    This script provides an interactive, menu-driven guide to help users understand and use
    the Unified Memory System. It covers onboarding, API references, memory management, and troubleshooting.

.NOTES
    - Onboarding: See README.md, docs/AGENT_GUIDE.md
    - Memory Protocols: docs/memory-protocols.md, tools/unified_memory.py
    - Python Parity: For every PowerShell operation, see Python equivalents in tools/memory_cli.py and tools/agent_interface.py
    - Prerequisite: Python memory system must be initialized for cross-platform parity.
    - Scripting/Automation: See stub at end of file for CI/onboarding integration.

.EXAMPLE
    # Run the guide interactively
    ./memory_system_guide.ps1

    # Python equivalent (for automation/onboarding):
    python tools/memory_cli.py list agent
    python tools/agent_interface.py --help
#>
# ==========================
# This guide provides information about the Windsurf Project's unified memory system.
# It includes API references, usage examples, and best practices for agents.
# For parity, see Python scripts in tools/.
#
# Last Updated: $(Get-Date -Format "yyyy-MM-dd")

# Colors for better output
$colors = @{
    success = 'Green'
    error   = 'Red'
    warning = 'Yellow'
    info    = 'Cyan'
    highlight = 'Magenta'
}

# Helper functions for the interactive guide

# Helper functions
function Show-Header($title) {
    Write-Host "`n$('=' * 80)" -ForegroundColor $colors.highlight
    Write-Host $title -ForegroundColor $colors.highlight
    Write-Host $('=' * $title.Length) -ForegroundColor $colors.highlight
    Write-Host ""
}

function Show-Section($title) {
    Write-Host "`n$title" -ForegroundColor $colors.highlight
    Write-Host $('-' * $title.Length) -ForegroundColor $colors.highlight
}

function Show-MainMenu {
    Show-Header "Windsurf Project - Unified Memory System"
    
    Write-Host "1. Getting Started" -ForegroundColor $colors.info
    Write-Host "2. Agent API Reference" -ForegroundColor $colors.info
    Write-Host "3. Memory Management" -ForegroundColor $colors.info
    Write-Host "4. Integration Guide" -ForegroundColor $colors.info
    Write-Host "5. Troubleshooting" -ForegroundColor $colors.info
    Write-Host "6. About the Unified Memory System" -ForegroundColor $colors.info
    Write-Host "Q. Quit" -ForegroundColor $colors.highlight
    Write-Host ""
}

function Show-Warning {
    param($text)
    Write-Host "[!] $text" -ForegroundColor $colors.warning
}

function Show-CommandReference {
    Show-Header "Agent API Reference"
    
    Show-Section "Core Commands"
    Write-Host "1. Initialize the agent interface:" -ForegroundColor $colors.highlight
    Write-Host "   from agent_interface import AgentMemoryInterface" -ForegroundColor $colors.info
    Write-Host ""
    Write-Host "2. Log activities:" -ForegroundColor $colors.highlight
    Write-Host "   agent.log_activity('task_started', {'task': 'Implement feature X'})" -ForegroundColor $colors.info
    Write-Host ""
    Write-Host "3. Share knowledge:" -ForegroundColor $colors.highlight
    Write-Host "   agent.share_knowledge('How to use the API', tags=['documentation', 'api'])" -ForegroundColor $colors.info
    
    Show-Section "Memory Management"
    Write-Host "1. Create entities:" -ForegroundColor $colors.highlight
    Write-Host "   agent.create_entity('task', {'name': 'Implement feature X'})" -ForegroundColor $colors.info
    Write-Host ""
    Write-Host "2. Update entities:" -ForegroundColor $colors.highlight
    Write-Host "   agent.update_entity('task', {'name': 'Implement feature X', 'status': 'in_progress'})" -ForegroundColor $colors.info
    Write-Host ""
    Write-Host "3. Delete entities:" -ForegroundColor $colors.highlight
    Write-Host "   agent.delete_entity('task', {'name': 'Implement feature X'})" -ForegroundColor $colors.info
    
    Show-Section "Relationships"
    Write-Host "1. Create relationships:" -ForegroundColor $colors.highlight
    Write-Host "   agent.create_relationship('task', 'depends_on', 'requirement')" -ForegroundColor $colors.info
    Write-Host ""
    Write-Host "2. Update relationships:" -ForegroundColor $colors.highlight
    Write-Host "   agent.update_relationship('task', 'depends_on', 'requirement', {'status': 'resolved'})" -ForegroundColor $colors.info
    Write-Host ""
    Write-Host "3. Delete relationships:" -ForegroundColor $colors.highlight
    Write-Host "   agent.delete_relationship('task', 'depends_on', 'requirement')" -ForegroundColor $colors.info
    
    Write-Host "`nFor more information, see the documentation in memory-bank/README.md`n" -ForegroundColor $colors.info
}

function Show-MemoryManagement {
    Show-Header "Memory Management"
    
    Write-Host "Best practices for managing memory in the unified system:" -ForegroundColor $colors.info
    Write-Host ""
    
    Show-Section "Structured Data"
    Write-Host "- Use consistent entity types (e.g., 'task', 'decision', 'requirement')" -ForegroundColor $colors.info
    Write-Host "- Include relevant metadata (created_at, updated_by, etc.)" -ForegroundColor $colors.info
    Write-Host "- Use tags for flexible categorization" -ForegroundColor $colors.info
    Write-Host ""
    
    Show-Section "Relationships"
    Write-Host "- Create meaningful relationships between entities" -ForegroundColor $colors.info
    Write-Host "- Use descriptive relationship types" -ForegroundColor $colors.info
    Write-Host "- Include relationship metadata when relevant" -ForegroundColor $colors.info
    Write-Host ""
    
    Show-Section "Performance"
    Write-Host "- Keep individual entities focused and concise" -ForegroundColor $colors.info
    Write-Host "- Use relationships instead of duplicating content" -ForegroundColor $colors.info
    Write-Host "- Batch operations when possible" -ForegroundColor $colors.info
}

function Show-IntegrationGuide {
    Show-Header "Integration Guide"
    
    Write-Host "How to integrate with the unified memory system:" -ForegroundColor $colors.info
    Write-Host ""
    
    Show-Section "For Cascade Agents"
    Write-Host "1. Import the agent interface:" -ForegroundColor $colors.highlight
    Write-Host "   from agent_interface import AgentMemoryInterface" -ForegroundColor $colors.info
    Write-Host ""
    Write-Host "2. Initialize with your agent details:" -ForegroundColor $colors.highlight
    Write-Host "   agent = AgentMemoryInterface('agent_id', 'agent_type')" -ForegroundColor $colors.info
    Write-Host ""
    Write-Host "3. Use the provided methods to interact with memory" -ForegroundColor $colors.info
    
    Show-Section "For External Tools"
    Write-Host "1. Direct File Access:" -ForegroundColor $colors.highlight
    Write-Host "   - Read/write markdown files in memory-bank/" -ForegroundColor $colors.info
    Write-Host "   - Files are automatically synced to the database" -ForegroundColor $colors.info
    Write-Host ""
    Write-Host "2. SQLite Database:" -ForegroundColor $colors.highlight
    Write-Host "   - Directly query memory-bank/windsurf_memory.db" -ForegroundColor $colors.info
    Write-Host "   - See database_schema.md for table structures" -ForegroundColor $colors.info
    
    Show-Section "Synchronization"
    Write-Host "- Automatic: Changes are synced in real-time" -ForegroundColor $colors.info
    Write-Host "- Manual: Run 'python tools/sync_memory.py' to force sync" -ForegroundColor $colors.info
    Write-Host "- Status: Check 'python tools/check_memory_sync.py'" -ForegroundColor $colors.info
}

function Show-Troubleshooting {
    Show-Header "Troubleshooting"
    
    Write-Host "Common issues and their solutions:" -ForegroundColor $colors.info
    Write-Host ""
    
    Show-Section "Connection Issues"
    Write-Host "1. Cannot connect to database:" -ForegroundColor $colors.highlight
    Write-Host "   - Verify the database file exists: memory-bank/windsurf_memory.db" -ForegroundColor $colors.info
    Write-Host "   - Check file permissions on the database file" -ForegroundColor $colors.info
    Write-Host "   - Ensure no other process has locked the database`n" -ForegroundColor $colors.info
    
    Show-Section "Data Issues"
    Write-Host "2. Missing or outdated data:" -ForegroundColor $colors.highlight
    Write-Host "   - Run manual sync: python tools/sync_memory.py" -ForegroundColor $colors.info
    Write-Host "   - Check for sync errors in logs/memory_sync.log" -ForegroundColor $colors.info
    Write-Host "   - Verify file permissions in memory-bank/`n" -ForegroundColor $colors.info
    
    Show-Section "Performance Issues"
    Write-Host "3. Slow queries:" -ForegroundColor $colors.highlight
    Write-Host "   - Add indexes for frequently queried fields" -ForegroundColor $colors.info
    Write-Host "   - Optimize complex queries" -ForegroundColor $colors.info
    Write-Host "   - Consider denormalizing hot data`n" -ForegroundColor $colors.info
    
    Show-Section "Getting Help"
    Write-Host "If you're still having issues:" -ForegroundColor $colors.info
    Write-Host "1. Check the logs in the logs/ directory" -ForegroundColor $colors.info
    Write-Host "2. Review the documentation in memory-bank/" -ForegroundColor $colors.info
    Write-Host "3. Contact the Windsurf development team" -ForegroundColor $colors.info
}

function Show-GettingStarted {
    Show-Header "Getting Started with the Unified Memory System"
    
    Write-Host "The Unified Memory System provides a consistent way for all agents to" -ForegroundColor $colors.info
    Write-Host "store, retrieve, and share information across the entire Windsurf ecosystem." -ForegroundColor $colors.info
    Write-Host ""
    
    Show-Section "Quick Start for Agents"
    Write-Host "1. Import the agent interface in your code:" -ForegroundColor $colors.highlight
    Write-Host "   from agent_interface import AgentMemoryInterface" -ForegroundColor $colors.info
    Write-Host ""
    
    Write-Host "2. Initialize with your agent details:" -ForegroundColor $colors.highlight
    Write-Host "   agent = AgentMemoryInterface(" -ForegroundColor $colors.info
    Write-Host "       agent_id='your_agent_id'," -ForegroundColor $colors.info
    Write-Host "       agent_type='your_agent_type'  # e.g., 'coder', 'reviewer', 'tester'" -ForegroundColor $colors.info
    Write-Host "   )" -ForegroundColor $colors.info
    Write-Host ""
    
    Write-Host "3. Start using the memory system:" -ForegroundColor $colors.highlight
    Write-Host "   # Log activities" -ForegroundColor $colors.info
    Write-Host "   agent.log_activity('task_started', {'task': 'Implement feature X'})" -ForegroundColor $colors.info
    Write-Host "   " -ForegroundColor $colors.info
    Write-Host "   # Share knowledge" -ForegroundColor $colors.info
    Write-Host "   agent.share_knowledge('How to use the API', tags=['documentation', 'api'])" -ForegroundColor $colors.info
    
    Show-Section "Key Features"
    Write-Host "- Unified Access: Single interface for all memory operations" -ForegroundColor $colors.info
    Write-Host "- Automatic Sync: Changes are immediately available to all agents" -ForegroundColor $colors.info
    Write-Host "- Context Awareness: Built-in support for agent context and relationships" -ForegroundColor $colors.info
    Write-Host "- Extensible: Easy to add new types of data and relationships" -ForegroundColor $colors.info
    
    Write-Host ""
    Write-Host "Use the interactive menu to explore more features and examples." -ForegroundColor $colors.highlight
}

function Show-About {
    Show-Header "About the Unified Memory System"
    
    Write-Host "The Unified Memory System provides a consistent, agent-agnostic way to manage" -ForegroundColor $colors.info
    Write-Host "project knowledge across the entire Windsurf ecosystem." -ForegroundColor $colors.info
    Write-Host ""
    
    Show-Section "Unified Architecture"
    Write-Host "- Single API for all memory operations" -ForegroundColor $colors.info
    Write-Host "- Consistent behavior across all agents" -ForegroundColor $colors.info
    Write-Host "- Automatic conflict resolution`n" -ForegroundColor $colors.info
    
    Show-Section "Dual-Layer Storage"
    Write-Host "- File-based memory (human-readable markdown)" -ForegroundColor $colors.info
    Write-Host "- SQLite database (efficient querying)" -ForegroundColor $colors.info
    Write-Host "- Automatic synchronization between layers`n" -ForegroundColor $colors.info
    
    Show-Section "Agent-Centric Design"
    Write-Host "- Built-in agent tracking" -ForegroundColor $colors.info
    Write-Host "- Activity logging" -ForegroundColor $colors.info
    Write-Host "- Context awareness`n" -ForegroundColor $colors.info
    
    Show-Section "Key Features"
    Write-Host "- Seamless integration with Cascade agents" -ForegroundColor $colors.info
    Write-Host "- Support for external tools and services" -ForegroundColor $colors.info
    Write-Host "- Comprehensive audit trail" -ForegroundColor $colors.info
    Write-Host "- Extensible data model" -ForegroundColor $colors.info
    Write-Host "- Built-in search and retrieval" -ForegroundColor $colors.info
}

# Main interactive menu
function Show-InteractiveMenu {
    do {
        Show-MainMenu
        $choice = Read-Host "`nSelect an option (1-6 or Q to quit)"
        
        switch ($choice) {
            '1' { 
                Show-GettingStarted
                $null = Read-Host "`nPress Enter to continue..."
            }
            '2' { 
                Show-CommandReference
                $null = Read-Host "`nPress Enter to continue..."
            }
            '3' { 
                Show-MemoryManagement
                $null = Read-Host "`nPress Enter to continue..."
            }
            '4' { 
                Show-IntegrationGuide
                $null = Read-Host "`nPress Enter to continue..."
            }
            '5' { 
                Show-Troubleshooting
                $null = Read-Host "`nPress Enter to continue..."
            }
            '6' { 
                Show-About
                $null = Read-Host "`nPress Enter to continue..."
            }
            'Q' { 
                Write-Host "`nThank you for using the Unified Memory System Guide!`n" -ForegroundColor $colors.success
                return
            }
            default {
                Write-Host "`nInvalid option. Please try again." -ForegroundColor $colors.error
                Start-Sleep -Seconds 1
            }
        }
    } while ($true)
}

# Start the interactive guide
Show-InteractiveMenu
