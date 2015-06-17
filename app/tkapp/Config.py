import ConfigParser

class Config:
    def __init__(self):
        config = ConfigParser.ConfigParser({'simulateEmulator':'False'},
                                           allow_no_value=True)

        with open('config.cfg') as cfgFile:
            config.readfp(cfgFile)
            self.imgdir = config.get('UserPrefs','imgdir')
            self.datFile = config.get('UserPrefs','datFile')
            self.device = config.get('UserPrefs','device')
            self.simulateEmulator = config.get('UserPrefs','simulateEmulator')

        cfgFile.close()
