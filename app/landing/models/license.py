"""
Structures for saving information about licenses

Models for saving information related to licenses 
used for sharing user contributions

@auth: Sam Pottinger
"""

class LicenseModel(db.Model):
    """ Structure with information about a license available for a test """
    
    LICENSE_NAME_MAX_SIZE = 120

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(LICENSE_NAME_MAX_SIZE))
    url = db.Column(db.Text)

    def __init__(self, name, url):
        """
        Create a new license with the given name and url

        @param name: The name of this license (ex GNU GPL v2)
        @type name: String
        @param url: The url where more information about this license can be found
        @type url: String
        """
        raise NotImplementedError("Not yet implemented")

    def get_name(self):
        """
        Get the name of this license

        @return: The common name of this license (ex MIT OS License)
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

    def get_url(self):
        """
        Get the url where more information about this license can be found

        @return: The url where additional information about this license
                 can be found (often its actual full text)
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")
