import web
from Models import RegisterModel, LoginModel

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/postregistration', 'PostRegistration',
    '/check-login', 'Checklogin'

)

render = web.template.render("views/templates", base="MainLayout")
app = web.application(urls, globals())


# Classes/Routes



class Home:
    def GET(self):
        return render.Home()


class Register:
    def GET(self):
        return render.Register()

class Login:
    def GET(self):
        return render.Login()


class PostRegistration:
    def POST(self):
        data = web.input()

        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username

class Checklogin:
    def POST(self):
        data = web.input()
        login = LoginModel.loginModel()
        login.check_user(data)
        isCorrect = login.check_user(data)

        if isCorrect:
            return isCorrect

        return "error"

if __name__ == "__main__":
    app.run()
