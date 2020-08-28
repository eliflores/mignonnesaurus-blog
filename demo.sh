#!/usr/bin/env bash

MY_BLOG_PASSWORD=$MY_BLOG_USERNAME && MY_BLOG_PASSWORD=$MY_BLOG_PASSWORD && pytest demos/blog_demo.py -v --browser=firefox --server=localhost --port=8000 --demo_mode --slow --start_page=http://localhost:8000
