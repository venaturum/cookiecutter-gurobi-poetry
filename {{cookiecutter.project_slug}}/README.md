# {{ cookiecutter.project_name}}

**{{ cookiecutter.short_description }}**


{%- set license_classifiers = {
    "MIT license": "MIT",
    "Apache Software License 2.0": "Apache-2.0",
    "GNU General Public License v3.0": "GPL-3.0-only",
    "GNU General Public License v2.0": "GPL-2.0-only",
    "BSD 3-Clause 'New' or 'Revised' License": "BSD-3-Clause",
    "GNU Lesser General Public License v2.1": "LGPL-2.1-only",
    "BSD 2-Clause 'Simplified' License": "BSD-2-Clause",
} -%}
{% if cookiecutter.open_source_license in license_classifiers %}

## License

This project is licensed under the {{ license_classifiers[cookiecutter.open_source_license] }} License - see the LICENSE file for details.
{%- endif %}

## Acknowledgments

This package was created with [`Cookiecutter`](https://github.com/cookiecutter/cookiecutter) and the [`cookiecutter-gurobi-poetry`](https://github.com/venaturum/cookiecutter-gurobi-poetry) project template.