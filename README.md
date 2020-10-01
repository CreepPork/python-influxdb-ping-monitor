# python-influxdb-ping-monitor

A simple Python script that pings your given endpoints and categorizes them which can be fed into an InfluxDB database (Telegraf), powering Grafana.

## Installation

```bash
git clone https://github.com/CreepPork/python-influxdb-ping-monitor
```

## Usage

1. Edit the `uptime.py` file to add your own services to monitor via ping
2. Configure your `telegraf.conf` (see example [here](#example-telegraf-configuration))
3. It will create a metric called `reachables`, use this in your Grafana dashboard
4. Ready!

### Example Telegraf configuration

```conf
[[inputs.exec]]
  commands = [
    '/usr/bin/python3 /etc/telegraf/inputs/uptime.py'
  ]
  interval="1m"
  timeout="30s"
  data_format="influx"
```

## Security

If you discover any security related issues, please email security@garkaklis.com instead of using the issue tracker.

## Credits

- [Ralfs Garkaklis](https://github.com/CreepPork)
- [All Contributors](https://github.com/CreepPork/python-influxdb-ping-monitor/contributors)

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
