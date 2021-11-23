import twint

class twint_service:
    
        c = twint.Config()
        c.Username = "azimnoryushan"

        userInfo = twint.run.Lookup(c)

        print(type(userInfo))