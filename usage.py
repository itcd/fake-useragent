from fake_useragent import UserAgent,header

if __name__=='__main__':
    ua=UserAgent()
    # Get a random browser user-agent string
    print(ua.random)
    # Or get user-agent string from a specific browser
    print(ua.chrome)
    print(ua.edge)
    print(ua.firefox)
    print(ua.safari)
    # Get an HTTP header with a random browser user-agent string
    print(header())
