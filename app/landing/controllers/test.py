"""
Controllers with high level logic for dealing with credibility test routines

@auth: Sam Pottinger
"""

@singleton
class TestDevelopmentRenderController:
    """ Controller that renders the TrustItDeveloperView and subordinates """

    def __init__(self):
        pass

    def render_developer_views(self, session):
        """
        Renders the developer view and all of its subordinates
        
        @param session: Session key value pairs
        @type session: Dict
        @return: The rendered developer views
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

@singleton
class TestSettingsController:
    """ CRUD controller for user submitted test routines """

    def __init__(self):
        pass

    def create_test(self, test_info, session):
        """
        Exposed logic for creating a test

        @param test_info: Structured information regarding a test. Should be parsed
                           YAML or equivalent from client.
        @type test_info: Dict
        @param session: key value pairs with all saved session values
        @type session: dict
        @note: Looking for name and sample id. Data not expected to be cleaned
               beforehand.
        @return: Serialized version of the newly created test
        @rtype: Dict
        """
        raise NotImplementedError("Not yet implemented")

    def read_test(self, test_id, session):
        """
        Exposed logic for reading a test from the database

        @param test_id: The unique numerical id of the test whose information
                         is being requested
        @type test_id: Integer
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: Serialized version of the requested test if access allowed
                 and None otherwise
        @rtype: Dict
        @note: User credentials will be checked by controller
        """
        raise NotImplementedError("Not yet implemented")

    def update_test(self, test_info, session):
        """
        Exposed logic for updating an existing test in the database

        @param test_info: Structured information that should replace current test
                           information. Should be parsed YAML or equivalent from
                           client.
        @type test_info: Dict
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: True if successful or error message otherwise 
        @rtype: Boolean or String
        @note: This controller will check user access control
        """
        raise NotImplementedError("Not yet implemented")

    def delete_test(self, test_id, session):
        """
        Exposed logic for deleting an existing test in the database

        @param test_id: The unique integer id of the test to delete
        @type test_id: Integer
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: True if successful or error message otherwise 
        @rtype: Boolean or String
        @note: This controller will check user access control
        """
        raise NotImplementedError("Not yet implemented")

@singleton
class TestTestingController:
    """ Controller to run small single site tests on a test routine """

    def __init__(self):
        pass

    def test(self, test_id, site_id):
        """
        Tests the given test on the given site

        @param test_id: The unique numerical id of the test to test (TestModel id)
        @type test_id: Integer
        @param site_id: The unique numerical id of the site to test with (SiteModel
                        id)
        @type site_id: Integer
        @return: Serialized TestRunRecordModel instance
        @rtype: Dict
        """
        raise NotImplementedError("Not yet implemented")

@singleton
class TestLogController:
    """ CRUD controller for LogModel and LogEntryModel """

    def create_log(self, log_info, session):
        """
        Exposed logic for creating a log

        @param log_info: Structured information regarding a log. Should be parsed
                           YAML or equivalent from client.
        @type log_info: Dict
        @param session: key value pairs with all saved session values
        @type session: dict
        @note: Looking for name and sample id. Data not expected to be cleaned
               beforehand.
        @return: Serialized version of the newly created log
        @rtype: Dict
        """
        raise NotImplementedError("Not yet implemented")

    def read_log(self, log_id, session):
        """
        Exposed logic for reading a log from the database

        @param log_id: The unique numerical id of the log whose information
                         is being requested
        @type log_id: Integer
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: Serialized version of the requested log if access allowed
                 and None otherwise
        @rtype: Dict
        @note: User credentials will be checked by controller
        """
        raise NotImplementedError("Not yet implemented")

    def update_log(self, log_info, session):
        """
        Exposed logic for updating an existing log in the database

        @param log_info: Structured information that should replace current log
                           information. Should be parsed YAML or equivalent from
                           client.
        @type log_info: Dict
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: True if successful or error message otherwise 
        @rtype: Boolean or String
        @note: This controller will check user access control
        """
        raise NotImplementedError("Not yet implemented")

    def delete_log(self, log_id, session):
        """
        Exposed logic for deleting an existing log in the database

        @param log_id: The unique integer id of the log to delete
        @type log_id: Integer
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: True if successful or error message otherwise 
        @rtype: Boolean or String
        @note: This controller will check user access control
        """
        raise NotImplementedError("Not yet implemented")

    def create_log_entry(self, log_entry_info, session):
        """
        Exposed logic for creating a log_entry

        @param log_entry_info: Structured information regarding a log entry.
                               Should be parsed YAML or equivalent from client.
        @type log_entry_info: Dict
        @param session: key value pairs with all saved session values
        @type session: dict
        @note: Looking for name and sample id. Data not expected to be cleaned
               beforehand.
        @return: Serialized version of the newly created log entry
        @rtype: Dict
        """
        raise NotImplementedError("Not yet implemented")

    def read_log_entry(self, log_entry_id, session):
        """
        Exposed logic for reading a log entry from the database

        @param log_entry_id: The unique numerical id of the log entry whose 
                             information is being requested
        @type log_entry_id: Integer
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: Serialized version of the requested log entry if access allowed
                 and None otherwise
        @rtype: Dict
        @note: User credentials will be checked by controller
        """
        raise NotImplementedError("Not yet implemented")

    def update_log_entry(self, log_entry_info, session):
        """
        Exposed logic for updating an existing log entry in the database

        @param log_entry_info: Structured information that should replace current 
                               log entry information. Should be parsed YAML or 
                               equivalent from client.
        @type log_entry_info: Dict
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: True if successful or error message otherwise 
        @rtype: Boolean or String
        @note: This controller will check user access control
        """
        raise NotImplementedError("Not yet implemented")

    def delete_log_entry(self, log_entry_id, session):
        """
        Exposed logic for deleting an existing log entry in the database

        @param log_entry_id: The unique integer id of the log entry to delete
        @type log_entry_id: Integer
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: True if successful or error message otherwise 
        @rtype: Boolean or String
        @note: This controller will check user access control
        """
        raise NotImplementedError("Not yet implemented")
