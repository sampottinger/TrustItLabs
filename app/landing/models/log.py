"""
Models related to maintaining a log regarding test performance

@auth: Sam Pottinger
"""

from ..support.util import Singleton

log_entry_associations = db.Table("log_entry_associations",
        db.Column("entry_id", db.Integer, db.ForeignKey("log_entry_model.id")),
        db.Column("log_id", db.Integer, db.ForeignKey("log_model.id"))
        )

class LogEntryModel(db.Model):
    """
    Simple timestamped record regarding an abnormal test performance

    A simple model with information about a timestamped event regarding a test
    and an error regarding it or something related to its runtime
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    logs = db.Relationship("LogModel", secondary=tags,
            backref=db.backref("log_entry_models", lazy="dynamic"))

    def __init__(self, timestamp, message):
        """
        Creates a new log entry with the given message and timestamp

        @param timestamp: The timestamp to use for this entry
        @type timestamp: DateTime instance
        @param message: The text to describe this entry
        @type message: String
        """
        raise NotImplementedError("Not yet implemented")

    def get_timestamp(self):
        """
        Gets the timestamp given to this log entry

        @return: This entry's corresponding timestamp
        @rtype: DateTime
        """
        raise NotImplementedError("Not yet implemented")

    def get_message(self):
        """
        Gets the text description of this log entry

        @return: This entry's corresponding message
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")

class LogModel(db.Model):
    """
    Collection of timestamped records with errors and messages regarding a test
    """

    LOG_NAME_MAX_SIZE = 120

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(LOG_NAME_MAX_SIZE))
    test_id = db.Column(db.Integer, db.ForeignKey("test_model.id"))

    def __init__(self, test_id, name):
        """
        Creates a new log for the given test for a category of messages

        @param test_id: The unique numerical id of the test for which this log is
                        being created
        @type test_id: Integer
        @param name: The name to use for this log
        @type name: String
        """
        raise NotImplementedError("Not yet implemented")
 
    def get_name(self):
        """
        Get the name of this log

        @return: The name of this log
        @rtype: String
        """
        raise NotImplementedError("Not yet implemented")
        
    def get_test_id(self):
        """
        Get the test this log is for

        @return: The unique id of the test this is a log for
        @rtype: int
        """
        raise NotImplementedError("Not yet implemented")

@Singleton
class LogServicer:
    """
    Singleton entry factory and support logic for log related tasks
    """

    def __init__(self):
        pass

    def get_entries_by_log_id(self, log_id, start_date=None, end_date=None):
        """
        Gets all of the log entries for the log with the given id
        
        @param log_id: The id of the log for which entries are being requested
        @type log_id: int
        @keyword start_date: The earliest timestamp at which to look for log entries,
                             inclusive
        @param start_date: Datetime
        @keyword end_date: The latest timestamp at which to look for log entries,
                           inclusive
        @return: Iterable over the entries found
        @rtype: Iterable over LogEntryModel
        """
        raise NotImplementedError("Not yet implemented")


