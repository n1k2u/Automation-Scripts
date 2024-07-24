
import subprocess
import yaml

# playbook structure
playbook = [{
    'name': 'Configure Practice-Final System with specified requirements',
    'hosts': 'all',
    'become': 'yes',
    'vars': {
        'ansible_ssh_user': 'root',
        'ansible_ssh_pass': '123456',
    },
    'tasks': [
        {
            'name': 'Add a user \'jsmith\'',
            'ansible.builtin.user': {
                'name': 'jsmith',
                'password': "{{ 'Password123!' | password_hash('sha512') }}",
                'state': 'present'
            }
        },
        {
            'name': 'Give \'jsmith\' sudo permissions',
            'ansible.builtin.lineinfile': {
                'path': '/etc/sudoers',
                'line': 'jsmith ALL=(ALL) NOPASSWD:ALL',
                'validate': '/usr/sbin/visudo -cf %s'
            }
        },
        {
            'name': 'Disallow root SSH logins',
            'ansible.builtin.lineinfile': {
                'path': '/etc/ssh/sshd_config',
                'regexp': '^PermitRootLogin',
                'line': 'PermitRootLogin no'
            },
            'notify': ['restart ssh']
        },
        {
            'name': 'Stop and disable the apache service',
            'ansible.builtin.service': {
                'name': 'apache2',
                'state': 'stopped',
                'enabled': 'no'
            }
        }
    ],
    'handlers': [
        {
            'name': 'restart ssh',
            'ansible.builtin.service': {
                'name': 'ssh',
                'state': 'restarted'
            }
        }
    ]
}]

playbook_file = 'configure_practice_final.yml'
with open(playbook_file, 'w') as file:
    yaml.dump(playbook, file)

try:
    subprocess.run(['ansible-playbook', '-i', '10.12.0.20,', playbook_file], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error executing playbook: {e}")






