# torip

![tests](https://github.com/mendrugory/torip/actions/workflows/unittest.yaml/badge.svg)

Python library for Tornado web framework to locate IPs or server names.

Torip will provide you information like country, city, zip code or the url of google maps.

## Installation

```bash
$ pip install torip
```

## Available APIs

Torip supports the following APIs:

### [abstractapi] [ABAPI]
It is also the default API.

```python
from torip.locator import Locator
locator = Locator(api_name='abstractapi', api_token=<Your API TOKEN>)
```

or

```python
from torip.locator import Locator
locator = Locator(api_token=<Your API TOKEN>)  # default API
```

### [ip-api] [IPAPI]

```python
from torip.locator import Locator
locator = Locator(api_name='ip-api')
```

## Example

```python
import tornado
from torip.locator import Locator
ip = '<IP ADDRESS>'
@tornado.gen.coroutine
def function():
    try:
        locator = Locator(api_token='<YOUR API TOKEN>')
        result = yield locator.locate(ip)
        print(result)
    except Exception as e:
        print(str(e))
    finally:
        ioloop.stop()
ioloop = tornado.ioloop.IOloop.instance()
ioloop.add_callback(function)
ioloop.start()
```

[ABAPI]:<https://www.abstractapi.com/ip-geolocation-api>
[IPAPI]: <http://ip-api.com/>

## Docs

* [github](https://github.com/mendrugory/torip)
* [pypi](https://pypi.org/project/torip/)
* [readthedocs](https://torip.readthedocs.io)
