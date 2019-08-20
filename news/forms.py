from django import forms


class ForgetForm(forms.Form):
    email = forms.EmailField()


class PasswordChangeForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput())
    verify_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        new_password = self.cleaned_data.get("new_password")
        verify_password = self.cleaned_data.get("verify_password")
        if new_password != verify_password:
            raise forms.ValidationError("Not equal")