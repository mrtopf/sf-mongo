from starflyer import Module
import pymongo

__all__ = ['MongoDB', 'mongodb']

class MongoModule(Module):
    """a simple mongodb module for starflyer to provide a database connection
    """

    name = "mongo"

    defaults = {
        'mongodb_name'      : "",                # use dummy mailer?
        'mongodb_host'      : "localhost",       # host to connect to
        'mongodb_port'      : 25,                # port to use
        'debug'             : False,
    }

    config_types = {
        'debug' : bool,
        'port' : int,
    }

    def finalize(self):
        """finalize the setup"""

        # push the mongodb instance into the app and the module
        self.db = self.app.mongodb = pymongo.Connection(
            self.config.mongodb_host,
            self.config.mongodb_port
        )[self.config.mongodb_name]

        # TODO: give it some mongogogo classes to instantiate with that connection?
        # or give it some way inside the class to predefine the collection to be used?

mongodb = MongoDB(__name__)


