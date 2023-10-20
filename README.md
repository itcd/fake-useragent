# fake-useragent
A local alternative to fake-useragent https://github.com/fake-useragent/fake-useragent

This program serves as a local alternative to fake-useragent, seamlessly replacing it in your projects without requiring any code modifications. It is fully compatible with the simple usage of fake-useragent, and user agent strings are locally cached and regularly updated from the website
https://www.useragents.me/.

## Compatible Usage
Get a random browser user-agent string
```py
from fake_useragent import UserAgent
ua = UserAgent()
# Get a random browser user-agent string
print(ua.random)
# Or get a user-agent string from a specific browser
print(ua.chrome)
print(ua.edge)
print(ua.firefox)
print(ua.safari)
```

## Additional Usage
Get an HTTP header with a random browser user-agent string
```py
from fake_useragent import header
# Get an HTTP header with a random browser user-agent string
print(header())
```
