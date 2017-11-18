from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "你的全名"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "邮箱"
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                "placeholder": "Your message"
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        """ 
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com 必须是这个域名的邮箱")
        """
        return email