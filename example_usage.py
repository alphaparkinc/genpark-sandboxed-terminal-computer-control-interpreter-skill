from client import SandboxedTerminalComputerControlInterpreterClient

def main():
    client = SandboxedTerminalComputerControlInterpreterClient()
    res = client.execute_sandboxed_computer_action('Inspect network socket connections and identify runaway port listening processes')
    print('Interpreter Session: ' + res['interpreter_session_id'] + ' | Runtime: ' + res['runtime'])
    print('Commands Executed: ' + str(res['commands_synthesized_and_run']) + ' (Sandbox Policy Enforced: ' + str(res['permission_sandbox_policy_enforced']) + ')')
    print('Exit Code: ' + str(res['system_exit_code']) + ' | Audit Log: ' + res['execution_audit_log_url'])

if __name__ == '__main__':
    main()
