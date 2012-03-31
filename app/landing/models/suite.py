"""
Models that describe collections of tests

@author: Sam Pottinger
"""

class TestUsageModel:
    """ Record of a test being used in a test suite (collection) """

    id = db.Column(db.Integer, primary_key=True)
    suite_id = db.Column(db.Integer, db.ForeignKey("test_suite_model.id"))
    test_id = db.Column(db.Integer, db.ForeignKey("test_model.id"))
    weight = db.Column(db.Float)

    def __init__(self, suite_id, test_id, weight):
        """
        Creates a new record of a test's inclusion in a suite

        @param suite_id: The unique numerical id of the suite for which a test is
                         being included
        @type suite_id: Integer
        @param test_id: The unique numerical id of the test that is being included
                        in the given test
        @type test_id: Integer
        @param weight: The weight (<= 0 and >= 1) that this test plays in the
                       suite's calculation of a overall score. This is a percentage
                       in a weighted average.
        """
        raise NotImplementedError("Not yet implemented")

    def get_test_id(self):
        """
        Determine the id of the test that is in this relationship

        @return: The unique numerical id of the test in this association
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_suite_id(self):
        """
        Determine the id of the suite that is in this relationship

        @return: The unqiue numerical if of the suite in this association
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_weight_id(self):
        """
        Determine the percentage that this test in this suite's overall score calc

        @return: The weight (<= 0 and >= 1) that this test in plays in this suites
                 calculation of an overall score which is a weighted average
        @rtype: Float
        """
        raise NotImplementedError("Not yet implemented")

class TestSuiteModel:
    """ A record of a test suite """

    MAX_SUITE_NAME_SIZE = 120

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_SUITE_NAME_SIZE))
    sample_id = db.Column(db.Integer, db.ForeignKey("site_sample_model.id"))

    def __init__(self, name, sample_id):
        """ 
        Create a new named record of a test collection

        @param name: The name of this collection (max size of MAX_SUITE_NAME_SIZE)
        @type name: String
        @param sample_id: The unique numerical id of the sample that this suite
                          is currently targeting (SiteSampleModel)
        @type sample_id: Integer
        @note: The uniqueness of name is not enforced
        """
        raise NotImplementedError("Not yet implemented")

    def get_name(self, name):
        """
        Get the name of this suite 

        @return: The non-unique name of this testing suite
        @rtype: String
        @note: Name may or may not be unqiue
        """
        raise NotImplementedError("Not yet implemented")

    def update_name(self, new_name):
        """
        Update the name that this suite is using

        @param new_name: The new name this suite will use (max size of
                         MAX_SUITE_NAME_SIZE)
        @type new_name: String
        """
        raise NotImplementedError("Not yet implemented")

    def get_current_sample_id(self):
        """
        Get the unqiue numerical id of the sample that this suite is targeting

        Get the unique numerical id of the SiteSampleModel that this suite will
        run on

        @return: Unique numerical id of this suite's current target sample
        @rtype: Integer
        @note: Does not check user access permissions
        """
        raise NotImplementedError("Not yet implemented")

    def set_current_sample_id(self):
        """
        Sets the unqiue numerical id of the sample that this suite is targeting

        Sets the unique numerical id of the SiteSampleModel that this suite will
        run on

        @param new_id: The numerical id of the sample that this suite should now
                       run on when it is asked to run
        @type new_id: Integer
        """
        raise NotImplementedError("Not yet implemented")

class SuiteAuthorRoleModel:
    """
    A record of a user's collaborator role for a suite

    Record of a user's ability to edit and experiment with a test suite
    """

    id = db.Column(db.Integer, primary_key=True)
    suite_id = db.Column(db.Integer, db.ForeignKey("test_suite_model.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user_model.id"))

    def __init__(self, user_id, suite_id):
        """
        Create a new record of a user's ability to collaborate on a suite

        @param user_id: The unique numerical id of the user being given 
                        permission to work on a suite
        @type user_id: Integer
        @param suite_id: The unique numerical id of the suite to which
                         the user is being given access
        @type suite_id: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_user_id(self):
        """
        Get the unique numerical id of the user in this assocation

        @return: The unique numerical id of the user in this permission record
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_suite_id(self):
        """
        Get the unique numerical id of the suite that this assocation targets

        @return: The unique numerical id of the suite in this permission record
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")


@singleton
class TestSuiteServicer:
    """ Logic for management of tests, their reviews, and their authors """

    def __init__(self):
        pass

    def get_test_reviews(self, suite_id):
        """
        Get all of the reviews written for the tests of a given test suite

        @param suite_id: The unique numerical id of the suite whose reviews are
                        being requested
        @type suite_id: Integer
        @return: All of the reviews written for the tests of a given test suite
        @rtype: Collection of Integers (TestReviewModel ids)
        """
        raise NotImplementedError("Not yet implemented")

    def get_tests(self, suite_id):
        """
        Get all of the tests in the given test suite

        @param suite_id: The unique numerical id of the test suite whose tests are
                         being requested
        @type suite_id: Integer
        @return: All of the tests in the given test suite
        @rtype: Collection of Integers (TestModel ids)
        """
        raise NotImplementedError("Not yet implemented")

    def get_authors(self, suite_id):
        """
        Get all of the authors who can edit or experiment with the given suite

        @param suite_id: The unique numerical id of the test suite whose authors
                         are being requested
        @return: All of the users who are authors to the given suite
        @rtype: Collection of Integers (TestModel ids)
        """
        raise NotImplementedError("Not yet implemented")

