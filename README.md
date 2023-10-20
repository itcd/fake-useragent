# fake-useragent
A local alternative to fake-useragent https://github.com/fake-useragent/fake-useragent

This program is a local alternative to fake-useragent. It is compatible with the simple usage of fake-useragent. User agent strings are stored locally.

## Compatible Usage
Get a random browser user-agent string or a user-agent string from a specific browser
```py
from fake_useragent import UserAgent
ua=UserAgent()
print(ua.random,ua.chrome,ua.firefox,sep='\n')
```

## Additional Usage
Get an HTTP header with a random browser user-agent string
```py
from fake_useragent import header
print(header())
```
