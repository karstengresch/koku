#
# Copyright 2018 Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
"""Custom Koku Dev Middleware."""
import logging
from base64 import b64encode
from json import dumps as json_dumps
from unittest.mock import Mock

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from api.common import RH_IDENTITY_HEADER
from api.iam.models import User

LOG = logging.getLogger(__name__)


class DevelopmentIdentityHeaderMiddleware(MiddlewareMixin):  # pylint: disable=too-few-public-methods
    """Middleware to add 3scale header for development."""

    header = RH_IDENTITY_HEADER

    def process_request(self, request):  # pylint: disable=no-self-use
        """Process request for to add header.

        Args:
            request (object): The request object

        """
        if hasattr(request, "META"):
            if settings.DEVELOPMENT_IDENTITY:
                identity_header = settings.DEVELOPMENT_IDENTITY

                user_dict = identity_header.get("identity", {}).get("user")
                user = Mock(
                    spec=User,
                    access=user_dict.get("access"),
                    username=user_dict.get("username", "user_dev"),
                    email=user_dict.get("email", "user_dev@foo.com"),
                    admin=user_dict.get("is_org_admin", False),
                    customer=Mock(account_id=identity_header.get("account_number", "10001")),
                    req_id="DEVELOPMENT",
                )

                request.user = user
            else:
                identity_header = {
                    "identity": {
                        "account_number": "10001",
                        "type": "User",
                        "user": {"username": "user_dev", "email": "user_dev@foo.com", "is_org_admin": True},
                    },
                    "entitlements": {"cost_management": {"is_entitled": True}},
                }
            json_identity = json_dumps(identity_header)
            LOG.info("Identity: %s", json_identity)
            dev_header = b64encode(json_identity.encode("utf-8"))
            request.META[self.header] = dev_header
