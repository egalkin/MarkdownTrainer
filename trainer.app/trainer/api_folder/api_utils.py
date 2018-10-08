import os
import random
from random import shuffle

from flask_restful import abort

from trainer import TASK_IMAGE_FOLDER, db
from trainer.models import Task

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    extension = filename.rsplit('.', 1)[1].lower()
    return '.' in filename and \
           extension in ALLOWED_EXTENSIONS, extension


def upload_images(pictures):
    if 'true_image' not in pictures and 'false_image' not in pictures:
        abort(406, message='No images presented')
    true_image, false_image = pictures['true_image'], pictures['false_image']
    if true_image.filename == '' or false_image.filename == '':
        abort(406, message='No images selected')
    is_ok_true, extension_true = allowed_file(true_image.filename)
    is_ok_false, extension_false = allowed_file(false_image.filename)
    if is_ok_true and is_ok_false:
        new_task = Task()
        db.session.add(new_task)
        db.session.commit()
        true_image_url = os.path.join(TASK_IMAGE_FOLDER,
                                      '{}true_image.{}'.format(new_task.id, extension_true))
        false_image_url = os.path.join(TASK_IMAGE_FOLDER,
                                       '{}false_image.{}'.format(new_task.id, extension_false))
        new_task.set_true_picture(true_image_url)
        new_task.set_false_picture(false_image_url)
        true_image.save(true_image_url)
        false_image.save(false_image_url)
        db.session.commit()
    return 'Ok'


def get_random_list(num_of_elem):
    elems = Task.query.all()
    shuffle(elems)
    return elems[:num_of_elem] if num_of_elem <= len(elems) else elems
