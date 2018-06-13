import datetime
import os
import uuid
from binascii import hexlify

import peewee
from peewee import CharField, BooleanField, IntegerField, DoesNotExist, \
    DateTimeField
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from openapprentice.errors import notfound
from openapprentice import user_db


class User(peewee.Model):
    # Required:
    # Required:
    uuid = CharField(
        primary_key=True,
        default=str(uuid.uuid4()),
        help_text="The user's unique identifier",
        verbose_name="uuid"
    )
    email = CharField(
        unique=True,
        help_text="The user's email",
        verbose_name="email"
    )
    password = CharField(
        help_text="The user's password",
        verbose_name="password"
    )
    scope = CharField(
        default="user",
        help_text="The user's scope",
        verbose_name="scope"
    )
    coach = CharField(
        null=True,
        help_text="The user's coach",
        verbose_name="coach"
    )
    creation_date = DateTimeField(
        default=datetime.datetime.utcnow(),
        help_text="When the user was created",
        verbose_name="Creation date"
    )
    last_access_date = DateTimeField(
        null=True,
        help_text="When was the last time the user logged in",
        verbose_name="Last access date"
    )
    is_confirmed = BooleanField(
        default=False,
        help_text="Did the user confirm his email adress",
        verbose_name="Is confirmed"
    )
    confirmed_by = CharField(
        null=True,
        help_text="Who was the user confirmed by",
        verbose_name="Confirmed by"
    )
    confirmed_on = DateTimeField(
        null=True,
        help_text="When was the user confirmed",
        verbose_name="Confirmed on"
    )
    secret = CharField(
        default=hexlify(os.urandom(32)).decode(),
        help_text="The user's secret used to access the API",
        verbose_name="API Secret"
    )
    has_api_access = BooleanField(
        default=False,
        help_text="Does the user have access to the API",
        verbose_name="Has API access"
    )
    last_modified = DateTimeField(
        default=datetime.datetime.utcnow(),
        help_text="When was the user last modified ?",
        verbose_name="Last modified"
    )
    access_count = IntegerField(
        default=0,
        help_text="How many times did the user login/used the API ?",
        verbose_name="Access count"
    )
    is_authenticated = BooleanField(
        default=False,
        help_text="Is the user currently logged in ?",
        verbose_name="Is authenticated"
    )

    # Optional
    username = CharField(
        null=True,
        unique=True,
        help_text="User's username/display name",
        verbose_name="Username"
    )
    first_name = CharField(
        null=True,
        help_text="User first name",
        verbose_name="First name"
    )
    last_name = CharField(
        null=True,
        help_text="User's last name",
        verbose_name="Last name"
    )
    phone_number = CharField(
        null=True,
        help_text="User's phone number",
        verbose_name="Phone number"
    )
    birthday = DateTimeField(
        null=True,
        help_text="User's birthday",
        verbose_name="Birthday"
    )
    gender = CharField(
        null=True,
        help_text="User's gender",
        verbose_name="Gender"
    )
    extra_info = CharField(
        null=True,
        help_text="User's extra info (Bio, etc)",
        verbose_name="Extra info"
    )
    position = CharField(
        null=True,
        help_text="Where is the user located ?",
        verbose_name="Position"
    )
    twitter = CharField(
        null=True,
        help_text="User's twitter account",
        verbose_name="Twitter"
    )
    stackoverflow = CharField(
        null=True,
        help_text="User's StackOverflow account",
        verbose_name="StackOverflow"
    )
    devrant = CharField(
        null=True,
        help_text="User's DevRant account",
        verbose_name="DevRant"
    )
    github = CharField(
        null=True,
        help_text="User's GitHub account",
        verbose_name="GitHub"
    )
    gitlab = CharField(
        null=True,
        help_text="User's GitLab account",
        verbose_name="GitLab"
    )
    bitbucket = CharField(
        null=True,
        help_text="User's BitBucket account",
        verbose_name="BitBucket"
    )
    cloudforge = CharField(
        null=True,
        help_text="User's CloudForge account",
        verbose_name="CloudForge"
    )
    linkedin = CharField(
        null=True,
        help_text="User's LinkedIn account",
        verbose_name="LinkedIn"
    )
    website = CharField(
        null=True,
        help_text="User's personal webiste",
        verbose_name="Personal Website"
    )

    class Meta:
        # This model uses the "user.db" database.
        database = user_db


def create_user(email, password, scope):
    hashed_password = generate_password_hash(password, method='sha256')

    return User.create(
        uuid=str(uuid.uuid4()),
        email=email.lower(),
        password=hashed_password,
        scope=scope.lower(),
        coach=None,
        creation_date=datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        last_access_date=None,
        is_confirmed=False,
        confirmed_by=None,
        confirmed_on=None,
        secret=hexlify(os.urandom(32)).decode(),
        has_api_access=False,
        last_modified=datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        access_count=0,
        is_authenticated=False,
        username=None,
        first_name=None,
        last_name=None,
        phone_number=None,
        birthday=None,
        gender=None,
        extra_info=None,
        position=None,
        twitter=None,
        stackoverflow=None,
        devrant=None,
        github=None,
        Gitlab=None,
        bitbucket=None,
        cloudforge=None,
        linkedin=None,
        website=None
    )


