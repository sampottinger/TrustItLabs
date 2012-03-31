"""
Models related to collections of website to use with tests

@auth: Sam Pottinger
"""

class AnonymizedSiteSampleModel(db.Model):
    """ Structure that indicates a collection of site but does not trace to a user """

    SAMPLE_NAME_MAX_SIZE = 120

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(SAMPLE_NAME_MAX_SIZE))

    def __init__(self, name):
        """
        Creates a new sample with the given name

        @param name: The name of this new sample (max size of SAMPLE_NAME_MAX_SIZE)
        @type name: String 
        @note: Uniqueness of name not enforced or assumed
        """
        raise NotImplementedError("Not yet implemented")

    def get_name(self):
        """
        Get the name of this site sample

        @return: The non-unique name of this site sample
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")
    
    def update_name(self, new_name):
        """
        Set the name of this sample

        @param new_name: The new name of this sample 
                         (max size of SAMPLE_NAME_MAX_SIZE)
        @type new_name: String
        @note: Unqiueness of new_name not implied or enforced
        """
        raise NotImplementedError("Not yet implemented")

class SiteUsageModel(db.Model):
    """ Structure that indicates a site's inclusion in a sample """
    
    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey("site_model.id"))
    sample_id = db.Column(db.Integer, db.ForeignKey("anonymized_site_sample_model.id"))

    def __init__(self, site_id, sample_id):
        """
        Create a new record of a sties inclusion in a sample

        @param site_id: The unique id of the site in this assocation
        @type site_id: Integer
        @param sample_id: The unqiue id of the sample in this assocation
        @type sample_id: Integer
        """
        raise NotImplementedError("Not yet implemented")

class SiteModel(db.Model):
    """ Structure that records a single site (ex nytimes.com) for use in samples """

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, unique=True)

    def __init__(self, url):
        """
        Create a new record of a site 

        @param url: The url for this site (enforced unqiue)
        @type url: String
        @note: All urls are converted to all lower case before saving
        """
        raise NotImplementedError("Not yet implemented")

    def get_url(self):
        """
        Get the url of this site

        @return: The url of this site
        @rtype: String
        @note: URLs are saved and returned as all lowercase
        """
        raise NotImplementedError("Not yet implemented")

