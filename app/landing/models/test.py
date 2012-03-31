"""
Models related to user submitted tests

@auth: Sam Pottinger
"""

class TestModel(db.Model):
    """ Model containing information regarding a user submitted test routine """
    
    TEST_KEY_SIZE = 256
    GET = 1
    POST = 3

    id = db.Column(db.Integer, primary_key=True)
    license_id = db.Column(db.Integer, db.ForeignKey("license_model.id"))
    controller_url = db.Column(db.Text)
    key = db.Column(db.String(TEST_KEY_SIZE))
    source_loc = db.Column(db.Text)
    method = db.Column(db.Integer)
    interpret_results = db.Column(db.Boolean)
    golf_scoring = db.Column(db.Boolean)
    num_users = db.Column(db.Integer)
    num_usages = db.Column(db.Integer)

    def __init__(self, license_id, controller_url, key, source_loc, 
            method, interpret_results, golf_scoring, num_users=0, num_usages=0):
        """
        Create a new record of a user submitted test routine

        @param license_id: The unique numerical id of the license to use for this
                           user submitted test (i.e. the license choosen by user)
        @type license_id: Integer
        @param controller_url: The url at which this test responds to requests to
                               run against a source
        @type controller_url: String
        @param key: The unique key to use when communicating this test to verify
                    valid test run request. Of size TEST_KEY_SIZE
        @type key: String
        @param source_loc: The URL at which the source for this test can be found
                           or where users can find more information about it
        @type source_loc: String
        @param method: The method to use when communicating with this web app. Should
                       be of constant GET or POST
        @type method: Integer
        @param interpret_results: Flag to indicate if result values should be
                                  statistically interpreted / normalized by the 
                                  application or the user-created test 
                                  (True for app responsibility and False for 
                                   test responsibilty)
        @type interpret_results: Boolean
        @param golf_scoring: If True, lower scores indicate better performance.
                             If False, higher scores indicate better performance.
        @type golf_scoring: Boolean
        @keyword num_users: The number of users that this test has (number of users
                          with test suites that have this test). Default to 0.
        @type num_users: Integer
        @keyword num_usages: The number of usages this test has (number of test suites
                           that have this test). Default to 0.
        @type num_usages: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_license_id(self):
        """
        Get the unique id of the license that this test is released under

        @return: The unique id of the LicenseModel instance that describes the
                 license that this test has been released under
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def update_license(self, new_license_id):
        """
        Set the license that this test is reportedly released under

        @param new_license_id: The id of the LicenseModel instance that describes
                               the license that this test is released under
        @type new_license_id: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_controller_url(self):
        """
        Get the url at which this test will respond to requests

        @return: The URL that this test services
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

    def get_controller_method(self):
        """
        Get the method taht this test requires requests to come in

        @return: GET or POST
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def update_controller(self, new_url, new_method):
        """
        Set the url reported by this test at which it responds to requests

        @param new_url: The new url at which this test will respond to requests
        @type new_url: String
        @param new_method: GET or POST
        @type new_method: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_key(self):
        """
        Get the key that this application needs to use to access this test

        @return: The key that this test requires before it can be used
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

    def update_key(self, new_key):
        """
        Set the key that this application needs to use to access this test

        @param new_key: New key of size TEST_KEY_SIZE 
        @type new_key: String
        """
        raise NotImplementedError("Not yet implemented")
    
    def get_source_loc(self):
        """
        Get the url at which additional information about this test is available

        @return: the url at which this test's code is available for more information
                 about it is available
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

    def update_source_loc(self, new_loc):
        """
        Set the url at which additional information about this test is available

        @param new_loc: The new URL at which users can find the source of this
                        test and / or more information about it
        @type new_loc: String
        """
        raise NotImplementedError("Not yet implemented")

    def should_app_interpret_results(self):
        """
        Determines if this test' developers interpret their own raw values

        Determines if this test statistically interprets and normalizes its own
        values or not. If this is the application's responsibility (as opposed to
        the test's), the application will normalize results to determine how
        raw values correspond to site performance on those tests

        @return: True if the application is interpreting raw values reported
                 by the test and False if the application is treating the values
                 reported by the test as already interpreted
        @rtype: Boolean
        """
        raise NotImplementedError("Not yet implemented")

    def test_uses_golf_scoring(self):
        """
        Determines if lower raw test scores indicate better performance or not

        @return: True if lower scores indicate better test performance and False
                 if higher scores indicate better test performance (True if
                 scores and performance are directly correlated and False if
                 inversely proportional
        @rtype: Boolean
        """
        raise NotImplementedError("Not yet implemented")

    def increment_usage(self):
        """ Increase this test's usage count by 1 """
        raise NotImplementedError("Not yet implemented")

    def decrement_usage(self):
        """ Decrease this test's usage count by 1 """
        raise NotImplementedError("Not yet implemented")

    def increase_user_count(self, amount):
        """
        Increase this test's user count by amount

        @param amount: The amount by which to increase this test's user count
        @type amount: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def decrease_user_count(self, amount):
        """
        Decrease this test's user count by amount

        @param amount: The amount by which to decrease this test's user count
        @type amount: Integer
        """
        raise NotImplementedError("Not yet implemented")

class CollaboratorRoleModel(db.Model):
    """ Structure indicating that a user is a collaborator on a test """
    
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey("test_model.id"))
    review_id = db.Column(db.Integer, db.ForeignKey("review_model.id"))

    def __init__(self, test_id, user_id):
        """
        Create a new indication of a collaboration role for a user

        @param test_id: The unqiue id of the test (from model) that is part of this
                        role
        @type test_id: Integer
        @param user_id: The unique id of the user (from model) that is participating
                        in this association
        @type user_id: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_test_id(self):
        """
        Get the id of the test that this collaborator role is for

        @return: The id of the test that this collaborator has access to
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_user_id(self):
        """
        Get the id of the user that is participating in this collaboration

        @return: The id of the collaborator participating in this role
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

