from sqlalchemy.orm.exc import NoResultFound

class Auth:
    """Authentication class to interact with users and sessions."""

    def __init__(self):
        self._db = DB()

    def get_user_from_session_id(self, session_id):
        """
        Retrieves the user associated with the given session_id.

        Args:
            session_id (str): The session ID of the user.

        Returns:
            User or None: The user object associated with the session ID, or None if no user found.
        """
        if session_id is None:
            return None

        try:
            # Assuming that the session_id is stored in the user object.
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

