from django import forms

class AddFriendForm (forms.Form):
    user_id = forms.CharField(required=True)


class FriendRequestForm (forms.Form):
    freind_request_id = forms.CharField(required=True)
    status = forms.ChoiceField(required=True, choices=[('Accept', 'accept'), ('Decline', 'decline')])