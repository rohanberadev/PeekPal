from django import forms

class CreatePostForm (forms.Form):
    hint_or_question = forms.CharField(max_length=255, required=True)
    answer = forms.CharField(required=True)
    option1 = forms.CharField(required=True)
    option2 = forms.CharField(required=True)
    option3 = forms.CharField(required=False)
    option4 = forms.CharField(required=False)

class PredictOnPostForm (forms.Form):
    post_id = forms.CharField(required=True)
    prediction = forms.CharField(required=True)