"""
Controllers for proposals, fame walls, and other community elements

@auth: Sam Pottinger
"""

from ..util import singleton

@singleton
class ProposalNavigationController:
    """ Controller to enable navigation of user submitted ideas """

    def __init__(self):
        pass

    def render_frame(self, session):
        """ 
        Renders the idea browsing view and its subordinates 
        
        @param session: Session key value pairs
        @type session: Dict
        @return: The rendered idea browsing views
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

    def get_idea_list(self, session, selection_criteria, offset, num_ideas):
        """
        Fetches a list of ideas

        @param session: Session key value pairs
        @type session: Dict
        @param selection_criteria: Constant indicating how ideas should be sorted
        @type selection_criteria: Integer
        @param offset: How many ideas to offset the list by (how far in the list
                       for pagination)
        @param num_ideas: How many ideas to retrieve and return
        @type num_ideas: Integer
        @return: Serialized list of ideas
        @rtype: List of Dict
        """
        raise NotImplementedError("Not yet implemented")

@singleton
class IdeaDetailsController:
    """ Controller that retrieves information about a proposal """

    def get_idea(self, idea_id, session):
        """
        Get idea details

        @param idea_id: The unique numerical id of the proposal for which
                            additional information is being requested
        @type idea_id: Integer
        @param session: Session key value pairs
        @type session: Dict
        @return: Serailized IdeaModel
        @rtype: Dict
        """
        raise NotImplementedError("Not yet implemented")

    def get_idea_comments(self, idea_id, session):
        """
        Get the comments for a idea

        @param idea_id: The unique numerical id of the idea whoose
                            comments are being requested
        @type idea_id: Integer
        @param session: Session key value pairs
        @type session: Dict
        @return: Serailized IdeaCommentModel instances
        @rtype: List of Dict
        """
        raise NotImplementedError("Not yet implemented")

@singleton
class FameWallController:
    """ Controller that supports the fame wall display and interactions with it """

    def __init__(self):
        pass

    def render_frame(self, session):
        """
        Renders AJAX components to display rankings

        @param session: Session key value pairs
        @type session: Dict
        @return: The rendered fame wall
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

    def get_rankings(self, offset, num_positions, session):
        """
        Get developer leaderboards

        @param offset: The offset into the rankings list to start retrieving entries
        @type offset: Integer
        @param num_positions: The number of rankings to return
        @type num_positions: Integer
        @param session: Session key value pairs
        @type session: Dict
        """
        raise NotImplementedError("Not yet implemented")

@singleton
class IdeaManipulationController:
    """ CRUD controller for proposal """

    def create_idea(self, idea_info, session):
        """
        Exposed logic for creating a idea

        @param idea_info: Structured information regarding a idea. 
                              Should be parsed YAML or equivalent from client.
        @type idea_info: Dict
        @param session: key value pairs with all saved session values
        @type session: dict
        @note: Looking for name and sample id. Data not expected to be cleaned
               beforehand.
        @return: Serialized version of the newly created idea
        @rtype: Dict
        """
        raise NotImplementedError("Not yet implemented")

    def read_idea(self, idea_id, session):
        """
        Exposed logic for reading a idea from the database

        @param idea_id: The unique numerical id of the idea whose information
                         is being requested
        @type idea_id: Integer
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: Serialized version of the requested idea if access allowed
                 and None otherwise
        @rtype: Dict
        @note: User credentials will be checked by controller
        """
        raise NotImplementedError("Not yet implemented")

    def update_idea(self, idea_info, session):
        """
        Exposed logic for updating an existing idea in the database

        @param idea_info: Structured information that should replace current 
                              idea information. Should be parsed YAML or 
                              equivalent from client.
        @type idea_info: Dict
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: True if successful or error message otherwise 
        @rtype: Boolean or String
        @note: This controller will check user access control
        """
        raise NotImplementedError("Not yet implemented")

    def delete_idea(self, idea_id, session):
        """
        Exposed logic for deleting an existing idea in the database

        @param idea_id: The unique integer id of the idea to delete
        @type idea_id: Integer
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: True if successful or error message otherwise 
        @rtype: Boolean or String
        @note: This controller will check user access control
        """
        raise NotImplementedError("Not yet implemented")

@singleton
class CommentManipulationController:
    """ CRUD controller for comments on ideas """

    def create_comment(self, comment_info, session):
        """
        Exposed logic for creating a comment

        @param comment_info: Structured information regarding a comment. 
                              Should be parsed YAML or equivalent from client.
        @type comment_info: Dict
        @param session: key value pairs with all saved session values
        @type session: dict
        @note: Looking for name and sample id. Data not expected to be cleaned
               beforehand.
        @return: Serialized version of the newly created comment
        @rtype: Dict
        """
        raise NotImplementedError("Not yet implemented")

    def read_comment(self, comment_id, session):
        """
        Exposed logic for reading a comment from the database

        @param comment_id: The unique numerical id of the comment whose information
                         is being requested
        @type comment_id: Integer
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: Serialized version of the requested comment if access allowed
                 and None otherwise
        @rtype: Dict
        @note: User credentials will be checked by controller
        """
        raise NotImplementedError("Not yet implemented")

    def update_comment(self, comment_info, session):
        """
        Exposed logic for updating an existing comment in the database

        @param comment_info: Structured information that should replace current 
                              comment information. Should be parsed YAML or 
                              equivalent from client.
        @type comment_info: Dict
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: True if successful or error message otherwise 
        @rtype: Boolean or String
        @note: This controller will check user access control
        """
        raise NotImplementedError("Not yet implemented")

    def delete_comment(self, comment_id, session):
        """
        Exposed logic for deleting an existing comment in the database

        @param comment_id: The unique integer id of the comment to delete
        @type comment_id: Integer
        @param session: key value pairs with all saved session values
        @type session: dict
        @return: True if successful or error message otherwise 
        @rtype: Boolean or String
        @note: This controller will check user access control
        """
        raise NotImplementedError("Not yet implemented")

@singleton
class VotingController:
    """ Controller that facilitates voting on proposals """

    def __init__(self):
        pass

    def add_vote(self, idea_id, is_positive, session):
        """
        Adds a new vote for / against an idea

        @param idea_id: The unique numerical id of the idea to register a vote for
                        or against
        @type idea_id: Integer
        @param is_positive: Indicates if this is a vote for or against an idea.
                            True indicates for and False against.
        @type is_positive: Boolean
        @param session: Session key value pairs
        @type session: Dict
        @return: True if successful and False otherwise
        @rtype: Boolean
        @note: This controller will ensure that a user only votes once for an idea
        """
        raise NotImplementedError("Not yet implemented")

