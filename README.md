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
  - systemd-failmail

```

# TLDR - What will happen if I run this

- Add a failmail service to your host. It will automatically be applied to all other services, to notify you of failures.
