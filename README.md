## prerequisites

- docker
- docker-compose
- python + pipenv

## getting started 

### overview

- create password file for mosquitto
- rename `template.secrets.toml` to `.secrets.toml` in `./client` and `./mock_publisher`

### create password file for mosquitto

#### bash

```bash
docker run \
--rm \
-it \
-v $(pwd)mosquitto/config:/mosquitto/config \
eclipse-mosquitto mosquitto_passwd -c /mosquitto/config/passwordfile iiotschool
```

#### powershell

```powershell
docker run `
--rm `
-it `
-v $(pwd)/config:/mosquitto/config `
eclipse-mosquitto mosquitto_passwd -c /mosquitto/config/passwordfile iiotschool
```

## resources

### mqtt clients
[mqttx](https://mqttx.app/downloads)
[mqtt explorer](https://mqtt-explorer.com/)

