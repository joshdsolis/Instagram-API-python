#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
from decouple import config


user = config('DB_USER')
password = config('DB_PASS')

InstagramAPI = InstagramAPI(user, password)
InstagramAPI.login()  # login

photo_path = '/Users/joshsolis/repos/joshdsolis/Instagram-API-python/examples/pictures/meme.jpg'
caption = "Sample photo"
InstagramAPI.uploadPhoto(photo=photo_path, caption=caption)
