"""
Database models for the tracking proposals / ideas

@auth: Sam Pottinger
"""

class IdeaAuthorRoleModel:
    """ Assocation between an idea and its author """
    
    id = db.Column(db.Integer, primary_key=True)
    idea_id = db.Column(db.Integer, db.ForeignKey("idea_model.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user_model.id"))

    def __init__(self, idea_id, user_id):
        """
        Create a new association between an idea and user

        @param idea_id: The unique numerical id of the idea that will participate
                        in this association
        @type idea_id: Integer
        @param user_id: The unique numerical id of the user that will also
                        participate in this association
        @type user_id: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_idea_id(self):
        """
        Get the id of the idea that a user is getting permission to

        @return: The unique numerical id of the idea that access is being
                 granted to
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_user_id(self):
        """
        Get the id of the user that is getting permission

        Get the id of the user that is getting permission to the idea that is on the
        other end of this association

        @return: The unique numerical id of the user that access is being
                 given to
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

class IdeaGroup:
    """ Label applied to idea proposals """
    
    MAX_IDEA_GROUP_NAME_SIZE = 120

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_IDEA_GROUP_NAME_SIZE))

    def __init__(self, name):
        """
        Creates a new group for ideas

        @param name: The name of the group to create (of max size
                     MAX_IDEA_GROUP_NAME_SIZE)
        @type name: String
        """
        raise NotImplementedError("Not yet implemented")

    def get_name(self):
        """
        Get the name of this group

        @return: The name of this group
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

class IdeaGroupAssocation:
    """ Assocation between an idea and group """

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey("idea_group_model.id"))
    idea_id = db.Column(db.Integer, db.ForeignKey("idea_model.id"))

    def __init__(self, group_id, idea_id):
        """
        Create a new assocation between a group and an idea

        @param group_id: The unique numerical id of the group to create an
                         association for
        @type group_id: Integer
        @param idea_id: The unique numerical id of the idea to create an
                        association for
        @type idea_id: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_group_id(self):
        """
        Get the id of the group that is participating in this association

        @return: The id of the group that is acting as a label for the idea in
                 this association
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_idea_id(self):
        """
        Get the id of the idea that is participating in this association

        @return: The id of the idea that is being labeled in this assocation
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

class IdeaModel:
    """ Structure containing information about a proposed idea """

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)

    def __init__(self, description):
        """
        Create a new idea with the given description

        @param description: The text description of this idea
        @type description: String
        """
        raise NotImplementedError("Not yet implemented")

    def get_description(self):
        """
        Get the description of this idea

        @return: The text description of this idea
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

class IdeaCommentModel:
    """ A user comment left on a model (does not affect score) """
    
    id = db.Column(db.Integer, primary_key=True)
    idea_id = db.Column(db.Integer, db.ForeignKey("idea_model.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("user_model.id"))
    body = db.Column(db.Text)

    def __init__(self, idea_id, author_id, body):
        """
        Creates a new comment on an idea

        @param idea_id: The unique numerical id of the idea for which this comment
                        is being created
        @type idea_id: String
        @param author_id: The unique numerical id of the user that wrote this
                          comment
        @type author_id: Integer
        @param body: The contents of this comment
        @type body: String
        """
        raise NotImplementedError("Not yet implemented")

    def get_idea_id(self):
        """
        Get the unique numerical id of the idea that this comment is for

        @return: The unique numerical id of this comment's target idea
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_author_id(self):
        """
        Get the unique numerical id of the user that wrote this comment

        @return: The unique numerical id of this comment's author
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_body(self):
        """
        Get the textual body of this comment

        @return: The contents of this comment
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

    def update_body(self, new_body):
        """
        Update the body of this comment

        @param new_body: The new text to use for this comment's body
        @type new_body: String
        """
        raise NotImplementedError("Not yet implemented")

class IdeaVoteModel:
    """ A record of a ser vote either for or against an idea """

    id = db.Column(db.Integer, primary_key=True)
    is_positive = db.Column(db.Boolean)
    idea_id = db.Column(db.Integer, db.ForeignKey("idea_model.id"))
    voter_id = db.Column(db.Integer, db.ForeignKey("user_model.id"))

    def __init__(self, is_positive, voter_id, idea_id):
        """
        Create a new vote for the given idea from the given voter

        @param is_positive: If True, this vote counts for the given idea and,
                            if False, this vote counts against the given idea
        @type is_positive: Boolean
        @param voter_id: The unique id of the voter that created this record (id
                         of UserModel)
        @type voter_id: Integer
        @param idea_id: The unique numerical id of the idea that this vote is for
                        or against (id of IdeaModel)
        """
        raise NotImplementedError("Not yet implemented")
    
    def set_value(self, is_positive):
        """
        Indicates if this is a vote is for or against an idea

        @param is_positive: If True, this vote will count for the idea and False
                            will have this vote count against this idea
        @type is_positive: Boolean
        """
        raise NotImplementedError("Not yet implemented")

    def get_voter_id(self):
        """
        Get the unique numerical id of the voter that cast this vote

        @return: Unique numerical id corresponding to the UserModel whose owner
                 cast this vote
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_idea_id(self):
        """
        Get the unique numerical id of the idea that this vote is for or against

        @return: The id of the IdeaModel that this vote is for / against
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def is_positive(self):
        """
        Determines if this vote is for or against its idea

        @return: True if this is a vote in the positive and False otherwise
        @rtype: Boolean
        """
        raise NotImplementedError("Not yet implemented")
