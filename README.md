![Molecule test](https://github.com/pimvh/systemd_failmail/actions/workflow/test.yaml/badge.svg)
# Requirements

1. Ansible installed:

```
sudo apt install python3
python3 -m ensurepip --upgrade
pip3 install ansible
```

## Required variables

Review the variables as shown in defaults.

```
systemd_failmail_email: ""
```

The ansible playbook will validate whether the variables exist that you defined before running.

# Example playbook

```
hosts:
  - foo
roles:
  - pimvh.systemd-failmail

```

# Future Improvements

- Isolate service, running as non-root

# TLDR - What will happen if I run this

- Add a failmail service to your host. It will automatically be applied to all other services, to notify you of failures.

# Sources

- How to add global on failure dependency was taken from: [freedesktop.org](https://www.freedesktop.org/software/systemd/man/systemd.unit.html) (Example 3)
