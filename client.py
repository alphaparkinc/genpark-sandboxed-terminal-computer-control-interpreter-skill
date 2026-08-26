class SandboxedTerminalComputerControlInterpreterClient:
    def execute_sandboxed_computer_action(self, natural_language_command='Convert all HEIC images in Downloads folder to compressed WebP and generate zip archive', execution_runtime='BASH_AND_PYTHON_SANDBOX'):
        return {
            'interpreter_session_id': 'int_ctl_8812',
            'command': natural_language_command,
            'runtime': execution_runtime,
            'commands_synthesized_and_run': 3,
            'permission_sandbox_policy_enforced': True,
            'system_exit_code': 0,
            'execution_audit_log_url': 'https://interpreter.genpark.ai/logs/8812.log'
        }
