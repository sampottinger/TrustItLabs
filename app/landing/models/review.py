"""
Models related to user submitted reviews of user submitted test routines

@auth: Sam Pottinger
"""

class ReviewModel:
    """ Structure for a generic user submitted review """
    
    MIN_RAITING = 0
    MAX_RAITING = 10

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user_model.id"))
    comment = db.Column(db.Text)
    raiting = db.Column(db.Integer)

    def __init__(self, author_id, comment, raiting):
        """
        Creates a new test review

        Creates a new test review for the given test with the given description and
        value

        @param author_id: The unique numerical id of the user who authored this review
        @type author_id: Integer
        @param comment: The free text description to attach to this test
        @type comment: String
        @param raiting: The numerical raiting to attach to this review, an
                        indication of what this review's author thought of the
                        test in question
        @type raiting: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_author_id(self):
        """
        Get the id of the user that wrote this review

        @return: The id of the user (UserModel) who wrote this review
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_comment(self):
        """
        Get the comment that the author of this review left regarding its test

        @return: The comment attached to this review
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

    def get_raiting(self):
        """
        Get the numerical raiting attached to this review

        @return: The numerical raiting left in this review by its author for the
                 test in question. Will be >= MIN_RAITING and <= MAX_RAITING
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

class TestReviewModel:
    """
    Record of a review regarding a user submitted test routine
    
    An assocation between a generic user review model instance and 
    a user submitted test
    """

    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey("review_model.id"))
    test_id = db.Column(db.Integer, db.ForeignKey("test_model.id"))

    def __init__(self, review_id, test_id):
        """
        Creates an assocation between a generic review and a test

        @param review_id: The id of the review to associate with a test
        @type review_id: Integer
        @param test_id: The id of the test to associate the given review with
        @type test_id: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_review_id(self):
        """
        Get the unique numerical id of the review this association targets

        @return: The unique numerical id of the review that is participating in this
                 record
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_test_id(self):
        """
        Get the unique numerical id of the test that this assocation targets
        
        @return: The unique numerical id of the test that is participating in this
                 record
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

class TestSuiteReviewModel:
    """
    Record of a review regarding a test suite

    An assocation between a generic user review model instance and a
    test suite model
    """

    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey("review_model.id"))
    test_id = db.Column(db.Integer, db.ForeignKey("test_model.id"))

    def __init__(self, review_id, suite_id):
        """
        Creates a new review of a test suite

        @param review_id: The unique numerical id of the generic user submitted 
                          review to attach to a test suite
        @type review_id: Integer
        @param suite_id: The unique numerical id of the suite that this 
                         review is being attached to
        @type suite_id: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_review_id(self):
        """
        Determines the unique numerical id of the review that is in this assocation

        @return: The unique numerical id of the review that is being attached to
                 a test suite through this assocation
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_suite_id(self):
        """
        Determine the unique numerical id of the suite in this assocation

        @return: The unqiue numerical id of the suite that this review is being
                 attached to
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

class SampleReviewModel:
    """
    Record of a review regarding a SiteSampleModel

    An assocation between a generic user review model instance and a
    site sample model
    """

    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey("review_model.id"))
    sample_id = db.Column(db.Integer, db.ForeignKey("site_sample_model.id"))

    def __init__(self, review_id, test_id):
        """
        Create a new sample review assocation

        @param review_id: The unique numerical id of the review that is being
                          associated with a site sample
        @type review_id: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_review_id(self):
        """
        Determines the unique numerical id of the review that is in this assocation

        @return: The unique numerical id of the review that is being attached to
                 a site sample through this assocation
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")

    def get_sample_id(self):
        """
        Determines the unique numerical id of the site sample in this assocation

        @return: The unique numerical id of the site sample that is having a
                 review attached to it
        @rtype: Integer
        """
        raise NotImplementedError("Not yet implemented")