def get_user_dict(user):
    data = {}
    data['access_count'] = user.access_count
    data['birthday'] = user.birthday
    data['bitbucket'] = user.bitbucket
    data['cloudforge'] = user.cloudforge
    data['coach'] = user.coach
    data['confirmed_by'] = user.confirmed_by
    data['confirmed_on'] = user.confirmed_on
    data['creation_date'] = user.creation_date
    data['devrant'] = user.devrant
    data['email'] = user.email
    data['extra_info'] = user.extra_info
    data['first_name'] = user.first_name
    data['gender'] = user.gender
    data['github'] = user.github
    data['gitlab'] = user.gitlab
    data['has_api_access'] = user.has_api_access
    data['is_authenticated'] = user.is_authenticated
    data['is_confirmed'] = user.is_confirmed
    data['last_access_date'] = user.last_access_date
    data['last_modified'] = user.last_modified
    data['last_name'] = user.last_name
    data['linkedin'] = user.linkedin
    data['password'] = user.password
    data['phone_number'] = user.phone_number
    data['position'] = user.position
    data['scope'] = user.scope
    data['secret'] = user.secret
    data['stackoverflow'] = user.stackoverflow
    data['twitter'] = user.twitter
    data['username'] = user.username
    data['uuid'] = user.uuid
    data['website'] = user.website
    return data


class UserLoginFlask(UserMixin):
    """
    This class is the classed user by the LoginManager to handle users.
    It is more or less a copy of the User class from the models.
    """

    def __init__(self, userid):
        """
        Get the user and set the self variables properly.
        :param userid: The user id to get and setup
        """
        user = get_user(userid)
        self.access_count = user.access_count
        self.birthday = user.birthday
        self.bitbucket = user.bitbucket
        self.cloudforge = user.cloudforge
        self.coach = user.coach
        self.confirmed_by = user.confirmed_by
        self.confirmed_on = user.confirmed_on
        self.creation_date = user.creation_date
        self.devrant = user.devrant
        self.email = user.email
        self.extra_info = user.extra_info
        self.first_name = user.first_name
        self.gender = user.gender
        self.github = user.github
        self.gitlab = user.gitlab
        self.has_api_access = user.has_api_access
        self.is_authenticated = user.is_authenticated
        self.is_confirmed = user.is_confirmed
        self.last_access_date = user.last_access_date
        self.last_modified = user.last_modified
        self.last_name = user.last_name
        self.linkedin = user.linkedin
        self.password = user.password
        self.phone_number = user.phone_number
        self.position = user.position
        self.scope = user.scope
        self.secret = user.secret
        self.stackoverflow = user.stackoverflow
        self.twitter = user.twitter
        self.username = user.username
        self.uuid = user.uuid
        self.website = user.website

    def __repr__(self):
        """
        The representation method.
        :return: Returns the id, name and is_authenticated for a user.
        """
        return "%s/%s/%s" % (self.uuid, self.email, self.is_authenticated)

    def is_active(self):
        """
        Returns True if user has it's email confirmed, False otherwise. (Default=False)
        """
        return self.is_confirmed

    def get_id(self):
        """
        Returns the user's id.
        """
        return self.uuid

    def is_authenticated(self):
        """
        Returns the value of `is_authenticated`
        """
        return self.is_authenticated

    def is_anonymous(self):
        """
        False, as anonymous users aren't supported.
        """
        return False

    def is_confirmed(self):
        """
        Returns True if user has it's email confirmed, False otherwise. (Default=False)
        """
        return self.is_confirmed


def get_user(uid):
    """
    This function will find a user based on it's uuid or username and return
    a user object.

    :param uid: The email/uuid of the user you want

    :return: Returns a user object based on `uid`
    """

    not_found = 0
    # These initializations are to make PEP happy and silence warnings
    f_user = None

    # Try and get the user by email
    try:
        user = User.get(User.email == uid.encode("utf-8").lower())
    except DoesNotExist:
        not_found += 1
    else:
        f_user = user
    # Try and query the user by uuid
    try:
        user = User.get(User.uuid == uid)
    except DoesNotExist:
        not_found += 1
    else:
        f_user = user

    # If none of those worked, throw an error
    if not_found == 2:
        raise notfound.NotFoundError(
            "User {} not found.".format(uid),
            "Check your spelling or check the client_id given and "
            "try again.")
    return f_user


def _reset_db():
    User.drop_table()
    User.create_table()
    user = create_user("admin@openapprentice.org", "oa", "admin")
    user.is_confirmed = True
    user.confirmed_on = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    user.confirmed_by = "admin"
    user.username = "Administrator"
    user.save()

