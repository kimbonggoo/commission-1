from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.forms import TextInput

class CustomLoginForm(AuthenticationForm):
    username = UsernameField(
        label=('아이디'),
        widget=forms.TextInput(
            attrs={
                'placeholder': '',
            }
        )
    )

class CustomUserForm(UserCreationForm):

    password1 = forms.CharField(
        label=('비밀번호'),
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호를 입력해 주세요.',
            }
        ),
    )
    password2 = forms.CharField(
        label=('비밀번호 확인'),
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호를 한 번 더 입력해 주세요.',
            }
        ),
    )
    
    class Meta:
        model = get_user_model()

        fields = (
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'phone',
        )

        labels = {
            'username': '아이디',
            'email': '이메일',
            'first_name': '이름',
            'phone': '휴대전화',
            'exchange': '가입거래소',
            'uid': 'UID',
        }

        widgets = {
            'username': TextInput(
                attrs={
                    'placeholder': '아이디를 입력해 주세요.'
                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'bitsolution@email.com'
                }
            ),
            'first_name': TextInput(
                attrs={
                    'placeholder': '홍길동'
                }
            ),
            'phone': TextInput(
                attrs={
                    'placeholder': '01012345678'
                }
            ),
        }

        help_texts = {
            'username': None,
        }
