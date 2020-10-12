#
# Copyright 2020 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from metadata_converter.generate import generate_dlf_yaml
import sys
import yaml

#
# This example illustrates how to invoke the exchange metadata converter
# programatically, using the DLF template
# Required parameters:
# /path/to/placeholder/yaml see examples in dax-data-set-descriptors/
if __name__ == "__main__":

    try:

        if len(sys.argv) != 2:
            print('Usage: {} {}'
                  .format(sys.argv[0],
                          '/path/to/placeholder/yaml'))
            sys.exit(1)

        with open(sys.argv[1], 'r') as source_yaml:
            placeholder_yaml = yaml.load(source_yaml,
                                         Loader=yaml.FullLoader)

        # Generate DLF-compatible YAML by replacing the placeholders
        # in  "templates/dlf_out.yaml" with values from placeholder_yaml
        generated_dlf_yaml = generate_dlf_yaml(placeholder_yaml)

        # print template YAML with replacements in place
        print(generated_dlf_yaml)

    except Exception as ex:
        print(ex)