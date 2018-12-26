from django import forms

TASK_PRIORITIES = (
    (0, 'High'),
    (1, 'Moderate'),
    (2, 'Low'),
    (3, 'done')
)

class TodoForm(forms.Form):
    text = forms.CharField(
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter todo task',
                'aria-label': 'Todo',
                'aria-describedby': 'add-btn',
                'style': 'z-index:0'
            }
        )
    )

    priority = forms.CharField(
        label='Task Priority: ',
        required=True,
        widget=forms.RadioSelect(
            choices=TASK_PRIORITIES,
        )
    )  

class MailForm(forms.Form):
    notes = forms.CharField(
        max_length=500,
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter description/message',
                'aria-label': 'Todo',
                'aria-describedby': 'add-btn',
            }
        )
    )

    mailto = forms.CharField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter recipient email',
                'aria-label': 'Todo',
                'aria-describedby': 'add-btn',
            }
        )
    )