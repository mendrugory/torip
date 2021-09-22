# torip

![tests](https://github.com/mendrugory/torip/actions/workflows/unittest.yaml/badge.svg)

Python library for Tornado web framework to locate IPs or server names.

Torip will provide you information like country, city, zip code or the url of google maps.

Torip has been developed and tested using Python3.4

## Installation

```bash
$ pip install torip
```

## Available APIs

Torip supports the following APIs:

### [ip-api] [IPAPI]
It is also the default API.

```python
from torip.locator import Locator
locator = Locator(api_name='ip-api')
```
or
```python
from torip.locator import Locator
locator = Locator()  # default API
```

### [freegeoip.net] [FGI]
```python
from torip.locator import Locator
locator = Locator(api_name='freegeoip')
```

## Example

```python
import tornado
from torip.locator import Locator
ip = ''  # IP or server name
@tornado.gen.coroutine
def function():
    try:
        locator = Locator()
        result = yield locator.locate(ip)
        print(result)
    except Exception as e:
        print(str(e))
    finally:
        ioloop.stop()
ioloop = tornado.ioloop.IOLoop.instance()
ioloop.add_callback(function)
ioloop.start()
```

[FGI]:<https://freegeoip.net>
[IPAPI]: <http://ip-api.com/>