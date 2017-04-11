## Telegram bot for Prometheus Alertmanager

# USAGE

- Create config file (config.yaml) for script with
```
chat_id: "CHAT_ID"
token: "BOT_TOKEN"
```

- Run this script on Flask+Uwsgi+Nginx stack

- Change config.yml in alertmanager:


```
receivers:
  - name: "team-tg"
    webhook_configs:
    - url: 'http://bot_ip:bot_port'
      send_resolved: true
```

