from trainer import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    true_picture_url = db.Column(db.String(512))
    false_picture_url = db.Column(db.String(512))


    def set_true_picture(self, true_picture_url):
        self.true_picture_url = true_picture_url

    def set_false_picture(self, false_picture_url):
        self.false_picture_url = false_picture_url
