from django.forms.widgets import ClearableFileInput

class CustomClearableFileInput(ClearableFileInput):
    template_name = "custom_clearable_file_input.html"  # Override the default template
