# Jinja2 MJML

Micro-package that integrates [MJML](https://mjml.io/) 
with [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/).

Under the hood it uses [mjml_python](https://pypi.org/project/mjml-python/) 
package, that is a wrapper around [rust port](https://github.com/jolimail/mrml-core)
of MJML.

## Example

```python
from jinja2_mjml import Environment

# MJMLEnvironment it's thin wrapper around jinja2.Environment,
# so you can use all the features of Jinja2 package.
environment = Environment()
template = environment.from_string('''
    <mjml>
      <mj-body>
        <mj-section>
          <mj-column>
            <mj-text>Hello {{ name }}!</mj-text>
          </mj-column>
        </mj-section>
      </mj-body>
    </mjml>
''')

# Render MJML template to HTML
print(template.render(name='MJML'))
```