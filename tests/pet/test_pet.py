from datetime import datetime

from nguylinc_python_utils.sqlalchemy import deserialize_body
from openapi_client import Pet, PutPetProps

from tests.clients import session, petApi, configuration
from models.resources.user import User
from tests.data.pet import PETS
from tests.data.user import USER


class Test:
    user_id: str = None
    token: str = None
    created_pets: list[Pet] = []

    @classmethod
    def setup_method(cls):
        # Add user
        user = deserialize_body(User, USER, User.google_fields)
        user.created_at = datetime.now()
        session.add(user)
        session.commit()
        session.refresh(user)
        cls.user_id = user.id
        configuration.access_token = user.generate_token()

        # Add pets
        for pet in PETS:
            PutPetProps.model_validate(pet)
        for pet in PETS:
            pet = petApi.put(PutPetProps(**pet))
            cls.created_pets.append(pet)
        session.commit()

    def test_get_pets(self):
        all_ids = [p.id for p in petApi.get_items()]
        for pet in self.created_pets:
            assert pet.id in all_ids

    @classmethod
    def teardown_method(cls):
        # Delete user and their pets
        session.query(User).filter(User.id == cls.user_id).delete()
        session.commit()
