"""
Database models for user authentication and management

@auth: Sam Pottinger
"""

class UserModel:
    """ A record of a OpenID authenticated user """

    def __init__(self, openID, email="", gravatarUrl="", joinDate=None, 
            lastLoggedIn=None):
        """ 
        Creates a new record of a user

        @param openID: The URL of this user's OpenID
        @type openID: String
        @keyword email: This user's email (if one could be parsed). Defaults to
                        an empty string (meaning none provided).
        @type email: String
        @keyword gravatarUrl: The gravatar url for this user if one provided. Default
                              to empty string signifying none provided.
        @type gravatarUrl: String (or None)
        @keyword joinDate: The date when this user is reporting to have joined this
                           app. Defaults to None and will use current datetime (now).
        @type joinDate: datetime
        """
        raise NotImplementedError("Not yet implemented")

    def get_open_id(self):
        """
        Get the openID associated with this user account

        @return: The openID associated with this user record
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

    def get_join_date(self):
        """
        Get the creation date for this account

        @return: The date and time when this record was created
        @rtype: datetime instance
        """
        raise NotImplementedError("Not yet implemented")

    def get_last_logged_in(self):
        """
        Get the date for when this user last logged into the application

        @return: The date and time when this user last logged into this application
        @rtype: datetime instance
        """
        raise NotImplementedError("Not yet implemented")

    def get_email(self):
        """
        Get the email address associated with this user account (if any)

        @return: Email address or empty string if none associated
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

    def get_gravatar_url(self):
        """
        Get the avatar URL reported by this user

        @return: The URL for this user's avatar
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

    def update_last_logged_in_timestamp(self, new_timestamp=None):
        """
        Update the timestamp that this account reports for its last logged in time

        @keyword new_timestamp: The timestamp that this account should report for
                                its owner's last logged in time
        @type new_timestamp: datetime
        """
        raise NotImplementedError("Not yet implemented")

    def update_gravatar_url(self, new_url):
        """
        Update this user's gravatar

        @param new_url: The new url where this user's gravatar can associated with this user account (if any)

        @return: Email address or empty string if none associated
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

    def get_gravatar_url(self):
        """
        Get the avatar URL reported by this user

        @return: The URL for this user's avatar
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

    def update_last_logged_in_timestamp(self, new_timestamp=None):
        """
        Update the timestamp that this account reports for its last logged in time

        @keyword new_timestamp: The timestamp that this account should report for
                                its owner's last logged in time
        @type new_timestamp: datetime
        """
        raise NotImplementedError("Not yet implemented")

    def update_gravatar_url(self, new_url):
        """
        Update this user's gravatar

        @param new_url: The new url where this user's gravatar can be found. An
                        empty string indicates that this user does not have a
                        gravatar.
        @type new_url: String
        """
        raise NotImplementedError("Not yet implemented")


