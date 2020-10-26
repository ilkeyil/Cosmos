import math

from django.contrib.auth.models import Group
from django.core.validators import ValidationError
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField

from apps.users.models.board import Board

# Committee model is defined here


def validate_aspect_ratio(image):
    # Function used to check if the board picture uses the correct aspect ratio
    ratio = 16 / 9
    if not math.isclose(image.width / image.height, ratio, rel_tol=1e-6):
        raise ValidationError("The aspect ratio is not correct. The aspect ratio should be: " + str(ratio))


class Committee(models.Model):
    """
    Extension of Django Group model to store extra data of committees.

    - `name`, `permissions`: self-explanatory

    To get all groups of a user you can do this:

    - user.groups.all()

    To get all users of a group:

    - group.user_set.all()
    """

    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    description = HTMLField(blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, blank=True, null=True)
    pretix_team_token = models.CharField(
        max_length=64, blank=True
    )  # Pretix token gives users who are part of the committee the right to create events
    display_name = models.CharField(max_length=50, blank=False, default="None")
    slug = models.CharField(max_length=20, blank=False, default="None")

    photo = models.ImageField(
        upload_to="committees",
        default="committees/default.png",
        validators=[validate_aspect_ratio],
    )

    # @property is used to return the output of a function as type of variable so it can be used in the template
    # https://docs.python.org/3/library/functions.html#property
    @property
    def name(self):
        return self.group.name

    # @property is used to return the output of a function as type of variable so it can be used in the template
    # https://docs.python.org/3/library/functions.html#property
    @property
    def permissions(self):
        return self.group.permissions

    def __str__(self):
        return f"{self.name}: {self.description}"
