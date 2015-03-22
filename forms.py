from writingfield import FullScreenTextarea

class YourAdminForm(forms.ModelForm):

    class Meta:
        widgets = {
        'mytextarea': FullScreenTextarea()
        }
