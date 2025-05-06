# Раздел 3. Ansible

Для установки Docker в целевой системе выполняется Playbook `install_docker.yaml`, чтобы выполнить его локально (без подключения по SSH) в инвентори файле указан адрес 127.0.0.1. 

Команда для запуска (при хосте 127.0.0.1). Если хост удаленный - добавить в ``inventory.ini`` - данные для подключения по ssh, флаг connection исключить.

```bash
ansible-playbook -i inventory.ini --connection=local install_docker.yaml
```

Для сборки и запуска приложения - аналогично:


```bash
ansible-playbook -i inventory.ini --connection=local build_app.yaml
```

