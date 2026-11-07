import pytest
from src.fake_db import db
from src.fake_db.database import Database


@pytest.fixture(autouse=True)
def reset_database():
    """Give every test the original data without replacing the shared object."""
    original_users, original_id = db._users, db._id
    fresh = Database()
    db._users, db._id = fresh._users, fresh._id
    yield
    db._users, db._id = original_users, original_id
