# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import argparse
import copy
import logging
from pprint import pprint
import sys

from datadog_builder import init
from datadog_builder import update
from datadog_builder import validate


logging.basicConfig(level=logging.DEBUG)

LOG = logging.getLogger(__name__)


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()

    parser.add_argument('--auth-config',
                        dest='auth_config',
                        # required=True,
                        type=argparse.FileType('r'),
                        help='Authentication Information')

    parser.add_argument('--config',
                        dest='config',
                        # required=True,
                        type=argparse.FileType('r'),
                        help='Job information')

    subparsers = parser.add_subparsers()

    init.add_arguments(subparsers)
    update.add_arguments(subparsers)
    validate.add_arguments(subparsers)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == '__main__':
    main()