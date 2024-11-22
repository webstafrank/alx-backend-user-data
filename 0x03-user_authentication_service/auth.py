class Auth:
    """Authentication class to interact with users and sessions."""

    def __init__(self):
        self._db = DB()

    def destroy_session(self, user_id):
        """
        Destroys the session of the user by setting session_id to None.

        Args:
            user_id (int): The ID of the user whose session should be destroyed.

        Returns:
            None
        """
        # Find the user by ID
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None

        # Update the session_id to None
        user.session_id = None

        # Commit the changes to the database
        self._db.session.commit()

