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
    error_messages = {
        "invalid_login": (
            "올바른 사용자 아이디와 비밀번호를 입력해주세요. "
            "계정 활성화가 필요한 경우에는 관리자에게 문의해주시길 바랍니다."
        ),
    }

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
            'amount',
        )

        labels = {
            'username': '아이디',
            'email': '이메일',
            'first_name': '이름',
            'phone': '휴대전화',
            'exchange': '가입거래소',
            'uid': 'UID',
            'amount': '투자금액'
        }

        widgets = {
            'username': TextInput(
                attrs={
                    'placeholder': '아이디를 입력해 주세요.',
                    'minlength': '3',
                    'maxlength': '20'
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
            'amount': TextInput(
                attrs={
                    'placeholder': '숫자만 입력해 주세요.',
                    'pattern': "[0-9]+",
                }
            ),
        }

        help_texts = {
            'username': '* 3자 이상 20자 이하 문자, 숫자 그리고 @/./+/-/_만 가능합니다.',
        }
