import web
from Models import RegisterModel, LoginModel, Posts

web.config.debug = False

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/logout', "Logout",
    '/postregistration', 'PostRegistration',
    '/check-login', 'Checklogin'
    '/post-activity', 'PostActivity',
    '/profile/{.*}/info', "UserInfo",
    '/settings', "UserSettings",
    '/update-settings', "UpdateSettings",
    '/profile/{.*}', "UserProfile",
    '/submit-comment', "SubmitComment"
)


app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': 'none'})
session_data = session._initializer

render = web.template.render("views/Templates", base="MainLayout", globals={'session': session_data, 'current_user': session_data["user"]})



# Classes/Routes



class Home:
    def GET(self):
        # data = type('obj', (object,), {"username": "nick1", "password": "password"})
        #
        # login = LoginModel.loginModel()
        # isCorrect = login.check_user(data)
        #
        # if isCorrect:
        #     session_data["user"] = isCorrect

        post_model = Posts.Posts()
        posts = post_model.get_all_posts()

        return render.Home(posts)


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
            session_data["user"] = isCorrect
            return isCorrect

        return "error"

class PostActivity:
    def POST(self):
        data = web.input()
        data.usernaame = session_data['user']['username']

        post_model = Posts.Posts()
        post_model.insert_post(data)
        return "success"

class UserProfile:
    def GET(self,user):
        data = type('obj', (object,), {"username": "nick1", "password": "password"})

        login = LoginModel.loginModel()
        user_info = login.get_profile(user)
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data["user"] = isCorrect

        post_model = Posts.Posts()
        posts = post_model.get_user_posts(user)
        return render.Profile(posts, user_info)

class UserInfo:
    def GET(self, user):
        data = type('obj', (object,), {"username": "nick1", "password": "password"})

        login = LoginModel.loginModel()
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data["user"] = isCorrect

        user_info = login.get_profile(user)

        return render.Info(user_info)

class UserSettings:
    def GET(self):
        data = type('obj', (object,), {"username": "nick1", "password": "password"})

        login = LoginModel.loginModel()
        isCorrect = login.check_user(data)

        if isCorrect:
            session_data["user"] = isCorrect

        return render.Info()

class SubmitComment:
    def POST(self):
        data = web.input()
        data.username = session_data["user"]["username"]

        post_model = Posts.Posts()
        added_comment = post_model.add_comment(data)

        if added_comment:
            return added_comment
        else:
            return "fatal error"

class UpdateSettings:
    def Post(self):
        data = web.input()
        data.username = session_data["user"]["username"]

        settings_model = LoginModel.loginModel()
        if settings_model.update(data):
            return "success"
        else:
            return "A fatal error has occured."




class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None

        session.kill()
        return "success"

if __name__ == "__main__":
    app.run()
