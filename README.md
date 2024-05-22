## software prerequisites

- git + github [IIoT School Mini-Course](https://www.skool.com/iiotschool/classroom/7e75039a)
- docker + docker-compose [IIoT School Mini-Course](https://www.skool.com/iiotschool/classroom/e2862b44)
- python + pipenv [IIoT School Mini-Course](https://www.skool.com/iiotschool/classroom/41753db0)

## Getting the lab setup

### overview

In general these are the two major steps that need to be completed after you clone the repo.

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

