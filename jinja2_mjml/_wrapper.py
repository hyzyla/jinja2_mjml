from typing import Any

import mjml
import jinja2


class Template(jinja2.Template):

    def render(self, *args: Any, **kwargs: Any) -> str:
        """Render MJML markup template to HTML."""

        # Render MJML markup
        markup = super().render(*args, **kwargs)

        # Convert MJML markup to HTML
        return mjml.mjml2html(markup)


class Environment(jinja2.Environment):
    template_class = Template
