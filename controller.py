import web


urls = (
    '/', 'home',
    '/register', 'register'
)

render = web.template.render("views/templates", base="mainLayout")
app = web.application(urls, globals())


# Classes/Routes



class home:
    def GET(self):
        return render.home()

class register:
    def GET(self):
        return render.register()

if __name__ == "__main__":
    app.run()