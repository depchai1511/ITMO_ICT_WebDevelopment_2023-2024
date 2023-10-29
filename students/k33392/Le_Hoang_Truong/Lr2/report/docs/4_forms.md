# Form

Мое Django приложение содержит следующие формы для обработки данных внутри приложения.

## Форма регистрации (RegistrationForm)

- **Поля**:  
  - **Имя (name)**: Текстовое поле для ввода имени пользователя.
  - **Имя пользователя (username)**: Текстовое поле для ввода имени пользователя.
  - **Email (email)**: Поле для ввода адреса электронной почты.
  - **Пароль (password1 и password2)**: Поля для ввода пароля (поле для ввода и подтверждение пароля).

- **Методы**:
  - **clean_password2()**: Проверяет, что введенные пароли совпадают и не являются пустыми.
  - **clean_username()**: Проверяет валидность имени пользователя и проверяет, не существует ли уже пользователя с таким именем.
  - **save()**: Создает нового пользователя с введенными данными, если они прошли все проверки.

## Форма обновления пользователя (UserUpdateForm)

- **Модель**: Использует модель `User` для обновления данных пользователя.

- **Поля**: 
  - **Имя (name)**: Поле для обновления имени пользователя.
  - **Имя пользователя (username)**: Поле для обновления имени пользователя.
  - **Email (email)**: Поле для обновления адреса электронной почты.
  - **Дата рождения (birthday)**: Поле для обновления даты рождения пользователя.

Эти формы позволяют пользователям регистрироваться в системе, обновлять свои данные и подвергаются различным проверкам, чтобы гарантировать правильность и безопасность данных.


## Реализация

```python
from typing import Any
from django import forms 
import re
from .models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form) :
    name = forms.CharField(label = 'Name', max_length=30)
    username = forms.CharField(label = 'Username', max_length=30)
    email = forms.EmailField(label = 'Email')
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput())
    password2 = forms.CharField(label = 'Password', widget = forms.PasswordInput())

    def clean_password2(self) :
        if 'password1' in self.cleaned_data :
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1 :
                return password2
        raise forms.ValidationError('Password is invalid')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username) :
            raise forms.ValidationError('Username has invalid character')
        try :
            User.objects.get(username=username)
        except ObjectDoesNotExist :
            return username 
        raise forms.ValidationError('Account have already existed')
    
    def save(self) :
        User.objects.create_user(name = self.cleaned_data['name'],username=self.cleaned_data['username'],email = self.cleaned_data['email'],password= self.cleaned_data['password1'])

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "username", "email", "birthday"]


```