"""
Controllers that run test routine discoverability

@auth: Sam Pottinger
"""

from ..util import singleton

@singleton
class TestExchangeRenderController:
    """ High level controller for the rendering of all test exchange views """

    def __init__(self):
        pass

    def render(self, session):
        """ 
        Renders the test exchange view and its subordinates 
        
        @param session: Session key value pairs
        @type session: Dict
        @return: The rendered test suite views
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

@singleton
class TestExplorationController:
    """ Controller to handle complex navigation operations during test discovery """

    def __init__(self):
        pass

    def search(self, search_term, session):
        """
        Looks for tests that fit the given search term

        @param search_term: The user provided query
        @type search_term: String
        @param session: Session key value pairs
        @type session: Dict
        @return: Seralized of dict (name -> id)
        @rtype: List of dict
        """
        raise NotImplementedError("Not yet implemented")

@singleton
class TestExchangeDetailsController:
    """ Controller to lookup information about tests during test discovery """

    def __init__(self):
        pass

    def get_test_info(self, test_id, session):
        """
        Get information about a test for the purposes of test discovery

        @param test_id: The unique numerical id of the test for which additional
                        information is being requested
        @type test_id: Integer
        @param session: Session key value pairs
        @type session: Dict
        @return: Serialized TestModel (removing sensitive data)
        @rtype: Dict
        """
        raise NotImplementedError("Not yet implemented")


