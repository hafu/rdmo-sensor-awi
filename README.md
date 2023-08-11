# RDMO Sensor AWI optionset plugin

Queries the [Sensor Information System](https://sensor.awi.de/) of the [Alfred-Wegener-Institut, Helmholtz-Zentrum für Polar- und Meeresforschung (AWI)](https://www.awi.de/).

This is an example optionset plugin, to show how to gather information from
other systems.

It was created during the RDMO Hackathon 2023.

## Setup

Install the plugins in your RDMO virtual environment using pip (directly from GitHub):

```bash
pip install git+https://github.com/hafu/rdmo-sensor-awi
```

Or when editing the code you can put the code a folder beneath your RDMO installation and install it with:

```bash
pip install -e ../rdmo-sensor-awi
```

Add the plugin to the `OPTIONSET_PROVIDERS` in `config/settings/local.py`:

```python
OPTIONSET_PROVIDERS = [
    ('awisensors', _('AWI Sensors'), 'sensor_awi.providers.SensorAWIProvider'),
]
```
After restarting RDMO, the `Sensor AWI` should be selectable as a provider option for option sets.
