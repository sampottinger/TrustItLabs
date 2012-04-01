"""
Application logic for controlling collections of tests as test suites

@auth: Sam Pottinger
"""

from ..util import singleton

@singleton
class TestSuiteRenderContoller:
    """ Logic for generating the AJAX capable test suite pages """

    def __init__(self):
        pass

    def render_suite_views(self, session):
        """
        Renders the test suite view and all of its subordinates
        
        @param session: Session key value pairs
        @type session: Dict
        @return: The rendered test suite views
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

@singleton
class TestSuiteConfigurationController:
    """ CRUD controller for test suites """

    def __init__(self):
        pass

    def create_suite(self, suite_info, session):
        """
        Exposed logic for creating a test suite

        @param suite_info: Structured information regarding a suite. Should be parsed
                           YAML or equivalent from client.
        @type suite_info: Dict
        @param session: key value pairs with all saved session values
        @type session: dict
        @note: Looking for name and sample id. Data not expected to be cleaned
               beforehand.
        @return: Serialized version of the newly created suite
        @rtype: Dict
        """
        raise NotImplementedError("Not yet implemented")

    def read_suite(self, suite_id, session):
        """
        Exposed logic for reading a suite from the database

        @param suite_id: The unique numerical id of the suite whose information
                         is being requested
        @type suite_id: Integer
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: Serialized version of the requested suite if access allowed
                 and None otherwise
        @rtype: Dict
        @note: User credentials will be checked by controller
        """
        raise NotImplementedError("Not yet implemented")

    def update_suite(self, suite_info, session):
        """
        Exposed logic for updating an existing suite in the database

        @param suite_info: Structured information that should replace current suite
                           information. Should be parsed YAML or equivalent from
                           client.
        @type suite_info: Dict
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: True if successful or error message otherwise 
        @rtype: Boolean or String
        @note: This controller will check user access control
        """
        raise NotImplementedError("Not yet implemented")

    def delete_suite(self, suite_id, session):
        """
        Exposed logic for deleting an existing suite in the database

        @param suite_id: The unique integer id of the suite to delete
        @type suite_id: Integer
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: True if successful or error message otherwise 
        @rtype: Boolean or String
        @note: This controller will check user access control
        """
        raise NotImplementedError("Not yet implemented")

@singleton
class TestSuiteSampleController:
    """ Controller that provides CRUD access to a sample """

    def __init__(self):
        pass

    def create_sample(self, sample_info, session):
        """
        Exposed logic for creating a site sample

        @param suite_info: Structured information regarding a sample. Should be parsed
                           YAML or equivalent from client.
        @type suite_info: Dict
        @param session: key value pairs with all saved session values
        @type session: dict
        @note: Looking for name and sample id. Data not expected to be cleaned
               beforehand.
        @return: Serialized version of the newly created site sample
        @rtype: Dict
        """
        raise NotImplementedError("Not yet implemented")

    def read_sample(self, sample_id, session):
        """
        Exposed logic for reading a sample from the database

        @param suite_id: The unique numerical id of the sample whose information
                         is being requested
        @type suite_id: Integer
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: Serialized version of the requested sample if access allowed
                 and None otherwise
        @rtype: Dict
        @note: User credentials will be checked by controller
        """
        raise NotImplementedError("Not yet implemented")

    def update_sample(self, sample_info, session):
        """
        Exposed logic for updating an existing sample in the database

        @param suite_info: Structured information that should replace current sample
                           information. Should be parsed YAML or equivalent from
                           client.
        @type suite_info: Dict
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: True if successful or error message otherwise 
        @rtype: Boolean or String
        @note: This controller will check user access control
        """
        raise NotImplementedError("Not yet implemented")

    def delete_sample(self, sample_id, session):
        """
        Exposed logic for deleting an existing sample in the database

        @param sample_id: The unique integer id of the sample to delete
        @type sample_id: Integer
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: True if successful or error message otherwise 
        @rtype: Boolean or String
        @note: This controller will check user access control
        """
        raise NotImplementedError("Not yet implemented")

    def set_test_sample(self, test_id, sample_id):
        """
        Sets the current sample for a test suite

        @param test_id: Unique integer id of the sample to use for the given test
        @type test_id: Integer
        @param sample_id: Unique integer id of the sample to assign the given
                          test
        @type sample_id: Integer
        """
        raise NotImplementedError("Not yet implemented")