class TestRunRecordModel(db.Model):
    """ Structure indicating that a test was run """

    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey("test_model.id"))
    successful = db.Column(db.Boolean)
    timestamp = db.Column(db.DateTime)

    def __init__(self, test_id, successful, run_time, source_id, timestamp):
        """
        Create a record of a test having run on a given source

        @param test_id: The unique numerical id of the test that this record is for
        @type test_id: Integer
        @param successful: Flag indicating if this test run finished without error
        @type successful: Boolean
        @param source_id: The unique numerical id of the source that this test was
                          run on
        @type source_id: Integer
        @param timestamp: The date and time at which this run occured
        @type timestamp: Datetime
        """
        raise NotImplementedError("Not yet implemented")

    def get_test_id(self):
        """
        Get the unique numerical id of the test this record is for

        @return: The numerical id of the test that this record indicates was run
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def was_successful(self):
        """
        Determine if the run that this record is for was successful

        @return: True if successful (no error) and False otherwise
        @rtype: Boolean
        """
        raise NotImplementedError("Not yet implemented")

    def get_source_id(self):
        """
        Get the unique numerical id of the source on which this test was run

        @return: Id for an AnonymizedSiteSampleModel
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_timestamp(self):
        """
        Get the date and time when this run happenend

        @return: Timestamp for when this test was run
        @rtype: DateTime instance
        """
        raise NotImplementedError("Not yet implemented")

class TestResult:
    """ Record of a result of test with scores reported by test """

    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey("site_model.id"))
    test_id = db.Column(db.Integer, db.ForeignKey("test_model.id"))

    def __init__(self, site_id, test_id, raw_score):
        """
        Creates a new record of the result of a test run on a site

        @param site_id: The unique id of the site that the test ran on
        @type site_id: Integer
        @param test_id: The unique id of the test that ran
        @type test_id: Integer
        @param raw_score: The raw score reported by the test itself
        @type raw_score: Float
        """
        raise NotImplementedError("Not yet implemented")

    def get_site_id(self):
        """
        Get the site on which this test was run and this result is for

        @return: The unique numerical id of the site on which this test was run
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_test_id(self):
        """
        Get the id of the test that produced this result

        @return: The unique id of the test that produced this record
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

